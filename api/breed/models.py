from django.db import models
import uuid

class Dog(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	image = models.JSONField()
	name = models.CharField(max_length=255)
	weight = models.JSONField()
	height = models.JSONField()
	life_span = models.CharField(max_length=255)
	origin = models.CharField(max_length=255)
	temperaments = models.ManyToManyField('Temperament', through='DogTemperament', related_name='dog_temperament')

	class Meta:
		db_table = 'dogs'


class Temperament(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=255)
	dogs = models.ManyToManyField('Dog', through='DogTemperament', related_name='dog_temperament')

	class Meta:
		db_table = 'temperaments'


class DogTemperament(models.Model):
	dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
	temperament = models.ForeignKey(Temperament, on_delete=models.CASCADE)

	class Meta:
		db_table = 'dog_temperament'