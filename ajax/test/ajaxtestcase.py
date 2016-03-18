import json
import unittest

from app import app, db


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.test_client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_user(self):
        mock_data = {'name': 'Joe'}

        # POST Collection
        self.test_client.post('/users', data=mock_data)

        # GET Collection
        data = json.loads(self.test_client.get('/users').data.decode('utf8'))
        print(data)
        self.assertEqual(data[0]['name'], mock_data['name'])

        detail_url = '/users/' + data[0]['id']

        # PATCH Detail
        data = json.loads(self.test_client.patch(
            detail_url,
            data={'name': 'John'},
        ).data.decode('utf8'))
        print(data)

        # DELETE Detail
        self.test_client.delete(detail_url)

        # GET Detail
        data = json.loads(self.test_client.get(detail_url).data.decode('utf8'))
        print(data)


if __name__ == '__main__':
    unittest.main()
