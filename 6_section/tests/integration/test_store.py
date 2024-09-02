from models.store import StoreModel
from models.item import ItemModel

from tests.integration.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store_item(self):
        store = StoreModel("store_1")

        self.assertIsNone(store.items.all(), [], "The store's items not 0 ")


    def test_crud(self):
        store = StoreModel("store_1")

        self.assertIsNone(StoreModel.find_by_name('store_1'))

        store.save_to_db()

        self.assertIsNotNone(StoreModel.find_by_name('store_1'))

        store.delete_from_db()
        self.assertIsNone(StoreModel.find_by_name('store_1'))


    def test_store_relatuinship(self):
        store = StoreModel("store_1")
        item = ItemModel("test", 19.99, 1)

        store.save_to_db()
        item.save_to_db()

        self.assertEqual(store.items.count(), 1)
        self.assertEqual(store.items.first().name, "test")
