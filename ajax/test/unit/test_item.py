from test.ajaxtestcase import TestCase
from app.utils import to_json


class ItemEndpointTestCase(TestCase):

    def test_get_collection(self):
        # setup
        self.test_client.post('/items', data={'name': 'Laundry'})
        self.test_client.post('/items', data={
            'name': 'Tickets',
            'order': 1,
        })

        data = to_json(self.test_client.get('/items'))
        self.assertEqual(len(data), 2)

    def test_get_collection_with_params(self):
        # setup
        self.test_client.post('/items', data={'name': 'Laundry'})
        self.test_client.post('/items', data={'name': 'Tickets'})

        data = to_json(self.test_client.get('/items?name=Laundry'))
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'Laundry')

    def test_post_collection(self):
        mock_data1 = {'name': 'Laundry'}
        mock_data2 = {'name': 'Tickets', 'order': 1}

        data = to_json(self.test_client.post('/items', data=mock_data1))
        self.assertEqual(data['name'], mock_data1['name'])
        # decode('utf8') converts int to unicode, therefore need to cast
        self.assertEqual(int(data['order']), 0)

        data = to_json(self.test_client.post('/items', data=mock_data2))
        self.assertEqual(data['name'], mock_data2['name'])
        self.assertEqual(int(data['order']), 1)

    def test_get_detail(self):
        # setup
        mock_data = {'name': 'Laundry'}
        data = to_json(self.test_client.post('/items', data=mock_data))
        id = data['id']

        data = to_json(self.test_client.get('/items/' + id))
        self.assertEqual(data['name'], mock_data['name'])

    def test_patch_detail(self):
        # setup
        mock_data = {'name': 'Laundry'}
        data = to_json(self.test_client.post('/items', data=mock_data))
        id = data['id']

        data = to_json(self.test_client.patch(
            '/items/' + id,
            data={'name': 'Tickets'},
        ))
        self.assertEqual(data['id'], id)
        self.assertEqual(data['name'], 'Tickets')
        self.assertEqual(int(data['order']), 0)

    def test_delete_detail(self):
        # setup
        mock_data = {'name': 'Laundry'}
        data = to_json(self.test_client.post('/items', data=mock_data))
        id = data['id']

        self.test_client.delete('/items/' + id)
        data = to_json(self.test_client.get('/items/' + id))
        self.assertEqual(data, {})
