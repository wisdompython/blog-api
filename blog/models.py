from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from users.models import *
from django.db.models import Avg
from django.utils.text import slugify
from autoslug import AutoSlugField
# Create your models here.


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField(blank=True, default='null')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    new_file = models.CharField(null=True, max_length=50)
    slug = AutoSlugField(populate_from='title',unique_with='created_on', always_update=True)
    post_image = models.CharField(max_length=250, default="https://th.bing.com/th/id/R.78aab76606113ad8d781df4cfdfe4787?rik=g34KT78av2NJgg&pid=ImgRaw&r=0")
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    # def __str__(self):
    #     return self.slug

    # @property
    # def total_rating(self):
    #     return Rating.objects.filter(post=self).aggregate(Avg('ratings'))['ratings__avg']
    

    class Meta:
        ordering = ['-created_on']

class Comment(models.Model):
    username = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    comment_body = models.TextField(blank=False)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    email = models.EmailField(default='null')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created']

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.CharField(max_length=200)
    #post = models.ManyToManyField('Post', related_name='categories', blank=True)

    def __str__(self):
        return self.name




    class Meta:
        verbose_name_plural = 'categories'

class Rating(models.Model):
    post = models.ForeignKey('Post',  related_name='ratings',on_delete=models.CASCADE)
    rating_owner = models.CharField(max_length=200)
    ratings = models.PositiveIntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(5)])
    #ratings = models.PositiveIntegerField()




    class Meta:
        verbose_name_plural = 'ratings'


class Postviewed(models.Model):
    post = models.ForeignKey('Post', related_name='postviewed',on_delete=models.CASCADE)
    #content_views = models.PositiveIntegerField(default=0)
    date_viewed = models.DateTimeField(auto_now= True)






