import unittest

from models.item import ItemModel
WRONG_NAME = "the name of item is wrong"
WRONG_PRICE = "the name of item is wrong"
WRONG_JSON = ""

class TestItems(unittest.TestCase):
    def setUp(self):
        item = ItemModel(name='NewItem', price=3)
        return item

    def test_item_creating(self):
        item = self.setUp()
        self.assertEqual(item.name, "NewItem", WRONG_NAME)
        self.assertEqual(item.price, 3, WRONG_PRICE)

    def test_item_jsonfy(self):
        item = self.setUp()
        ex = {"name" : "NewItem", "price" : 3}
        self.assertDictEqual(item.json, ex, WRONG_JSON)
        



if __name__== "__main__":
    unittest.main()


