from .models import SettingSite


def settings(request):
    setting = SettingSite.objects.first()

    return {"setting":setting}