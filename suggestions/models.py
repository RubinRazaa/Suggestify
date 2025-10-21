from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Suggestion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    
        
     
        
class Comment(models.Model):
    suggestion = models.ForeignKey(Suggestion, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    upvote = models.ManyToManyField(User, related_name='upvote_comment', blank=True)

    
    def __str__(self):
        return f'{self.author.username} on {self.suggestion.title}'
    
    def total_upvotes(self):
        return self.upvote.count()
    
