from django.shortcuts import render
from urls_results.models import Result
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def delete(request, result_id):
    Result.objects.get(
        Q(id = result_id),
    ).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))