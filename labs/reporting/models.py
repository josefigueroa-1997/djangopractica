from django.db import models


class Report(models.Model):

    descripcion = models.CharField(max_length=100,blank=False, null=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return "{} - {}".format(self.descripcion,self.fecha)