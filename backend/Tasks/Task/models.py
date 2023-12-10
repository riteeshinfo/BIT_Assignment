from django.db import models

# Create your models here.
class ListModel(models.Model):
    Title=models.CharField(max_length=100)
    Description=models.TextField(max_length=100)
    Due_Date=models.DateField(max_length=100)
    Status=models.IntegerField(choices=((1, ("Pending")),
                                        (2, ("In Progress")),
                                        (3, ("Completed"))),default=1)