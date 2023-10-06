from __future__ import print_function

from gilded_rose import *

if __name__ == "__main__":
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]

    days = 100
    import sys

    content = ""
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        content += str("-------- day %s --------\n" % day)
        content += "name, sellIn, quality\n"
        for item in items:
            content += str(item)
            content += "\n"
        content += "\n"
        GildedRose(items).update_quality()

    file = open('output.txt', 'wb')
    file.write(content.encode("UTF-8"))
    file.close()
