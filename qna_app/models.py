from django.db import models

# Create your models here.
#models creates database automatically (ORM(OBJECT RELATION MODEL) CONCEPT)

class CategoryModel(models.Model):
    cat_title = models.CharField(max_length=120)
    cat_desc = models.TextField()
    def __str__(self):
        return(self.cat_title) #shows the title in the website


class QuestionModel(models.Model):
    #id is made by django automatically (built-in)
    title = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    question_desc = models.TextField()
    qn_img = models.ImageField(upload_to='QuestionImg', blank= True, null=True)
    qn_votes= models.IntegerField(default=0)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return(self.question_desc) #shows question description
        


class AnswerModel(models.Model):
    answered_by = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    answer_desc = models.TextField()
    answer_img = models.ImageField(upload_to='AnswerImg',blank=True, null=True)
    answer_votes = models.IntegerField(default=0)
    is_accept = models.BooleanField(default=0)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)

    def __str__(self):
        return(self.answer_desc)

