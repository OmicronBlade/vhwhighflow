from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from datetime import datetime

class highflow(models.Model):
    FolderNo = models.PositiveIntegerField(primary_key=True, null=False, unique=True)
    Name = models.CharField(null=False, max_length=50)
    Age = models.PositiveIntegerField(null=False, validators=[MinValueValidator(10),MaxValueValidator(75)])
    RedScore = models.PositiveIntegerField(null=False, default=1)
    Archive = models.BooleanField(default=False)

    def get_sats(self):
        return self.sats_set.all()

    def get_latest_sats(self):
        return self.sats_set.all().order_by('-Date')

    def __str__(self):
        return self.Name+" "+self.FolderNo

class sats(models.Model):
    Patient = models.ForeignKey(highflow, on_delete=models.CASCADE)
    Date = models.DateField(null=True)
    Sats = models.PositiveIntegerField(null=False, validators=[MinValueValidator(40),MaxValueValidator(100)])

#    def __str__(self):
#        return self.patient+" "+self.date+" "+self.sats