from django.db import models


class Articles(models.Model):
    article_name = models.CharField(max_length=50)
    article_value = models.CharField(max_length=500)
    image_name = models.CharField(max_length=30, default='img')
    new_field = models.ImageField(null=False, default=False)

    def __unicode__(self):
        return self.article_name


class Extras(models.Model):
    rel_article_name = models.CharField(max_length=50)
    image_name = models.CharField(max_length=30, default='img')

    def __unicode__(self):
        return self.rel_article_name
