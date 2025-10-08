import unittest
from fastapi.testclient import TestClient
from main import app
from connect import Inform_Status


class TestInformCRUD(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        Inform_Status.delete().execute()

        self.test_data = {
            'podk': 'test_podk',
            'nastr': 'test_nastr',
            'oblak': 'test_oblak'
        }
        self.test_record = Inform_Status.create(**self.test_data)

    def test_read(self):
        """Test GET /inform - получение всех записей"""
        response = self.client.get('/inform')
        print(f"GET /inform: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

        record = data[0]
        self.assertIn('id', record)
        self.assertIn('podk', record)
        self.assertIn('nastr', record)
        self.assertIn('oblak', record)

    def test_add(self):
        """Test POST /inform_post - создание новой записи"""
        # Используем params вместо json
        response = self.client.post(
            '/inform_post',
            params={
                'podk': 'new_podk',
                'nastr': 'new_nastr',
                'oblak': 'new_oblak'
            }
        )
        print(f"POST /inform_post: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

        # Проверка в базе данных
        record_count = Inform_Status.select().where(
            Inform_Status.podk == 'new_podk'
        ).count()
        self.assertEqual(record_count, 1)

    def test_update(self):
        """Test PUT /inform_put/{id} - обновление записи"""
        # Используем params вместо json
        response = self.client.put(
            f'/inform_put/{self.test_record.id}',
            params={
                'podk': 'updated_podk',
                'nastr': 'updated_nastr',
                'oblak': 'updated_oblak'
            }
        )
        print(f"PUT /inform_put/{self.test_record.id}: .\
              {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

        # Проверяем обновление в базе
        updated_record = Inform_Status.get_by_id(self.test_record.id)
        self.assertEqual(updated_record.podk, 'updated_podk')
        self.assertEqual(updated_record.nastr, 'updated_nastr')
        self.assertEqual(updated_record.oblak, 'updated_oblak')

    def test_delete(self):
        """Test DELETE /inform_delete/{id} - удаление записи"""
        temp_record = Inform_Status.create(
            podk='to_delete',
            nastr='to_delete',
            oblak='to_delete'
        )

        initial_count = Inform_Status.select().count()

        response = self.client.delete(f'/inform_delete/{temp_record.id}')
        print(f"DELETE /inform_delete/{temp_record.id}: \
              {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)

        # Проверяем удаление
        final_count = Inform_Status.select().count()
        self.assertEqual(final_count, initial_count - 1)

        with self.assertRaises(Inform_Status.DoesNotExist):
            Inform_Status.get_by_id(temp_record.id)


if __name__ == '__main__':
    unittest.main()
