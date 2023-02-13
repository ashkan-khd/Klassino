from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError

from announcement.models import Announcement


class AnnouncementForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        main_page = cleaned_data.get("main_page")
        student_page = cleaned_data.get("student_page")

        if (not main_page) and (not student_page):
            raise ValidationError(
                "هر اطلاعیه حداقل باید در یکی از صفحات نمایش داده شود!"
            )


@admin.register(Announcement)
class AdminStudent(admin.ModelAdmin):
    form = AnnouncementForm
    fields = ['title', 'context', 'main_page', 'student_page']

    class Meta:
        model = Announcement
