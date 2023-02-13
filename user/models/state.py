from django.db import models


class State(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='نام استان'
    )

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'

    def __str__(self):
        return 'استان: ' + str(self.name)
