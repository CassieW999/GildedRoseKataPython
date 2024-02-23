# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 1, "Aged Brie quality should increase as it ages."

    def test_sulfuras_never_decreases_in_quality_or_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 80 and items[0].sell_in == 0, "Sulfuras quality and sell-in should never decrease."

    def test_backstage_passes_increase_in_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 21, "Backstage passes quality should increase as the concert approaches."

    def test_backstage_passes_increase_in_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 21, "Backstage passes quality should increase as the concert approaches."

    def test_backstage_passes_increase_by_2_with_10_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 22, "Backstage passes quality should increase by 2 when there are 10 days or less."

    def test_backstage_passes_increase_by_3_with_5_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 23, "Backstage passes quality should increase by 3 when there are 5 days or less."

    def test_backstage_passes_quality_drops_to_0_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 0, "Backstage passes quality should drop to 0 after the concert."


if __name__ == '__main__':
    unittest.main()
