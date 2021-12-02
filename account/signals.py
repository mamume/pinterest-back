# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from .models import UserProfile
# from oauth2_provider.models import AccessToken
# from oauth2_provider.models import RefreshToken
# from oauth2_provider.models import Application
# from django.utils import timezone
# from oauthlib.common import generate_token

# def refresh_time():
#     time = timezone.now() + timezone.timedelta(days=7)
#     return time

# def access_time():
#     time = timezone.now() + timezone.timedelta(hours=10)
#     return time

# ref_tok = generate_token()
# acc_tok = generate_token()
# app = Application.objects.get(id=1)

# @receiver(post_save, sender=UserProfile)
# def signupToken(created, instance, *args, **kwargs):
#     print(access_time())

#     if created:
#         refresh_token = RefreshToken.objects.create(user=instance, application=app, revoked=refresh_time(), token=ref_tok)
#         access_token = AccessToken.objects.create(
#             user=instance,
#             source_refresh_token=refresh_token,
#             application=app,
#             expires = access_time(),
#             token=acc_tok,
#             scope='read write'
#         )
#         RefreshToken.objects.filter(token=ref_tok).update(access_token=access_token)
