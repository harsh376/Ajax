from test.ajaxtestcase import TestCase


class AuthEndpointTestCase(TestCase):

    def setUp(self):
        super(AuthEndpointTestCase, self).setUp()
        self.data1 = {
            'email': 'joe@email.com',
            'password': 'joe123',
        }

    def test_post_collection_missing_fields(self):
        new_data = {'email': 'joe@email.com'}
        data = self.test_client.post('/users/v2', data=new_data)
        self.assertEqual(data.status_code, 400)

    def test_post_collection_invalid_credentials(self):
        self.test_client.post('/users/v2', data=self.data1)
        self.data1['password'] = 'abc'
        data = self.test_client.post('/token', data=self.data1)
        self.assertEqual(data.status_code, 401)

    def test_post_collection_valid(self):
        self.test_client.post('/users/v2', data=self.data1)
        data = self.test_client.post('/token', data=self.data1)
        self.assertEqual(data.status_code, 201)
