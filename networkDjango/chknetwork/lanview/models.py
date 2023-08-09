from django.db import models


class Hardware(models.Model):
    title = models.CharField(max_length=250)
    assignment = models.CharField(max_length=250)
    is_router = models.BooleanField(default=False)
    ip_address = models.CharField(max_length=15)
    content = models.TextField(blank=True)
    Location = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="photos")

    def __str__(self):
        return self.title
