import requests
from django.http import JsonResponse
from ..models import Dog, Temperament, DogTemperament

def fetch_dogs_from_dog_api():
	api_url = 'https://api.thedogapi.com/v1/breeds'
	api_key = 'live_mYqEuqE22grVm35ZYyKeB25L8Db5CsFPKVhhXktFWQKsaBvdHJlgFFmWtqrpSugq'
	headers = { 'x-api-key': api_key }
	response = requests.get(api_url, headers=headers)
	response.raise_for_status()
	dogs_data = response.json()
	dogs_from_api = []
	for dog in dogs_data:
		id = dog.get('id')
		image = dog.get('image', {}).get('url')
		name = dog.get('name')
		weight = dog.get('weight', {}).get('metric')
		height = dog.get('height', {}).get('metric')
		life_span = dog.get('life_span')
		temperament = dog.get('temperament')
		dog_details = {
		    'id': id,
		    'image': image,
		    'name': name,
		    'weight': weight,
		    'height': height,
		    'life_span': life_span,
		    'temperament': temperament or '',
		    'origin': 'Dog API',
		}
		dogs_from_api.append(dog_details)
	return dogs_from_api


def fetch_dogs_from_db():
	dogs_from_db = Dog.objects.all()
	dogs_from_db_with_temperaments = []
	for dog in dogs_from_db:
		id = dog.id
		image = dog.image
		name = dog.name
		weight = dog.weight
		height = dog.height
		life_span = dog.life_span
		dog_temperaments = DogTemperament.objects.filter(dog=dog)
		temperaments_array = []
		for dog_temperament in dog_temperaments:
			temperament_record = dog_temperament.temperament
			temperament = temperament_record.name
			temperaments_array.append(temperament)
		temperaments_list = ', '.join(temperaments_array)
		dog_details = {
		    'id': id,
		    'image': image,
		    'name': name,
		    'weight': weight,
		    'height': height,
		    'life_span': life_span,
		    'temperament': temperaments_list,
		    'origin': origin
		}
		dogs_from_db_with_temperaments.append(dog_details)
	return dogs_from_db_with_temperaments


def get_dogs(request):
	try:
		dogs_from_api = fetch_dogs_from_dog_api()
		dogs_from_db = fetch_dogs_from_db()
		all_dogs = dogs_from_api + dogs_from_db
		return JsonResponse(all_dogs, safe=False)
	except Exception as e:
		print(str(e))
		return JsonResponse({ 'error': 'Internal server error' }, status=500)