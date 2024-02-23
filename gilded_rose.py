# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue  # Sulfuras does not change

            self.update_sell_in(item)

            if item.name == "Aged Brie":
                self.update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage_pass(item)
            elif item.name.startswith("Conjured"):
                self.update_conjured_item(item)
            else:
                self.update_normal_item(item)

            self.ensure_quality_limits(item)

    def update_sell_in(self, item):
        item.sell_in -= 1

    def update_aged_brie(self, item):
        if item.sell_in < 0:
            self.add_quality(item, 2)
        else:
            self.add_quality(item, 1)

    def update_backstage_pass(self, item):
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            self.add_quality(item, 3)
        elif item.sell_in < 10:
            self.add_quality(item, 2)
        else:
            self.add_quality(item, 1)

    def update_normal_item(self, item):
        if item.sell_in < 0:
            self.subtract_quality(item, 2)
        else:
            self.subtract_quality(item, 1)

    def update_conjured_item(self, item):
        if item.sell_in < 0:
            self.subtract_quality(item, 4)  # Twice as fast as normal items
        else:
            self.subtract_quality(item, 2)

    def ensure_quality_limits(self, item):
        if item.quality < 0:
            item.quality = 0
        elif item.quality > 50:
            if item.name != "Sulfuras, Hand of Ragnaros":  # Sulfuras can exceed 50
                item.quality = 50

    def add_quality(self, item, amount):
        item.quality += amount

    def subtract_quality(self, item, amount):
        item.quality -= amount
