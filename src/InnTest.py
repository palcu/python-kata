from Inn import *
import unittest

def testInn():
    myinn = Inn()
    assert(True)

#def test_item_value_after_one_day():

class TestInn(unittest.TestCase):
    def test_update_quality_decreases_sell_in(self):
        myinn = Inn()
        myinn.addItem(Item("Elixir of the Mongoose", 10, 20))
        myinn.updateQuality()
        updated_item = myinn.getList()[0]
        self.assertEqual(updated_item.getSellIn(), 9)

    def test_update_quality_does_not_decrease_for_sulfuras(self):
        myinn = Inn()
        myinn.addItem(Item("Sulfuras, Hand of Ragnaros", 10, 20))
        myinn.updateQuality()
        updated_item = myinn.getList()[0]
        self.assertEqual(updated_item.getSellIn(), 10)

    def test_update_quality_decreases_quality(self):
        myinn = Inn()
        myinn.addItem(Item("Elixir of the Mongoose", 10, 20))
        myinn.updateQuality()
        updated_item = myinn.getList()[0]
        self.assertEqual(updated_item.getQuality(), 19)

    def test_update_quality_does_not_decrease_quality_for_sulfuras(self):
        myinn = Inn()
        myinn.addItem(Item("Sulfuras, Hand of Ragnaros", 10, 20))
        myinn.updateQuality()
        updated_item = myinn.getList()[0]
        self.assertEqual(updated_item.getQuality(), 20)

    def test_update_quality_decreases_quality_by_two_past_the_sellin_date(self):
        myinn = Inn()
        myinn.addItem(Item("Elixir of the Mongoose", -1, 20))
        myinn.updateQuality()
        updated_item = myinn.getList()[0]
        self.assertEqual(updated_item.getQuality(), 18)

    def test_update_quality_increases_quality_of_bree_by_two_past_the_sellin_date(self):
        myinn = Inn()
        myinn.addItem(Item("Aged Brie", 1, 20))
        myinn.updateQuality()
        updated_item = myinn.getList()[0]
        self.assertEqual(updated_item.getQuality(), 21)

    def test_quality_never_goes_over_50(self):
        myinn = Inn()
        myinn.addItem(Item("Aged Brie", 1, 50))
        myinn.updateQuality()
        updated_item = myinn.getList()[0]
        self.assertEqual(updated_item.getQuality(), 50)

    def test_quality_never_goes_below_0(self):
        myinn = Inn()
        myinn.addItem(Item("Elixir of the Mongoose", 1, 0))
        myinn.updateQuality()
        updated_item = myinn.getList()[0]
        self.assertEqual(updated_item.getQuality(), 0)

    def test_backstage_goes_to_zero_after_concert(self):
        myinn = Inn()
        myinn.addItem(Item("Backstage passes to a TAFKAL80ETC concert", 0, 50))
        myinn.updateQuality()
        updated_item = myinn.getList()[0]
        self.assertEqual(updated_item.getQuality(), 0)

    def test_backstage_goes_increases_by_one_more_than_10_days_before_concert(self):
        myinn = Inn()
        myinn.addItem(Item("Backstage passes to a TAFKAL80ETC concert", 12, 10))
        myinn.updateQuality()
        updated_item = myinn.getList()[0]
        self.assertEqual(updated_item.getQuality(), 11)

if __name__ == "__main__":
    unittest.main()
