import random
import string

from django.conf import settings
from discounting.models import CourseDiscount, AssistanceDiscount


def get_random_string(length):
    letters = string.ascii_lowercase
    letters += string.ascii_uppercase
    letters += string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def make_new_code() -> str:
    while True:
        random_code = get_random_string(settings.CODE_LENGTH)
        if not (AssistanceDiscount.objects.filter(code=random_code).exists() or CourseDiscount.objects.filter(code=random_code).exists()):
            return random_code


