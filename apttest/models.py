from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
#from dateutil.relativedelta import relativedelta
from datetime import date

SEX_CHOICES = (
    ('male', '男'),
    ('female', '女'),
);

class Result(models.Model):
    name = models.CharField(max_length=20, null=True);
    sex = models.CharField(max_length=10, null=True);
    email = models.CharField(max_length=50, null=True);
    #tester = models.ForeignKey(User, on_delete=models.PROTECT);
    age = models.DecimalField(max_digits=2,decimal_places=0, null=True);
    answer = models.CharField(max_length=80, null=True);
    person_type = models.CharField(max_length=10, null=True);
    work_exp = models.BooleanField(default=False);
    submitted_date = models.DateTimeField(blank=True, null=True);

    def submit(self):
        self.submitted_date = timezone.now();
        self.save();

    def __str__(self):
        return self.name;
'''
    @property
    def get_age(self):
        return relativedelta(self.birth_date.days, datetime.date.now()).years;

'''
