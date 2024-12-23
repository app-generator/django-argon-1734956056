# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    idusuario = models.IntegerField(null=True, blank=True)
    nombre = models.TextField(max_length=255, null=True, blank=True)
    clave = models.TextField(max_length=255, null=True, blank=True)
    tipousuario = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Vendedor(models.Model):

    #__Vendedor_FIELDS__
    idvendedor = models.IntegerField(null=True, blank=True)

    #__Vendedor_FIELDS__END

    class Meta:
        verbose_name        = _("Vendedor")
        verbose_name_plural = _("Vendedor")


class Cliente(models.Model):

    #__Cliente_FIELDS__
    nombre = models.TextField(max_length=255, null=True, blank=True)
    direccion = models.TextField(max_length=255, null=True, blank=True)
    rif = models.IntegerField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    antiguedad = models.IntegerField(null=True, blank=True)
    idvendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

    #__Cliente_FIELDS__END

    class Meta:
        verbose_name        = _("Cliente")
        verbose_name_plural = _("Cliente")



#__MODELS__END
