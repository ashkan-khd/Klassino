def try_assistant(user):
    try:
        return user.assistant
    except:
        return None


def try_teacher(user):
    try:
        return user.teacher
    except:
        return None


def try_student(user):
    try:
        return user.student
    except:
        return None


def concrete(user):
    return try_student(user) or try_teacher(user) or try_assistant(user)
