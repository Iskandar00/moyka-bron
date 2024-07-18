from rest_framework.exceptions import ValidationError


def phone_number_validate(phone_number: str):
    if len(phone_number) != 13 or not phone_number.startswith('+998') or not phone_number[1:].isdigit():
        raise ValidationError('phone number is not valid.')
