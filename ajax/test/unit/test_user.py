from test.ajaxtestcase import TestCase
from app.utils import to_json

data1 = {
    'name': 'joe',
    'email': 'joe@email.com',
}
data2 = {
    'name': 'john',
    'email': 'john@email.com',
}


class UserEndpointTestCase(TestCase):

    def test_get_collection(self):
        # setup
        self.test_client.post('/users', data=data1)
        self.test_client.post('/users', data=data2)

        data = to_json(self.test_client.get('/users'))
        self.assertEqual(len(data), 2)

    def test_get_collection_with_params(self):
        # setup
        self.test_client.post('/users', data=data1)
        self.test_client.post('/users', data=data2)

        data = to_json(self.test_client.get('/users?name=joe'))
        self.assertEqual(len(data), 1)
        self._is_equal(data1, data[0])

    def test_post_collection(self):
        data = to_json(self.test_client.post('/users', data=data1))
        self._is_equal(data1, data)

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
            data={'name': 'John'},
        ))
        self.assertEqual(data['id'], id)
        self.assertEqual(data['name'], 'John')

    def test_delete_detail(self):
        data = to_json(self.test_client.post('/users', data=data1))
        id = data['id']
        self.test_client.delete('/users/' + id)
        data = to_json(self.test_client.get('/users/' + id))
        self.assertEqual(data, {})

    def _is_equal(self, first, second):
        for key in first:
            self.assertEqual(first[key], second[key])
