import datetime

from django.core.management import BaseCommand
from django.db.utils import IntegrityError

from apps.clinics.models import AppointmentTime, DurationChoices


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):

        intervals = DurationChoices.values
        for interval in intervals:
            interval = int(interval)
            start_time = datetime.timedelta(minutes=0)
            for i in range(int(24 * 60 / interval)):
                try:
                    null_datetime = datetime.datetime(2022, 1, 1, 00, 00, 00, 0)
                    time = AppointmentTime(start_time=(null_datetime + start_time).time(), code=str(interval))
                    time.save()
                except IntegrityError:
                    pass
                start_time += datetime.timedelta(minutes=interval)
