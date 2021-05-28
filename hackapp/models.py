from django.db import models
import uuid

# Create your models here.

class Employee(models.Model) :
    name = models.CharField(max_length = 100, null = True)
    OpCo = models.CharField(max_length = 300, null = True)
    EntEmail = models.EmailField(max_length = 300, null = True)
    password = models.CharField(max_length = 20, null = True)

    def __str__(self):
        return self.name

class Lead(models.Model):
    STATUS = (
        ('OPEN' , 'OPEN'), 
        ('CLOSED', 'CLOSED'),
        ('VALIDATED', 'VALIDATED'),
        ('REJECTED', 'REJECTED'),
    )
    leadid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 100, null = True)
    project = models.CharField(max_length = 500, null = True)
    segment = models.CharField(max_length = 100, null = True)
    submitted_by = models.CharField(max_length = 100 , null = True)
    submitted_to = models.CharField(max_length = 100, null = True)
    status = models.CharField(max_length = 100, null = True, choices = STATUS, default = 'OPEN')
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.name

