from django.db import models
from django.urls import reverse


class Hardware(models.Model):
    title = models.CharField(max_length=250)
    assignment = models.CharField(max_length=250)
    is_router = models.BooleanField(default=False)
    ip_address = models.CharField(max_length=15)
    content = models.TextField(blank=True)
    Location = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="photos")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    filial = models.ForeignKey('Filial', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id', self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Filial(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    location = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name
