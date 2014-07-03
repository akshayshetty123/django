from django.conf.urls import patterns, url
from piston.resource import Resource
from event_calendar.handlers import EventMonthHandler, EventDayHandler
from event_calendar.views import EventCalendarView


event_month_resource = Resource(handler=EventMonthHandler)
event_day_resource = Resource(handler=EventDayHandler)

urlpatterns = patterns('event_calendar.views',
    url(r'^$', EventCalendarView.as_view(), name='calendar_home'),
    url(r'events/(?P<year>\d{4})/(?P<month>\d{1,2})/$', event_month_resource),
    url(r'events/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', event_day_resource),
)