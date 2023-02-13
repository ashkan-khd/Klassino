

def apply_course_discount(discount):
    p = discount.course.price
    p *= ((100 - discount.percentage)/100)
    return p


def apply_assistance_discount(discount):
    p = discount.assistance.price
    p *= ((100 - discount.percentage)/100)
    return p
