from rest_framework import serializers
from .models import FormTemplates



class UsersTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormTemplates
        fields = '__all__'

