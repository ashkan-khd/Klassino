from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from teaching.models import Subject, Course, CourseSession, CourseSubscription

admin.site.register(Subject)


class CourseInline(ModelAdminJalaliMixin, admin.StackedInline):
    model = CourseSession
    extra = 0


@admin.register(Course)
class CourseAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    inlines = [CourseInline]


@admin.register(CourseSession)
class CourseSessionAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    pass


@admin.register(CourseSubscription)
class CourseSubscriptionAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    pass
