from django.db import models

# Create your models here.
from datetime import date, datetime
from django.utils.dateparse import parse_date
import re

# Create your models here.
class ShowManager(models.Manager):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    
    def show_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "El titulo debe ser mayor a 2 caracteres"
        if len(postData['tv_network']) < 3:
            errors['tv_network'] = " tv_network debe ser mayor a 2 caracteres"
        if parse_date(postData['release_date']) > date.today():
            errors['release_date'] = "Ingrese una fecha menor a hoy"
        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            errors['desc'] = "La descripcion debe contener al menos 10 cararcteres, o estar vacia "
        return errors
    
    def edit_validators(self, postData):
        errors = {}
        if len(postData['updated_title']) == 0:
            errors["updated_title"] = "No ingreso valores"
        elif len(postData['updated_title']) < 2:
            errors["updated_title"] = "Se ingresaron 2 caracteres,ingrese mas "
        if len(postData["updated_tv_network"]) < 3:
            errors["updated_tv_network"] = "Se ingresaron 2 caracteres,ingrese mas tv_network  "
        if parse_date(postData["updated_release_date"]) > date.today():
            errors["updated_release_date"] = "Cambie a una fecha anterior a hoy"
        if len(postData["updated_desc"]) > 0 and len(postData['updated_desc']) < 10:
            errors["updated_desc"] = "La descripcion debe contener al menos 10 cararcteres, o estar vacia "
        return errors
class Show(models.Model):
    title = models.CharField(max_length=255)
    tv_network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()