from django.contrib import admin
from jalali_date import date2jalali
from jalali_date.admin import ModelAdminJalaliMixin

from konkour.models import Konkour


@admin.register(Konkour)
class KonkourAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['name', 'get_jalali_date']

    def get_jalali_date(self, obj):
        return date2jalali(obj.date).strftime('%y/%m/%d')

    get_jalali_date.short_description = 'تاریخ برگزاری'
    get_jalali_date.admin_order_field = 'date'
