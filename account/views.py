from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from account.models import Data, Photo


def index(request):
    if request.method == "POST":
        form = Data()
        form.name = request.POST["name"]
        form.text = request.POST["text"]
        form.pub_date = timezone.datetime.now()
        form.save()
        for img in request.FILES.getlist('images'):
            photo = Photo()
            photo.data = form
            photo.image = img
            photo.save()
        return redirect('show/' + str(form.id), form.id)
    else:
        return render(request, 'index.html')


def show(request, form_id):
    lst = get_object_or_404(Data, pk=form_id)
    return render(request, 'show.html', {'lst': lst})
