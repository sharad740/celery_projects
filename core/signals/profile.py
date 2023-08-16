from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import signals
from django.contrib.auth.models import User
from core.models.profiles import Profile

@receiver(signals.post_save, sender=User)
def post_usersave(sender, created, instance, **kwargs):
    if created:
        if not Profile.objects.filter(user=instance).exists():
            profile , _ = Profile.objects.get_or_create(user=instance)
            profile.save()