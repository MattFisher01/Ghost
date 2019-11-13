from django.db import models

# Create your models here.
class ghost_user(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    def __str__(self):
        return '%s %s' % self.first_name, self.last_name



class ghost_names(models.Model):
    person = models.OneToOneField(ghost_user, on_delete=models.SET_NULL, null=True, blank=True)
    ghost_name = models.CharField(max_length=256)
    descripton = models.CharField(max_length=256)

    def __str__(self):
        return self.ghost_name
