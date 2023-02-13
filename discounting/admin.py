from django import forms
from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models.assistance_discount import AssistanceDiscount
from .models.course_discount import CourseDiscount
from django.core.exceptions import ValidationError
from .service import random_generator


class DiscountForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DiscountForm, self).__init__(*args, **kwargs)
        self.fields['code'].help_text = 'در صورت وارد نکردن کد، یک کد تصادفی ساخته می شود.'

    def clean_code(self):
        data = self.data['code']
        if not data:
            return random_generator.make_new_code()
        return data

    def clean(self):
        cleaned_data = super().clean()
        end = cleaned_data['end_time']
        start = cleaned_data['start_time']
        if start > end:
            raise ValidationError({
                'end_time': 'زمان پایان باید پس از زمان شروع باشد',
            })
        return cleaned_data

    class Meta:
        exclude = ['is_used']


@admin.register(AssistanceDiscount)
class AdminAssistanceDiscount(ModelAdminJalaliMixin, admin.ModelAdmin):
    form = DiscountForm

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            return super().get_readonly_fields(request, obj)
        else:
            return ['code']

    class Meta:
        model = AssistanceDiscount


@admin.register(CourseDiscount)
class AdminCourseDiscount(ModelAdminJalaliMixin, admin.ModelAdmin):
    form = DiscountForm

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            return super().get_readonly_fields(request, obj)
        else:
            return ['code']

    class Meta:
        model = CourseDiscount
