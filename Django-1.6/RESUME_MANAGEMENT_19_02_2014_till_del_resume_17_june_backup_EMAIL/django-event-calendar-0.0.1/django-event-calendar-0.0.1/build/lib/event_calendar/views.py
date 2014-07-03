from django.views.generic import TemplateView


class EventCalendarView(TemplateView):
    template_name = 'calendar/calendar.html'