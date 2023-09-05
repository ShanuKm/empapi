from rest_framework import serializers
from .models import Emp

class EmpSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)    
    phone=serializers.CharField(max_length=10)
    address=serializers.CharField(max_length=150)
    department=serializers.CharField(max_length=10)

    def create(self,validated_data):
        return  Emp.objects.create(**validated_data)
    
    def update(self, instance,validated_data):
        #print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        #print(instance.name)
        instance.department=validated_data.get('department',instance.department)
        instance.phone=validated_data.get('phone',instance.phone)
        instance.address=validated_data.get('address',instance.address)
        instance.save()
        return instance