from .models import User, UserProfile
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print("user profile is created")
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # Create the userprofile if it does not exist
            UserProfile.objects.create(user=instance)
            print("Profile does not exist, I created one")
        print("User is updated")

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, "this user is being saved")
# post_save.connect(post_save_created_receiver, sender=User)