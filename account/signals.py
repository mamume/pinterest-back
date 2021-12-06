from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import UserProfile, Notification
from oauth2_provider.models import AccessToken
from oauth2_provider.models import RefreshToken
from oauth2_provider.models import Application
from django.utils import timezone
from oauthlib.common import generate_token
from pin.models import Pin

def refresh_time():
    time = timezone.now() + timezone.timedelta(days=7)
    return time

def access_time():
    time = timezone.now() + timezone.timedelta(hours=10)
    return time



    

@receiver(post_save, sender=UserProfile)
def signupToken(created, instance, *args, **kwargs):
    if created:
        try:

            ref_tok = generate_token()
            acc_tok = generate_token()
            app = Application.objects.get(id=1)
            if not instance.is_superuser:
                refresh_token = RefreshToken.objects.create(user=instance, application=app, revoked=refresh_time(), token=ref_tok)
                access_token = AccessToken.objects.create(
                    user=instance,
                    source_refresh_token=refresh_token, 
                    application=app, 
                    expires = access_time(),
                    token=acc_tok,
                    scope='read write'
                )
                RefreshToken.objects.filter(token=ref_tok).update(access_token=access_token)
        except Exception as e:
            print(e)



@receiver(post_save, sender=Pin)
def post_notif(instance, created, *args, **kwargs):
    if created:
        users = instance.owner.follower.all()
        for user in users:
            Notification.objects.create(text=f"{instance.owner} posted new pin '{instance.title}'", user=user.user)