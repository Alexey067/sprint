from rest_framework import serializers
from .models import Users, PerevalAdded, Coords


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class PerevalAddedSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    coord_id = CoordsSerializer()

    class Meta:
        model = PerevalAdded
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coord_data = validated_data.pop('coord_id')
        user = Users.objects.filter(email=user_data['email']).first()
        if not user:
            user = Users.objects.create(**user_data)
        coord = Coords.objects.create(**coord_data)
        validated_data['user'] = user
        validated_data['coord_id'] = coord
        pereval_added = PerevalAdded.objects.create(**validated_data)
        return pereval_added
