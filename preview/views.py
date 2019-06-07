from django.shortcuts import render_to_response


# Create your views here.
from django.template import context


def home(request):
    return render_to_response("index.html", context={ 'site_name': 'asd'})

