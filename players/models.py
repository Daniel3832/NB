from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    career_history = models.CharField(max_length=200)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Team(models.Model):
    team_name = models.CharField(max_length=200)
    founded = models.IntegerField(default=0)
    location = models.CharField(max_length=200)


class Game(models.Model):
    game_name= models.CharField(max_length=200)
    mvp = models.CharField(max_length=200)









