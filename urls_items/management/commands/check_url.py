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

# CURRENT_FILE_DIR = os.path.dirname(os.path.abspath(__file__))

class Command(BaseCommand):

    # @lock(os.path.join(CURRENT_FILE_DIR, os.path.basename(__file__)+".lock"))
    def handle(self, *args, **options):

        http = self.initHttpClient()

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
            else:
                self.successRequest(response, result, delay)
            
            result.save()


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