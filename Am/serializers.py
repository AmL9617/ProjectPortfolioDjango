from rest_framework import serializers

from .models import *

class UserSerailizer(serializers.ModelSerializer):
	class Meta:
		model = Home
		fields = '__all__'