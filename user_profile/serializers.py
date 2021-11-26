from rest_framework import serializers
from account.models import UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'get_full_name', 'profile_pic', 'username']

    # country_name = serializers.SerializerMethodField('get_country_name')
    full_name = serializers.SerializerMethodField('get_full_name')

    # def get_country_name(self, instance):
    #     return instance.country.name

    def get_full_name(self, instance: UserProfile):
        return f"{instance.first_name} {instance.last_name}"
