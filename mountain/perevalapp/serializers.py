from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
# from users.serializers import PassUserSerializer
from .models import Pereval, MyUser, Coord, Images, Level


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', 'phone', 'fam', 'name', 'otc']

    def save(self, **kwargs):
        self.is_valid()
        user = MyUser.objects.filter(email=self.validated_data.get('email'))
        if user.exists():
            return user.first()
        else:
            new_user = MyUser.objects.create(
                email=self.validated_data.get('email'),
                phone=self.validated_data.get('phone'),
                fam=self.validated_data.get('fam'),
                name=self.validated_data.get('name'),
                otc=self.validated_data.get('otc'),
            )
        return new_user


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['latitude', 'longitude', 'height', ]


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class PerevalSerializer(WritableNestedModelSerializer):
    user_id = MyUserSerializer()
    coord_id = CoordSerializer()
    level_id = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'level_id', 'user_id', 'coord_id', 'images']
