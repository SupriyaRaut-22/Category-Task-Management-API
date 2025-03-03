from django.db import models

STATUS_CHOICES=[
    ('unavailable','Unavailable'),
    ('available','Available')
]

class Task1(models.Model):
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    availability = models.CharField(max_length=15,choices=STATUS_CHOICES,default='unavailable')

    def __str__(self):
        return self.name
    

