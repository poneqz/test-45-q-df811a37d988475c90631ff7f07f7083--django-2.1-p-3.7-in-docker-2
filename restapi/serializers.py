from rest_framework import serializers
from .models import Leads


class LeadsSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    mobile = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    location_type = serializers.CharField(required=True)
    location = serializers.CharField(required=True)

    class Meta:
        model = Leads
        fields = ('id',
                  'first_name',
                  'last_name',
                  'mobile',
                  'email',
                  'location_type',
                  'location',
                  'status',
                  'communication')


class MarkLeadSerializer(serializers.ModelSerializer):
    communication = serializers.CharField(required=True)

    class Meta:
        model = Leads
        fields = ('status', 'communication',)






