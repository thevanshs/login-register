from django.core.exceptions import ValidationError
import re

class CustomPasswordValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                "Password must be at least {} characters long.".format(self.min_length)
            )

        if not re.search(r'\d', password):
            raise ValidationError("Password must contain at least one digit.")

        if not re.search(r'[A-Z]', password):
            raise ValidationError("Password must contain at least one uppercase letter.")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError("Password must contain at least one special character.")

    def get_help_text(self):
        return (
            "Password must be at least {} characters long, "
            "contain at least one digit, one uppercase letter, and one special character."
        ).format(self.min_length)
