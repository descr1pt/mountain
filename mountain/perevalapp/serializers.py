from rest_framework import serializers
from .models import Pereval


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = (['id', 'user_id', 'beauty_title', 'title', 'other_titles', 'connect', 'coord_id', 'level_id', 'photo'])