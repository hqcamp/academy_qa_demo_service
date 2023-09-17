from rest_framework import serializers
from demo_service.models import PetCategory, Pet
from rest_framework.fields import ChoiceField
from django.http import Http404


class PetCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # Return ID only in get requests
    name = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return PetCategory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # Return ID only in get requests
    name = serializers.CharField(max_length=150)
    photo_url = serializers.CharField(max_length=150)
    category = PetCategorySerializer()
    status = serializers.CharField(max_length=30)
    status = ChoiceField(choices=["available", "pending", "sold"])

    def create(self, validated_data):
        category = validated_data.pop("category")
        category = PetCategory.objects.filter(name=category["name"]).first()

        if not category:
            raise Http404

        return Pet.objects.create(
            name=validated_data["name"],
            photo_url=validated_data["photo_url"],
            status=validated_data["status"],
            category=category,
        )

    def update(self, instance, validated_data):
        category = validated_data.pop("category")
        category = PetCategory.objects.filter(name=category["name"]).first()

        if not category:
            raise Http404

        instance.name = validated_data.get("name", instance.name)
        instance.photo_url = validated_data.get("photo_url", instance.photo_url)
        instance.category = category
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance
