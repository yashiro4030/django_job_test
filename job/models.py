from typing import Tuple
from django.db import models

class Category(models.Model):
    cat_title = models.CharField(max_length=100,null=True)
    publish_at=models.DateField(null=True,auto_now=True)

    def __str__(self) -> str:
        return self.cat_title

class Job(models.Model):
    JOB_TYPE=(("FULL TIME","FULL TIME"),("PART TIME","PART TIME"))
    title = models.CharField(max_length=100,null=True)
    descript=models.TextField(max_length=500,null=True)
    location = models.CharField(max_length=100,null=True)
    job_type=  models.CharField(max_length=100,choices=JOB_TYPE)
    publish_at=models.DateField(null=True,auto_now=True)
    vacancy = models.IntegerField(null=True)
    salary = models.FloatField(null=True)
    experience = models.IntegerField(null=True)
    Category = models.ForeignKey('category',null=True,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    