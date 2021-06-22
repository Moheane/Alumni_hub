from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.
class jobModel(models.Model):
    Tittle = models.CharField(max_length=100)
    Description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    closing_date = models.DateTimeField(default=timezone.now)
 #   category = models.Choices('IT','HR')
#    experience_level = models.Choices('Student','Young Proffesioonal','Experienced Proffesioonal')
    
    def __str__(self):
        return self.Tittle