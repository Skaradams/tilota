from django.db import models
from django.contrib.auth.models import User
from tilota.core import utils

__all__ = ('GameInfo', 'Game', 'GameHistory')


class GameInfo(models.Model):
    name = models.CharField(max_length=32)
    cmd = models.CharField(max_length=32)


class Game(models.Model):
    user = models.ForeignKey(User)
    dmtcp_id = models.CharField(max_length=32, default=None)
    info = models.ForeignKey(GameInfo)

    def save(self):
        if not self.dmtcp_id:
            self.dmtcp_id = utils.create_game(self.info.cmd)
        super(Game, self).save()


class GameHistory(models.Model):
    game = models.ForeignKey(Game)
    request = models.CharField(max_length=256)
    text = models.CharField(max_length=256)

    def save(self):
        self.text = utils.play(self.game.dmtcp_id, self.request)
        super(Game, self).save()
