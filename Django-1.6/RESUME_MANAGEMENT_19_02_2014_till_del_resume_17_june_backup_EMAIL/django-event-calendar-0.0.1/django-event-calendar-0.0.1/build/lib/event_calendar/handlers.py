from django.db.models import Count
from models import CalendarEvent
from piston.handler import BaseHandler


class EventMonthHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request, year, month):
        events = CalendarEvent.objects.extra({'scheduled_date': "date(scheduled_on)"}).filter(
            scheduled_on__year=year,
            scheduled_on__month=month
        ).values('scheduled_date').annotate(count=Count('id'))

        return events


class EventDayHandler(BaseHandler):
    allowed_methods = ('GET',)

    def read(self, request, year, month, day):
        events = CalendarEvent.objects.filter(
            scheduled_on__year=year,
            scheduled_on__month=month,
            scheduled_on__day=day,
        )

        return events