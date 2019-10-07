from django.db import models

# Create your models here.


class Search(models.Model):

    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.search)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Search'
        verbose_name_plural = 'Searches'
