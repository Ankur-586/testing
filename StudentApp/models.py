from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.conf import settings
from datetime import date

class CustomUser(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    email = models.EmailField(_('email address'), unique = True)
    # native_name = models.CharField(max_length = 5)
    # phone_no = models.CharField(max_length = 10)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    def __str__(self):
        return "{}".format(self.first_name.capitalize() + ' ' + self.last_name.capitalize())

class Subject(models.Model):
    subj_id = models.AutoField(primary_key=True)
    Subject_name = models.CharField(max_length=200)

    def __str__(self):
        return self.Subject_name

class Student(models.Model):
    stud = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, null=True, blank=False)
    marks = models.IntegerField()

    def __str__(self):
        return self.stud.first_name + ", " + self.stud.last_name


# class combined(models.Model):
#     student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     marks = models.IntegerField()

        
# stuenv\scripts\activate 
# python manage.py runserver 
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser

# {% if perms.StudentApp(appname).delete(this is method) Post,put etc)_modelname %}