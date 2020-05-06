from IPython.testing.tools import full_path
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import  RichTextUploadingField
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


class Category(MPTTModel):
    STATUS = (
        ("True", "Evet"),
        ("False","Hayır"),
    )
    title = models.CharField(blank=True,max_length=30)
    keywords = models.CharField(blank=True,max_length=255)
    description = models.CharField(blank=True,max_length=255)
    image = models.ImageField(blank=True,upload_to="images/")
    status = models.CharField(blank=True,max_length=10,choices=STATUS)
    slug = models.SlugField()
    parent = TreeForeignKey("self",blank=True,null=True,related_name="children",on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        #level_attr = 'mptt_level'
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '->'.join(full_path[::-1])


    def image_tag(self):
       return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = "Image"


class Cars(models.Model):
    STATUS = (
        ("True", "Evet"),
        ("False","Hayır"),
    )
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    keywords = models.CharField(blank=True,max_length=255)
    description = models.CharField(blank=True,max_length=255)
    slug = models.SlugField()
    image = models.ImageField(blank=True,upload_to="images/")
    price = models.FloatField()
    amount = models.IntegerField()
    detail = RichTextUploadingField(blank=True)
    status = models.CharField(blank=True,max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = "Image"



class Images(models.Model):
    car = models.ForeignKey(Cars,on_delete=models.CASCADE)
    title = models.CharField(max_length=30,blank=True)
    image = models.ImageField(blank=True, upload_to="images/")

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = "Image"