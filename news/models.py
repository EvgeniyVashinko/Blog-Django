from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:post-detail-page', kwargs={'pk' : self.pk})

    def was_published_recently(self):
        return self.date_posted >= (timezone.now() - datetime.timedelta(days=7))

    #
    # class Meta:
    #     verbose_name='Статья'
    #     verbose_name_plural='Статьи'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора', max_length=50)
    comment_text = models.CharField('текст комментария', max_length=350)

    def __str__(self):
        return self.author_name

    def get_writer(self):
        return User.objects.get(username=self.author_name)


    #
    # class Meta:
    #     verbose_name='Комментарий'
    #     verbose_name_plural='Комментарии'


# class UserData(models.Model):
#     # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     login = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)
#
#     class Meta:
#         verbose_name='Данные'
#         verbose_name_plural='Данные'
