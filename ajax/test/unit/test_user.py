from test.ajaxtestcase import TestCase
from app.utils import to_json

data1 = {
    'first_name': 'joe',
    'last_name': 'baker',
    'email': 'joe@email.com',
    'photo_url': 'https://lh3.googleusercontent.com/12321.jpg',
    'external_auth_type': 'google',
    'external_auth_id': 123213123324324,
}
data2 = {
    'first_name': 'jack',
    'email': 'jack@email.com',
    'external_auth_type': 'google',
    'external_auth_id': 1000012323,
}


class UserEndpointTestCase(TestCase):

    # Collection

    def test_get_collection(self):
        # setup
        self.test_client.post('/users', data=data1)
        self.test_client.post('/users', data=data2)

        data = to_json(self.test_client.get('/users'))
        self.assertEqual(len(data), 2)
        self._is_equal(data1, data[0])
        self._is_equal(data2, data[1])

    def test_get_collection_with_params(self):
        # setup
        self.test_client.post('/users', data=data1)
        self.test_client.post('/users', data=data2)

        data = to_json(self.test_client.get(
            '/users?email=joe@email.com&external_auth_type=google',
        ))
        self.assertEqual(len(data), 1)
        self._is_equal(data1, data[0])

    def test_post_collection(self):
        data = to_json(self.test_client.post('/users', data=data1))
        self._is_equal(data1, data)

    # Detail

    def test_get_detail(self):
        # setup
        data = to_json(self.test_client.post('/users', data=data1))
        id = data['id']
        data = to_json(self.test_client.get('/users/' + id))
        self._is_equal(data1, data)

    def test_patch_detail(self):
        # setup
        data = to_json(self.test_client.post('/users', data=data1))
        id = data['id']
        data = to_json(self.test_client.patch(
            '/users/' + id,
            data={'first_name': 'John'},
        ))
        self.assertEqual(data['id'], id)
        self.assertEqual(data['first_name'], 'John')

    def test_delete_detail(self):
        data = to_json(self.test_client.post('/users', data=data1))
        id = data['id']
        self.test_client.delete('/users/' + id)
        data = to_json(self.test_client.get('/users/' + id))
        self.assertEqual(data, {})

    def _is_equal(self, first, second):
        for key in first:
            self.assertEqual(str(first[key]), second[key])
