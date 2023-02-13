from django.contrib import admin

from jalali_date.admin import ModelAdminJalaliMixin

from mentoring.models import AssistanceCourse, AssistancePackage

admin.site.register(AssistancePackage)


@admin.register(AssistanceCourse)
class AssistanceCourseAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    pass
