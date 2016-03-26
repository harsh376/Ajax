import json

from test.ajaxtestcase import TestCase


class ItemEndpointTestCase(TestCase):

    def test_get_collection(self):
        # setup
        self.test_client.post('/items', data={'name': 'Laundry'})
        self.test_client.post('/items', data={
            'name': 'Tickets',
            'order': 1,
        })

        data = json.loads(self.test_client.get('/items').data.decode('utf8'))
        self.assertEqual(len(data), 2)

    def test_get_collection_with_params(self):
        # setup
        self.test_client.post('/items', data={'name': 'Laundry'})
        self.test_client.post('/items', data={'name': 'Tickets'})

        data = json.loads(
            self.test_client.get('/items?name=Laundry').data.decode('utf8'))
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'Laundry')

    def test_post_collection(self):
        mock_data1 = {'name': 'Laundry'}
        mock_data2 = {'name': 'Tickets', 'order': 1}
        data = self.test_client.post('/items', data=mock_data1)
        conditioned_data = json.loads(data.data.decode('utf8'))
        self.assertEqual(conditioned_data['name'], mock_data1['name'])
        # decode('utf8') converts int to unicode, therefore need to cast
        self.assertEqual(int(conditioned_data['order']), 0)

        data = self.test_client.post('/items', data=mock_data2)
        conditioned_data = json.loads(data.data.decode('utf8'))
        self.assertEqual(conditioned_data['name'], mock_data2['name'])
        # decode('utf8') converts int to unicode, therefore need to cast
        self.assertEqual(int(conditioned_data['order']), 1)

    def test_get_detail(self):
        # setup
        mock_data = {'name': 'Laundry'}
        data = self.test_client.post('/items', data=mock_data)
        id = json.loads(data.data.decode('utf8'))['id']

        data = json.loads(self.test_client.get('/items/' + id).data.decode(
            'utf8'))
        self.assertEqual(data['name'], mock_data['name'])

    def test_patch_detail(self):
        # setup
        mock_data = {'name': 'Laundry'}
        data = self.test_client.post('/items', data=mock_data)
        id = json.loads(data.data.decode('utf8'))['id']

        data = json.loads(self.test_client.patch(
            '/items/' + id,
            data={'name': 'Tickets'},
        ).data.decode('utf8'))
        self.assertEqual(data['id'], id)
        self.assertEqual(data['name'], 'Tickets')
        self.assertEqual(int(data['order']), 0)

    def test_delete_detail(self):
        mock_data = {'name': 'Laundry'}
        data = self.test_client.post('/items', data=mock_data)
        id = json.loads(data.data.decode('utf8'))['id']

        self.test_client.delete('/items/' + id)
        data = json.loads(self.test_client.get('/items/' + id).data.decode(
            'utf8'))
        self.assertEqual(data, {})
