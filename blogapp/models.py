from django.db import models
import django.utils.timezone as timezone


class UserBlog(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    pwd = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'User blog'
        verbose_name_plural = 'User blogs'


class Blog(models.Model):
    content = models.CharField(max_length=1000)
    time = models.DateTimeField(default=timezone.now)
    # userblogid = models.ForeignKey(UserBlog,on_delete=models.CASCADE)
    userid = models.ForeignKey(UserBlog, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'


class Comment(models.Model):
    content = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.now)
    blogid = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)





