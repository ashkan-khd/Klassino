from rest_framework import permissions

from mentoring.services import find_active_assistance_courses


class IsStudent(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            return bool(not request.user.student.is_deleted)
        except:
            return False


class PasswordIsCorrect(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            password = request.data.get('old_password', '')
            if not isinstance(password, str):
                password = password[0]
            return request.user.check_password(password)
        except:
            return False


class IsAssistant(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            return bool(not request.user.assistant.is_deleted)
        except:
            return False


class IsAssistantToStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.method == 'GET':
                student_id = request.query_params.get('student_id', '')
            elif request.method == 'DELETE':
                return True
            else:
                student_id = request.data.get('student', '')
            return find_active_assistance_courses().filter(
                assistance_package__assistant=request.user.assistant,
                student_id=student_id
            )
        except:
            return False
