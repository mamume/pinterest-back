from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username', 'password', 'first_name', 'last_name', 'age', 'gender', 'country', 'bio', 'profile_pic']
        extra_kwargs = {'password':{'write_only':True}}

    def save(self, **kwargs):
        user = User(
            email = self.validated_data.get('email'),
            username = self.validated_data.get('username'),
            first_name = self.validated_data.get('first_name'),
            last_name = self.validated_data.get('last_name'),
            age = self.validated_data.get('age'),
            bio = self.validated_data.get('bio'),
            gender = self.validated_data.get('gender'),
            country = self.validated_data.get('country'),
            profile_pic = self.validated_data.get('profile_pic'),
                
            )

        user.set_password(self.validated_data.get('password'))
        user.save()

        return user
