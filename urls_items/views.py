from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Url
from urls_results.models import Result
from .forms import UrlForm
from django.db.models import Q
from pprint import pprint

def store(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("urls_items:index"))
    else:
        form = UrlForm()
    return render(
        request,
        'utils/form.html',
        {
            'title': "Nouvelle url",
            'form': form,
        }
    )

def index(request):
    return render(
        request,
        "urls_items/urls_list.html",
        {
            'urls': Url.objects.all(),
        }
    )

def edit(request, url_id=None):
    current_instance = None
    if url_id:
        current_instance = Url.objects.get(
            Q(id = url_id),
            )
    form_class = UrlForm
    if request.method == 'POST':
        form = form_class(request.POST, instance = current_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("urls_items:index"))
    else:
        form = form_class(instance = current_instance)
    return render(
        request,
        'utils/form.html',
        {
            'title': "Appel",
            'form':form,
        }
    )

def show(request, url_id):
    current_instance = Url.objects.get(
        Q(id = url_id),
    )
    return render(
        request,
        "urls_items/detail.html",
        {
            'url_results': Result.objects.filter(url__pk=url_id).order_by("-id"),
            'url': current_instance,
        }
    )
