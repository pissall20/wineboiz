from django.db import models
import numpy as np
from django.contrib.auth.models import User

# Create your models here.


class Wine(models.Model):
    name = models.CharField(max_length=200)

    def average_rating(self):
        all_ratings = list(map(lambda x: x.rating, self.review_set.all()))
        return int(np.mean(all_ratings))

    def __unicode__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"))

    wine = models.ForeignKey(Wine)
    pub_date = models.DateTimeField("date_published")
    user_name = models.CharField(max_length=100)
    comments = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)


class Cluster(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def get_members(self):
        return "\n".join([u.username for u in self.users.all()])
