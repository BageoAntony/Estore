from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models import Count

class Questions(models.Model):
    question=models.CharField(max_length=500)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    create_date=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    @property
    def fetch_answers(self):
        answers=self.answers_set.all().annotate(up_count=Count('up_vote')).order_by('-up_count')
        return answers

    def _str_(self):
        return self.question


class Answers(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=500)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    create_date=models.DateField(auto_now_add=True)
    up_vote=models.ManyToManyField(User,related_name="upvotes")

    @property
    def up_vote_count(self):
        return self.up_vote.all().count()
    
    def _str_(self):
        return self.answer





# class Upvotes(models.Model):
#     user=models.ForeignKey(User)
#     answer=models.ForeignKey(Answers)