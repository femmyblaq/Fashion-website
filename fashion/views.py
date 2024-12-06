#type - ignore
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Fashion

# Create your views here.

def fashion(request):
    myfashion = Fashion.objects.all().values()
    template = loader.get_template("all_fash.html")
    context = {
        'myfashion': myfashion
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    myfashion = Fashion.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        'myfashion': myfashion
    }
    return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())