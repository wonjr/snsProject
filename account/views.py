from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from account.models import Data


def index(request):
        if request.method == "POST":
                name = request.POST.get('name')
                text = request.POST.get('text')
                form = Data()
                form.name = name
                form.text = text
                form.save()
                lst = Data.objects.all()
                return HttpResponseRedirect(reverse('index'))
        else:
                lst = Data.objects.all()
                return render(request, 'index.html')
def show(request):
        lst = Data.objects.all()
        return render(request, 'show.html',{'lst':lst})
