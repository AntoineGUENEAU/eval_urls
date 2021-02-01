import os
import datetime
import requests
import urllib.parse
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils import timezone
from requests.adapters import HTTPAdapter
from urls_items.models import Url
from urls_results.models import Result
from django.core.mail import send_mail

class UrlScan():

    def handle(self):

        http = self.initHttpClient()

        error_urls = []

        for url in Url.objects.all():

            urlFormated = self.formatUrl(url.url)

            result = Result()
            result.date = timezone.now()
            result.url = url

            try:
                start = datetime.datetime.now()
                response = http.get(urlFormated)
                end = datetime.datetime.now()
                # delay = end - start
                delay = 'TODO'
            except Exception as err:
                result.success = False
                print("Url invalide : %s" % err)
                error_urls.append(urlFormated)
            else:
                self.successRequest(response, result, delay)
            
            result.save()
      
        self.sendMail( error_urls )

    def formatUrl(self, url):
        print("Check url  : " + str(url))
        if not self.checkUrlContainPrefixHttp(url):
            url = self.addPrefixHttp(url)

        print("Check url(formated) : " + str(url))
        return url
    
    def checkUrlContainPrefixHttp(self, url):
        return url.startswith("http://") or url.startswith("https://")

    def addPrefixHttp(self ,url):
        return "http://" + url

    def initHttpClient(self):
        adapter = HTTPAdapter(max_retries=5)
        http = requests.Session()
        http.mount("https://", adapter)
        http.mount("http://", adapter)
        return http

    def successRequest(self, response, result, delay):
        result.success = True
        result.http_code = self.check_http_code(response, result)
        result.has_text = self.check_has_text(response, result)
        result.answer_delay = delay
        result.ssl_certificat_validation = self.check_ssl_certificat_validation(response, result)
        result.ssl_delay_before = self.check_ssl_delay_before(response, result)
        return result

    def check_http_code(self, response, result):
        return int(response.status_code)

    def check_has_text(self, response, result):
        return response.content != ''

    # TODO
    def check_ssl_certificat_validation(self, response, result):
        return 

    # TODO
    def check_ssl_delay_before(self, esponse, result):
        return 

    def sendMail(self, error_urls):
        try:
           send_mail(
            'Url en erreurs',
            self.formatMailContent(error_urls),
            settings.EMAIL_FROM_ERRORS,
            [settings.EMAIL_DEST_ERRORS],
        )
        except Exception as err:
            return

    def formatMailContent(self, error_urls):
        content = '<h1>Voici la liste des ursl en erreur</h1>'
        content += '<ul>'
        for error_url in error_urls :
            content += '<li>' + error_url +'<li>'

        content += '</ul>'
        return content