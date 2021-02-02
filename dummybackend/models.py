from django.db import models

# Create your models here.
class lists(models.Model):
    Listname=models.CharField(max_length=500)
    Listdescription = models.TextField()
    columns=models.TextField()

    def __str__(self):
        return (self.Listname)

class data(models.Model):
    row_id = models.IntegerField(null=True)
    column = models.CharField(max_length=500)
    value = models.TextField()
    list_id = models.IntegerField(null=True)

    def __str__(self):
        return (self.row_id)