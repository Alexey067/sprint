from django.db import models
from mountain.status import STATUS


class Users(models.Model):
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otc = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PerevalAdded(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    beauty_title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    other_titles = models.CharField(max_length=200)
    connect = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    winter_level = models.CharField(max_length=100)
    summer_level = models.CharField(max_length=100)
    autumn_level = models.CharField(max_length=100)
    spring_level = models.CharField(max_length=100)
    coord_id = models.ForeignKey('Coords', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    date_added = models.DateTimeField(null=True)
    raw_data = models.JSONField(null=True)
    images = models.JSONField(null=True)
    status = models.CharField(choices=STATUS, max_length=20, default='new')

    def __str__(self):
        return f"{self.title} or {self.beauty_title}"

    class Meta:
        db_table = 'public.pereval_added'


class PerevalAreas(models.Model):
    id = models.AutoField(primary_key=True)
    id_parent = models.BigIntegerField()
    title = models.TextField(null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'public.pereval_areas'


class PerevalImages(models.Model):
    id = models.AutoField(primary_key=True)
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.BinaryField()

    def __str__(self):
        return f"{self.image_name}"

    class Meta:
        db_table = 'public.pereval_images'



class SprActivitiesTypes(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'public.spr_activities_types'


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return f"{self.latitude} {self.longitude} {self.height}"
