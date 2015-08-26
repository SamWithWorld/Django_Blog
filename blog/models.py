from django.db import models
from django.utils import timezone
from django.contrib.auth.models import  User

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)


    class Meta:
        verbose_name = 'word'
        verbose_name_plural = 'word'


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

class  Comment(models.Model):
    author = models.CharField(max_length=20)
    email = models.EmailField()
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    post = models.ForeignKey(Post)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comment'

    def __unicode__(self):
        return  '{0}:{1}'.format(self.author,self.post.title)



