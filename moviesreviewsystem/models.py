from django.db import models
from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
from datetime import date


class Cinema(models.Model):
    cinema_name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    director = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    release_date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.cinema_name)


class Viewers(models.Model):
    cinema_name = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name=None, blank=True, null=True)
    viewer_name = models.TextField(max_length=100, blank=True, null=True)
    viewer_comments = models.TextField(max_length=100, blank=True, null=True)
    viewer_ratingchoices = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    viewer_rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=viewer_ratingchoices)
    #email = models.EmailField(max_length=60)
    #address = models.CharField(max_length=100)
    #zipcode = models.CharField(max_length=10)

    def __str__(self):
        return str(self.viewer_name)


class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True


class cinema_review(Review):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
