from test.ajaxtestcase import TestCase
from app.utils import to_json


class UserEndpointTestCase(TestCase):

    def test_get_collection(self):
        # setup
        self.test_client.post('/users', data={'name': 'joe'})
        self.test_client.post('/users', data={'name': 'john'})

        data = to_json(self.test_client.get('/users'))
        self.assertEqual(len(data), 2)

    def test_get_collection_with_params(self):
        # setup
        self.test_client.post('/users', data={'name': 'joe'})
        self.test_client.post('/users', data={'name': 'john'})

        data = to_json(self.test_client.get('/users?name=joe'))
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'joe')

    def test_post_collection(self):
        mock_data = {'name': 'Joe'}
        data = to_json(self.test_client.post('/users', data=mock_data))
        self.assertEqual(data['name'], mock_data['name'])

    def test_get_detail(self):
        # setup
        mock_data = {'name': 'Joe'}
        data = to_json(self.test_client.post('/users', data=mock_data))
        id = data['id']
        data = to_json(self.test_client.get('/users/' + id))
        self.assertEqual(data['name'], mock_data['name'])

    def test_patch_detail(self):
        # setup
        mock_data = {'name': 'Joe'}
        data = to_json(self.test_client.post('/users', data=mock_data))
        id = data['id']
        data = to_json(self.test_client.patch(
            '/users/' + id,
            data={'name': 'John'},
        ))
        self.assertEqual(data['id'], id)
        self.assertEqual(data['name'], 'John')

    def test_delete_detail(self):
        mock_data = {'name': 'Joe'}
        data = to_json(self.test_client.post('/users', data=mock_data))
        id = data['id']
        self.test_client.delete('/users/' + id)
        data = to_json(self.test_client.get('/users/' + id))
        self.assertEqual(data, {})
