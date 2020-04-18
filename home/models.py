from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
class Setting(models.Model):
    STATUS = (
        ("True", "Evet"),
        ("False", "Hayır"),
    )
    title = models.CharField(blank=True,max_length=30)
    keywords = models.CharField(blank=True,max_length=255)
    description = models.CharField(blank=True,max_length=255)
    company = models.CharField(blank=True,max_length=30)
    adress = models.CharField(blank=True,max_length=255)
    phone = models.CharField(blank=True,max_length=255)
    fax = models.CharField(blank=True,max_length=30)
    email = models.CharField(blank=True,max_length=255)
    smtpserver = models.CharField(blank=True,max_length=20)
    smtpemail = models.CharField(blank=True,max_length=20)
    smtppassword = models.CharField(blank=True,max_length=20)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True,upload_to="images/")
    facebook = models.CharField(blank=True,max_length=255)
    instagram = models.CharField(blank=True,max_length=255)
    twitter = models.CharField(blank=True,max_length=255)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
