from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', related_name='blogs', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    commented = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    author = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    blog = models.ForeignKey('Blog', related_name='comments', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['commented']