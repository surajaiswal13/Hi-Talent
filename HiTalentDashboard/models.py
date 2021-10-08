from django.db import models

# Create your models here.

class candidate(models.Model):

    fresher = 'fresher'
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    fiveplus = '5+'

    Experirnce_choices = [
        ('fresher',fresher),
        ('1',one),
        ('2',two),
        ('3',three),
        ('4',four),
        ('5',five),
        ('5+',fiveplus)
    ]

    # candidate_id = models.IntegerField(unique=True, primary_key=True, blank=False)
    candidate_name = models.CharField(max_length=256, blank=False)
    candidate_experience = models.CharField(max_length=7, choices=Experirnce_choices, default=fresher)  ## testby changeing max_length
    candidate_tech_stack = models.TextField(default='')
    candidate_placed = models.BooleanField()

    def __str__(self,*args,**kwargs):
        return self.candidate_name