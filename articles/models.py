from django.db import models

class Articles(models.Model):
    tittle = models.CharField(max_length=40)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.tittle
    def snippet(self):
        return self.body[:10]+" ..."
