from django.db import models
# Game.objects.filter(type__contains='NES')
# Tools -> Run manage.py Task.. -> makemigrations/migrate

class GameType(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    type = models.ForeignKey(GameType, on_delete=models.CASCADE)
    price = models.FloatField()
    def __str__(self):
        return self.name
    # TODO: more info??


class GameImage(models.Model):
    image = models.CharField(max_length=999)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

