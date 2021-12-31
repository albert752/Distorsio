from .models import Bocamoll
import random


def bocamoll(request):
    return {'bocamoll': random.choice(list(Bocamoll.objects.filter(approved=True)))}
