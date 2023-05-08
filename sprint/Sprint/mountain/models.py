from django.db import models


class PerevalAdded(models.Model):
    id = models.AutoField(primary_key=True)
    date_added = models.DateTimeField(null=True)
    raw_data = models.JSONField(null=True)
    images = models.JSONField(null=True)
    status = models.CharField(max_length=20, default='new')

    class Meta:
        db_table = 'public.pereval_added'


class PerevalAreas(models.Model):
    id = models.AutoField(primary_key=True)
    id_parent = models.BigIntegerField()
    title = models.TextField(null=True)

    class Meta:
        db_table = 'public.pereval_areas'


class PerevalImages(models.Model):
    id = models.AutoField(primary_key=True)
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.BinaryField()

    class Meta:
        db_table = 'public.pereval_images'


class SprActivitiesTypes(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(null=True)

    class Meta:
        db_table = 'public.spr_activities_types'