from django.shortcuts import render, redirect
from django.contrib import messages
from .models import student
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .validators import CustomPasswordValidator
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password

def register_page(request):
    if request.method == 'POST':
        data = request.POST
        fname = data.get('fname')
        lname = data.get('lname')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Validate the password using the custom validator
        password_validator = CustomPasswordValidator(min_length=8)
        try:
            password_validator.validate(password)
        except ValidationError as e:
            messages.warning(request, str(e))
            return redirect('register_page')

        # Check if the username or email already exists
        if student.objects.filter(username=username).exists():
            messages.warning(request, "Username already taken")
            return redirect('register_page')
        if student.objects.filter(email=email).exists():
            messages.warning(request, "Email already taken")
            return redirect('register_page')

        # Hash the password before storing it
        hashed_password = make_password(password)
        print("Hashed Password:", hashed_password)

        # Create a new student only if the username and email are unique
        new_student = student.objects.create(
            fname=fname,
            lname=lname,
            username=username,
            email=email,
            password=hashed_password,  # Store the hashed password
        )

        messages.success(request, "Successfully registered")
        return redirect('register_page')

    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username').strip()
        password = data.get('password').strip()

        # Get the user from the database
        user = student.objects.filter(username=username).first()

        if not user:
            messages.warning(request, "Username doesn't exist")
            return redirect('login_page')

        # Check the password manually
        if not check_password(password, user.password):
            messages.warning(request, "Invalid password")
            return redirect('login_page')

        # If the password is correct, proceed with login
        messages.info(request, "Success")
        return redirect('login_page')

    return render(request, 'login.html')
