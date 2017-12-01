import datetime

from django.core.management.base import BaseCommand, CommandError
from address.models import Coordinate




class Command(BaseCommand):
    help = 'Reminds his/her job has crossed the deadline'

    # def add_arguments(self, parser):
    #     parser.add_argument('job_id', nargs='+', type=int)

    def handle(self, *args, **options):
        older_datas = Coordinate.objects.filter(created_at__lt=datetime.datetime.now() - datetime.timedelta(1))
        older_datas.delete()
        self.stdout.write(self.style.SUCCESS('Success'))
