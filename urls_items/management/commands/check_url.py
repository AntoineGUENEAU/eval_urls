from django.core.management.base import BaseCommand
from urls_items.services.urls_scan import UrlScan

class Command(BaseCommand):

    def handle(self, *args, **options):
        service = UrlScan()
        service.handle()