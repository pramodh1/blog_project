from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# model for Blog : Insert blog in database like this
class Blog(models.Model):

    category_choices = (
      ('Python','Python'),
      ('Django','Django'),
      ('Web_Development','Web_Development'),
      ('Data_Science','Data_Science'),
      ('Machine_Learning','Machine_Learning'),
      ('Cloud_Computing','Cloud_Computing'),
      ('Cyber_Security','Cyber_Security'),
      ('Tools','Tools'),
      ('Other','Other'),
   )

    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(choices=category_choices, max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    description = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
       return self.title





