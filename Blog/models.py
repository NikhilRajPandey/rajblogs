from django.db import models

class AllBlogs(models.Model):
    id = models.AutoField(primary_key=True)
    sludge = models.CharField(max_length=40)
    title = models.CharField(max_length=70)
    thumnail = models.FileField(upload_to="blog/",default="")
    category = models.CharField(max_length=25)
    content = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=15)

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=100)
    image_name = models.CharField(max_length=50)

