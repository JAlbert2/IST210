from django.db import models

# Create your models here.


class Patient(models.Model):
    user = models.CharField(max_length=200)
    creation = models.DateTimeField('creation')
    age = models.IntegerField()
    covid = models.BooleanField()
    UID = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.user) + ': ' + str(self.UID)
