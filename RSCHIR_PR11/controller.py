import io
import os

import matplotlib
import matplotlib.pyplot as plt
import requests
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from RSCHIR_PR11.models import Analytics


def hello(request: WSGIRequest):
    name = request.GET.get("name", "World")

    return HttpResponse(f"Hello {name}!")


@csrf_exempt
def diagram(request: WSGIRequest):
    body = requests.get(f"{os.environ.get('HISTORY_HOST', 'http://localhost:8080/history')}").json()

    statuses = [event["status"] for event in body]
    successes = statuses.count("SUCCESS")
    cancels = statuses.count("CANCELED")

    statuses = ["SUCCESS", "CANCELED"]
    data = [successes, cancels]

    matplotlib.use('Agg')

    plt.pie(data, labels=statuses)

    plt.title('Order statuses')

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")

    new_entity = Analytics(image=buffer.getvalue())
    new_entity.save()

    return HttpResponse(buffer.getvalue(), content_type="image/png")
