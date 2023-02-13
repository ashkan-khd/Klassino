from rest_framework.authtoken.models import Token

from user.models import Student


def get_or_create_token(student: Student):
    token = Token.objects.filter(user=student).first()
    if token:
        return token

    token = Token.objects.create(user=student)
    return token


def revoke_token(token: Token):
    token.delete()
