from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_or_update_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
    else:
        instance.account.save()
    

    