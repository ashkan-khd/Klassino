from functools import reduce

from django.utils import timezone

from financial.models import Transaction


def calculate_account_charge(student):
    return reduce(lambda a1, a2: a1 + a2, list(map(lambda t: t.amount, student.transactions.all())))


def reduce_account_charge(student, amount):
    return Transaction.objects.create(user=student, amount=-(1 * amount), description='', transaction_time=timezone.now())


def increase_account_charge(student, amount):
    return Transaction.objects.create(user=student, amount=amount, description='', transaction_time=timezone.now())
