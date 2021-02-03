from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Url
from urls_results.models import Result
from .forms import UrlForm
from django.db.models import Q
from urls_items.services.urls_scan import UrlScan
from django.core.paginator import Paginator
from django.contrib import messages

def store(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Url créée avec succès')
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
            messages.add_message(request, messages.SUCCESS, 'Url modifiée avec succès')
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
    results = Result.objects.filter(url__pk=url_id).order_by("-id")
    paginator = Paginator(results, 3)
    page_number = request.GET.get('page')
    url_results = paginator.get_page(page_number)
    return render(
        request,
        "urls_items/detail.html",
        {
            'url_results': url_results,
            'url': current_instance,
        }
    )

def handle_scan(request):
    service = UrlScan()
    service.handle()
    messages.add_message(request, messages.SUCCESS, 'Scan achevé avec succès')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))