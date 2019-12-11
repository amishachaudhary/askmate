from django.db import models

# Create your models here.
#models creates database automatically (ORM(OBJECT RELATION MODEL) CONCEPT)

class QuestionModel(models.Model):
    #id is made by django automatically (built-in)
    title = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    question_desc = models.TextField()
    qn_img = models.ImageField(upload_to='QuestionImg')


class AnswerModel(models.Model):
    answered_by = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    answer_desc = models.TextField()
    answer_img = models.ImageField(upload_to='AnswerImg')
    votes = models.IntegerField()
    is_accept = models.BooleanField()
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)


