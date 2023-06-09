from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

CANCELLED = ((0, "Cancelled"), (1, "Active"))


class Event(models.Model):
    title = models.CharField(max_length=200)
    region = models.CharField(max_length=200, default='location')
    location = models.CharField(max_length=200)
    featured_image = CloudinaryField('image', default='placeholder')
    date = models.DateTimeField()
    details = models.TextField()
    organiser = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_listings")
    contact = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="contact_email")
    attending = models.ManyToManyField(
        User, related_name="event_attending", blank=True)
    listed_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=CANCELLED, default=1)

    class Meta:
        ordering = ["-listed_on"]

    def __str__(self):
        return self.title

    def number_of_attendees(self):
        return self.attending.count()
