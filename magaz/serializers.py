from rest_framework import serializers

from .models import Category, Item


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    code = serializers.IntegerField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def detail(self, validated_data):
        return Category.objects.detail(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.name = validated_data['code']
        instance.save()
        return instance
