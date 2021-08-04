from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date

class highflow(models.Model):
    FolderNo = models.PositiveIntegerField(primary_key=True, null=False, unique=True, verbose_name='Folder No')
    Name = models.CharField(null=False, max_length=50)
    Age = models.PositiveIntegerField(null=False, validators=[MinValueValidator(10),MaxValueValidator(75)])
    Background = models.TextField(blank=True, max_length=255)
    PriorityScore = models.PositiveIntegerField(null=False, default=1, verbose_name='Priority Score')
    PriorityScoreDate = models.DateField(null=False, verbose_name='Priority Score Date')
    UpdatedPriority = models.PositiveIntegerField(null=True, blank=True, verbose_name='Updated Priority Score')
    UpdatedPriorityDate = models.DateField(null=True, blank=True, verbose_name='Updated Date')
    HFStart = models.DateField(null=False, verbose_name='Date Starting High Flow')
    Archive = models.BooleanField(default=False)

    def get_sats(self):
        return self.sats_set.all()

    def get_days_hfno2(self):
        #print(date.today())
        #print(self.HFStart)
        #print(date.today() - self.HFStart)

        return (date.today() - self.HFStart).days

    def get_latest_sats(self):
        return self.sats_set.all().order_by('-Date')

    def __str__(self):
        return self.Name+" "+self.FolderNo

class sats(models.Model):
    Patient = models.ForeignKey(highflow, on_delete=models.CASCADE)
    Date = models.DateField(null=False)
    RespRate = models.PositiveIntegerField(null=False, verbose_name='Resp Rate', validators=[MinValueValidator(10),MaxValueValidator(60)])
    HeartRate = models.PositiveIntegerField(null=False, verbose_name='Heart Rate', validators=[MinValueValidator(40),MaxValueValidator(200)])
    Sats = models.PositiveIntegerField(null=False, default=90, validators=[MinValueValidator(40),MaxValueValidator(100)])
    FiO2 = models.PositiveIntegerField(null=False, default=21, validators=[MinValueValidator(21),MaxValueValidator(100)])
    Litres = models.PositiveIntegerField(null=False, default=10, validators=[MinValueValidator(25),MaxValueValidator(60)])

#    def __str__(self):
#        return self.patient+" "+self.date+" "+self.sats