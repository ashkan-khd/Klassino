from django.contrib import admin
from jalali_date import date2jalali
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Transaction, ManualTransaction


@admin.register(Transaction)
class TransactionAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['__str__', 'transaction_time']
    exclude = ['is_deleted']

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(ManualTransaction)
class TransactionAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['__str__', 'transaction_time']
