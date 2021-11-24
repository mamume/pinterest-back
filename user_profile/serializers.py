from rest_framework import serializers
from account.models import UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["username", "first_name", "last_name",
                  "followers_num", "following_num", "pins", "pins_num"]
