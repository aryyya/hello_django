from django.core.exceptions import ValidationError
from django.test import TestCase
from menu.models import Origin

def get_origin(city='New York', state='New York', country='United States', latitude='40.7128', longitude='74.0060', grower_name='Barack Obama'):
    return Origin(city=city, state=state, country=country, latitude=latitude, longitude=longitude, grower_name=grower_name)

class OriginTestCase(TestCase):

    def setUp(self):
        pass

    def test_an_origin_can_be_saved(self):
        origin = get_origin()
        origin.save()
        self.assertTrue(origin == Origin.objects.get(pk=origin.id))

    def test_only_save_valid_data(self):
        valid_origin = get_origin(latitude='1.0', longitude='1.0')
        valid_origin.save()
        self.assertTrue(valid_origin == Origin.objects.get(pk=valid_origin.id))

        invalid_origin = get_origin()
        invalid_origin.latitude = "999"
        invalid_origin.longitude = "999"
        self.assertRaises(ValidationError, invalid_origin.save)
