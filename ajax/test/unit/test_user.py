import json

from test.ajaxtestcase import TestCase


class UserEndpointTestCase(TestCase):

    def test_get_collection(self):
        # setup
        self.test_client.post('/users', data={'name': 'joe'})
        self.test_client.post('/users', data={'name': 'john'})

        data = json.loads(self.test_client.get('/users').data.decode('utf8'))
        self.assertEqual(len(data), 2)

    def test_get_collection_with_params(self):
        # setup
        self.test_client.post('/users', data={'name': 'joe'})
        self.test_client.post('/users', data={'name': 'john'})

        data = json.loads(
            self.test_client.get('/users?name=joe').data.decode('utf8'))
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'joe')

    def test_post_collection(self):
        mock_data = {'name': 'Joe'}
        data = self.test_client.post('/users', data=mock_data)
        conditioned_data = json.loads(data.data.decode('utf8'))
        self.assertEqual(conditioned_data['name'], mock_data['name'])

    def test_get_detail(self):
        # setup
        mock_data = {'name': 'Joe'}
        data = self.test_client.post('/users', data=mock_data)
        id = json.loads(data.data.decode('utf8'))['id']

        data = json.loads(self.test_client.get('/users/' + id).data.decode(
            'utf8'))
        self.assertEqual(data['name'], mock_data['name'])

    def test_patch_detail(self):
        # setup
        mock_data = {'name': 'Joe'}
        data = self.test_client.post('/users', data=mock_data)
        id = json.loads(data.data.decode('utf8'))['id']

        data = json.loads(self.test_client.patch(
            '/users/' + id,
            data={'name': 'John'},
        ).data.decode('utf8'))
        self.assertEqual(data['id'], id)
        self.assertEqual(data['name'], 'John')

    def test_delete_detail(self):
        mock_data = {'name': 'Joe'}
        data = self.test_client.post('/users', data=mock_data)
        id = json.loads(data.data.decode('utf8'))['id']

        self.test_client.delete('/users/' + id)
        data = json.loads(self.test_client.get('/users/' + id).data.decode(
            'utf8'))
        self.assertEqual(data, {})
