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
            times_in_hour = int(60 / interval)
            hour = 0
            for i in range(24*times_in_hour):
                minute = 0
                for _ in range(times_in_hour):
                    try:
                        time = AppointmentTime(start_time=datetime.time(hour, minute, 00), code=str(interval))
                        time.save()
                    except IntegrityError:
                        pass
                    minute += interval
                hour += 1
                if hour == 24:
                    break