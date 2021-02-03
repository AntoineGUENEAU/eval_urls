from django.views.generic import DeleteView
from django import http
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse
from .models import Url
from django.contrib import messages

class UrlDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'utils/delete.html'
    model = Url

    def test_func(self):
        self.object = self.get_object()
        return True
        
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.add_message(request, messages.SUCCESS, 'Url supprimée avec succès')
        return http.HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse("urls_items:index")