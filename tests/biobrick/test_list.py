from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from biohub.biobrick.models import Biobrick


class TestList(APITestCase):
    # To test the list rest-api

    def test_empty(self):
        # Test the empty list with no data in the database
        resp = self.client.get(reverse('api:biobrick:biobrick-list'))
        self.assertEqual(len(resp.data['results']), 0)

    def test_show(self):
        # Test if biobrick-list can show the bbk
        bbk = Biobrick.objects.create(part_name='asdfasvasvav')
        resp = self.client.get(reverse('api:biobrick:biobrick-list'))
        self.assertEqual(len(resp.data['results']), 1)
        self.assertDictContainsSubset({
            'part_name': bbk.part_name,
        }, resp.data['results'][0])

    def test_order(self):
        # Test if biobrick-list can show the bbk in the specific order
        bbk1 = Biobrick.objects.create(part_name='aaaaaaaa', uses=10)
        bbk2 = Biobrick.objects.create(part_name='bbbbbbbb', uses=20)

        resp = self.client.get(reverse('api:biobrick:biobrick-list'))
        self.assertDictContainsSubset({
            'part_name': bbk1.part_name,
        }, resp.data['results'][0])

        resp = self.client.get(reverse('api:biobrick:biobrick-list'),
                               {'order': '-uses'})
        self.assertDictContainsSubset({
            'part_name': bbk2.part_name,
        }, resp.data['results'][0])

        resp = self.client.get(reverse('api:biobrick:biobrick-list'),
                               {'order': '2333?'})
        self.assertDictContainsSubset({
            'part_name': bbk1.part_name,
        }, resp.data['results'][0])