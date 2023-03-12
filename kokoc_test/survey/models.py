from django.db import models

class Poll(models.Model):
    name = models.CharField()
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField()
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text
