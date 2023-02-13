from konkour.models import Konkour


def get_closest_ahead_konkour(date):
    konkours = Konkour.objects.filter(date__gte=date).order_by('date')
    return konkours.first()
