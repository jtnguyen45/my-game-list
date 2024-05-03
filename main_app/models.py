from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Game(models.Model):
    api_id = models.CharField()
    name = models.CharField()
    summary = models.TextField()
    cover = models.TextField(default='https://i.pinimg.com/736x/64/9d/37/649d37014bd486376f3f8552a1f049d8.jpg')

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
    cover = models.TextField(default='https://i.pinimg.com/736x/64/9d/37/649d37014bd486376f3f8552a1f049d8.jpg')
    rating = models.CharField(choices=RATING_OPTIONS, null=True, blank=True)
    status = models.CharField(choices=STATUS_OPTIONS, default='1')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})
    
class Note(models.Model):
    title = models.CharField(max_length=100)
    note = models.TextField(max_length=350)
    date = models.DateField('note date')
    user_game = models.ForeignKey(UserGame, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} on {self.date}'
    
    class Meta:
        ordering = ['date']

class Photo(models.Model):
    url = models.CharField(max_length=100)
    user_game = models.ForeignKey(UserGame, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for user_game: {self.user_game.name}'