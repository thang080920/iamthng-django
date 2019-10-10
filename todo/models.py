from django.db import models

# Create your models here


class todo(models.Model):

    created = models.DateTimeField(auto_now=True)

    text = models.CharField(max_length=200)

    active = models.IntegerField(default=1)

    def __str__(self):
        return self.text

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'todo'
        verbose_name_plural = 'todoes'
