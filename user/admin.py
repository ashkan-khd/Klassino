from django import forms
from django.contrib import admin
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from jalali_date.admin import ModelAdminJalaliMixin
from unidecode import unidecode

from user.models import Assistant, Student, Teacher, City, State

admin.site.register(State)
admin.site.register(City)


class KarinoUserBaseForm(forms.ModelForm):
    def clean_password(self):
        if 'password' in self.changed_data:
            return make_password(self.data['password'])
        else:
            return self.data['password']

    def clean_phone_number(self):
        if 'phone_number' not in self.changed_data:
            return self.data['phone_number']
        phone_number = unidecode(self.data['phone_number'])
        if phone_number.startswith('0'):
            phone_number = '+98' + phone_number[1:]
        if not phone_number.startswith('+98') or len(phone_number) != 13:
            raise ValidationError('فرمت وارد شده صحیح نیست')
        return phone_number


class StudentForm(KarinoUserBaseForm):
    def clean_nationality_code(self):
        nationality_code = self.data['nationality_code']  # type: str
        if not nationality_code.isnumeric():
            raise ValidationError('شماره شناسنامه باید تنها از عدد تشکیل شود.')

        return nationality_code

    def validate_username(self):
        return self.data['username']

    def clean(self):
        validated_data = super().clean()
        validated_data['username'] = validated_data['nationality_code']

        return validated_data


@admin.register(Student)
class AdminStudent(ModelAdminJalaliMixin, admin.ModelAdmin):
    form = StudentForm
    list_display = ('id', 'nationality_code', 'get_full_name')
    fields = ['profile_image', 'password', 'phone_number', 'email', 'first_name', 'last_name', 'gender', 'birth_date',
              'nationality_code', 'city', 'school', 'is_active']

    def get_full_name(self, obj):
        return obj.get_full_name()

    get_full_name.short_description = 'نام'

    class Meta:
        model = Student


@admin.register(Teacher)
class AdminTeacher(ModelAdminJalaliMixin, admin.ModelAdmin):
    form = KarinoUserBaseForm
    list_display = ('id', 'get_full_name')
    fields = ['profile_image', 'username', 'password', 'phone_number', 'email', 'first_name', 'last_name',
              'description', 'is_active', 'is_top', 'home_page_image']

    def get_full_name(self, obj):
        return obj.get_full_name()

    get_full_name.short_description = 'نام'

    class Meta:
        model = Teacher


@admin.register(Assistant)
class AdminAssistant(ModelAdminJalaliMixin, admin.ModelAdmin):
    form = KarinoUserBaseForm
    list_display = ('id', 'get_full_name')
    fields = ['profile_image', 'username', 'password', 'phone_number', 'email', 'first_name', 'last_name',
              'description', 'is_active', 'is_top', 'home_page_image']

    def get_full_name(self, obj):
        return obj.get_full_name()

    get_full_name.short_description = 'نام'

    class Meta:
        model = Assistant
