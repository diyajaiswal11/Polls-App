from django.db import models
from datetime import datetime
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    
    #def __str__(self):
    #   return self.question_text

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    #if que deleted ,choices also deleted....Foreign Key is a link to another models
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0) 

    #def __str__(self):
    #   return self.choice_text
 




"""You created a foreign key on Choice which relates each one to a Question.
So, each Choice explicitly has a question field, which you declared in the model.
Django's ORM follows the relationship backwards from Question too, automatically generating a field on each instance called foo_set where Foo is the model with a ForeignKey field to that model.
choice_set is a RelatedManager which can create querysets of Choice objects which relate to the Question instance, e.g. q.choice_set.all()
 """