import jdatetime
from django.contrib.auth.hashers import make_password
from jalali_date import date2jalali
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from unidecode import unidecode

from introducing.serializers import AssistantIntroductionVideoSerializer
from mentoring.serializers import AssistancePackageSerializer
from user.models import Teacher, Assistant, Student, State, City


def generate_details_serializer(model_name):
    class KarinoUserSerializer(serializers.ModelSerializer):
        profile_image = serializers.SerializerMethodField()

        def get_profile_image(self, teacher):
            request = self.context.get('request')
            if teacher.profile_image:
                photo_url = teacher.profile_image.url
                return request.build_absolute_uri(photo_url)
            else:
                return None

        class Meta:
            model = model_name
            fields = ['id', 'first_name', 'last_name', 'profile_image', 'phone_number']

    return KarinoUserSerializer


USER_DETAILS_SERIALIZER_MAP = {
    Assistant: generate_details_serializer(Assistant),
    Student: generate_details_serializer(Student),
    Teacher: generate_details_serializer(Teacher)
}


class TopPersonSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ['id', 'first_name', 'last_name', 'image', 'short_description', 'description', ]

    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        image = obj.home_page_image or obj.profile_image
        request = self.context.get('request')
        if image:
            return request.build_absolute_uri(image.url)
        else:
            return None


class TopTeacherSerializer(TopPersonSerializer):
    class Meta:
        model = Teacher
        fields = TopPersonSerializer.Meta.fields


class TopAssistantSerializer(TopPersonSerializer):
    class Meta:
        model = Assistant
        fields = TopPersonSerializer.Meta.fields


class AssistantSerializer(serializers.ModelSerializer):
    introduction_videos = AssistantIntroductionVideoSerializer(many=True)
    packages = AssistancePackageSerializer(many=True)

    class Meta:
        model = Assistant
        fields = ['id', 'first_name', 'last_name', 'profile_image', 'short_description', 'description',
                  'introduction_videos', 'packages']


class TeacherSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'profile_image', 'short_description', 'description']

    def get_profile_image(self, teacher):
        request = self.context.get('request')
        if teacher.profile_image:
            photo_url = teacher.profile_image.url
            return request.build_absolute_uri(photo_url)
        else:
            return ""


class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'password',
            'phone_number',
            'gender',
            'birth_date',
            'nationality_code',
            'school',
            'city'
        ]

    def validate_password(self, password):
        return make_password(password)

    def validate_nationality_code(self, nationality_code):
        if not nationality_code.isnumeric():
            raise ValidationError('شماره شناسنامه تنها میتواند از عدد تشکیل شود')

        nationality_code = unidecode(nationality_code)
        if Student.objects.filter(nationality_code=nationality_code).exists():
            raise ValidationError('دانش‌آموز با این شماره شناسنامه از قبل ثبت‌نام شده است!')

        return nationality_code

    def validate_phone_number(self, phone_number: str):
        phone_number = unidecode(phone_number)
        if phone_number.startswith('0'):
            phone_number = '+98' + phone_number[1:]
        if not phone_number.startswith('+98') or len(phone_number) != 13:
            raise ValidationError('فرمت وارد شده شماره تلفن صحیح نیست!')
        return phone_number

    def to_internal_value(self, data):
        if 'birth_date' in data and isinstance(data['birth_date'], str):
            try:
                year, month, day = [int(x) for x in data['birth_date'].split('/')]
                data['birth_date'] = jdatetime.date(year, month, day).togregorian()
            except Exception as e:
                raise ValidationError({'birth_date': ['فرمت تاریخ تولد داده شده اشتباه است!']}) from None
        if 'password' in data and isinstance(data['password'], str):
            data['password'] = make_password(data['password'])
        return super().to_internal_value(data)


class LoginSerializer(serializers.Serializer):
    nationality_code = serializers.CharField()

    password = serializers.CharField()

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        raise NotImplementedError

    def validate_nationality_code(self, nationality_code):
        return unidecode(nationality_code)

    class Meta:
        model = Student
        fields = [
            'nationality_code',
            'password'
        ]


class AssistantLoginSerializer(serializers.Serializer):
    username = serializers.CharField()

    password = serializers.CharField()

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        raise NotImplementedError

    def validate_username(self, username):
        return unidecode(username)

    class Meta:
        model = Student
        fields = [
            'username',
            'password'
        ]


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = [
            'id',
            'name'
        ]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            'id',
            'name'
        ]


class StateAndCitiesSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True)

    class Meta:
        model = State
        fields = [
            'id',
            'name',
            'cities'
        ]


class StudentEditSerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'password',
            'phone_number',
            'gender',
            'birth_date',
            'school',
            'email',
            'city',
            'state',
            'profile_image'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, password):
        return make_password(password)

    def get_state(self, obj):
        return obj.city.state.id

    def validate_phone_number(self, phone_number: str):
        phone_number = unidecode(phone_number)
        if phone_number.startswith('0'):
            phone_number = '+98' + phone_number[1:]
        if not phone_number.startswith('+98') or len(phone_number) != 13:
            raise ValidationError('فرمت وارد شده شماره تلفن صحیح نیست!')
        return phone_number

    def to_internal_value(self, data):
        if 'birth_date' in data and isinstance(data['birth_date'], str):
            try:
                year, month, day = [int(x) for x in data['birth_date'].split('/')]
                data['birth_date'] = jdatetime.date(year, month, day).togregorian()
            except Exception as e:
                raise ValidationError({'birth_date': ['فرمت تاریخ تولد داده شده اشتباه است!']}) from None
        return super().to_internal_value(data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['birth_date'] = date2jalali(instance.birth_date).strftime('%Y/%m/%d')
        representation['phone_number'] = '0' + representation['phone_number'][len('+98'):]
        return representation
