from rest_framework import serializers
from .models import Dog, Temperament

class TemperamentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Temperament
		fields = ('id', 'name', 'dogs')


class DogSerializer(serializers.ModelSerializer):
	temperaments = TemperamentSerializer(many=True)

	class Meta:
		model = Dog
		fields = ('id', 'image', 'name', 'weight', 'height', 'life_span', 'origin', 'temperaments')