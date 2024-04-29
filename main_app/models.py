from django.db import models
from django.urls import reverse

class Game(models.Model):
    api_id = models.CharField()
    name = models.CharField()
    summary = models.TextField()

class UserGame(models.Model):
    RATING_OPTIONS = [(str(i), str(i)) for i in range(6)]
    STATUS_OPTIONS = (
        ('1', 'Not started'),
        ('2', 'In progress'),
        ('3', 'Finished'),
        ('4', 'Dropped'),
        ('5', 'Taking a break'),
        ('6', 'Playing again!'),
    )

    api_id = models.CharField()
    name = models.CharField()
    summary = models.TextField()
    rating = models.CharField(choices=RATING_OPTIONS, null=True, blank=True)
    status = models.CharField(choices=STATUS_OPTIONS, default='1')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})