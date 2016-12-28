from test.ajaxtestcase import TestCase
from app.utils import to_json


class UserV2EndpointTestCase(TestCase):
    def setUp(self):
        super(UserV2EndpointTestCase, self).setUp()
        self.data1 = {
            'email': 'joe@email.com',
            'password': 'joe123',
        }
        self.data2 = {
            'email': 'jack@email.com',
            'password': 'jack123',
        }
        self.test_client.post('/users/v2', data=self.data1)

    # Collection
    def test_get_collection_without_email(self):
        response = self.test_client.get('/users/v2')
        self.assertEquals(response.status_code, 400)

    def test_get_collection_with_email(self):
        response = self.test_client.get('/users/v2?email=joe@email.com')
        self.assertEqual(response.status_code, 200)
        data = to_json(response)
        self.assertEqual(len(data), 1)
        self.assertEqual(self.data1['email'], data[0]['email'])

    def test_get_collection_with_invalid_email(self):
        response = self.test_client.get('/users/v2?email=joooo@email.com')
        self.assertEqual(response.status_code, 200)
        data = to_json(response)
        self.assertEqual(len(data), 0)

    def test_post_collection(self):
        response = self.test_client.post('/users/v2', data=self.data2)
        self.assertEqual(response.status_code, 201)
        data = to_json(response)
        self.assertEqual(data, {'email': self.data2['email']})

    def test_post_collection_missing_fields(self):
        new_data = {'email': 'rachel@email.com'}
        response = self.test_client.post('/users/v2', data=new_data)
        self.assertEqual(response.status_code, 400)

    def test_post_collection_duplicate(self):
        response = self.test_client.post('/users/v2', data=self.data1)
        self.assertEqual(response.status_code, 409)
