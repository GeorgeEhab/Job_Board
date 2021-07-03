from django.db import models
from django.utils.text import slugify

# Create your models here.
# Created By Me
'''
django model field :
    - HTML widght
    - Validation
    - DB size 
'''

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)

def image_upload(instance,filename):
    imagename ,extention = filename.split('.')
    return "Jobs Images/%s.%s"%(instance.id,extention)

class Job(models.Model) : # create table
    title = models.CharField(max_length=100) # column
    #location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1) # No of Position
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to = image_upload)
    
    slug = models.SlugField(blank = True , null = True)


    def save(self,*args,**kwargs):
        # Logic
        self.slug = slugify(self.title)  # slugify() to remove spaces from title
    
        # Overwrite
        super(Job,self).save(*args,**kwargs)

    def __str__(self):
        return self.title


#category
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

