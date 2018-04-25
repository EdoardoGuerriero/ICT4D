from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

       
class Farmer(models.Model):
    farmer_name = models.CharField("Farmer's name", max_length=50)
    number_animal_owned = models.IntegerField()
    last_request_date = models.DateTimeField('Last request')
    
    def __str__(self):
       return self.name
    
class Animal(models.Model):
    species = models.CharField("Aminal's fspecies", max_length = 15)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    time_since_request = models.DurationField()
    symptom = models.CharField("Symptom description", max_length=200)
    first_day_sickness = models.DateTimeField('Time passed from last request')
    
    
    def __str__(self):
       return self.symptom