from django.db import models


class CalendarEvent(models.Model):
    title = models.CharField(max_length=255)
    scheduled_on = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)