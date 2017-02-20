# -*- coding: utf-8 -*-

from Item import *

def update_stock_item(item):
    item.setSellIn(item.getSellIn() - 1)

    if item.getSellIn() < 0:
        item.setQuality(item.getQuality() - 1)

    item.setQuality(item.getQuality() - 1)

def update_brie_item(item):
    item.setQuality(item.getQuality() + 1)

def update_backstage_pass_item(item):
    item.setSellIn(item.getSellIn() - 1)

    if item.getSellIn() < 0:
        item.setQuality(0)
    if item.getSellIn() > 10:
        item.setQuality(item.getQuality() + 1)

def update_item(item):
    success = False
    if item.getName() in ["+5 Dexterity Vest", "Elixir of the Mongoose"]:
        update_stock_item(item)
        success = True
    if item.getName() == "Aged Brie":
        update_brie_item(item)
        success= True
    if item.getName() == "Backstage passes to a TAFKAL80ETC concert":
        update_backstage_pass_item(item)
        success = True

    if success and item.getQuality() > 50:
        item.setQuality(50)
    if success and item.getQuality() < 0:
        item.setQuality(0)

    return success

class Inn(object):
    def __init__(self):
        self.__itemslist=[]

    def addFixtures(self):
        self.__itemslist.append(Item("+5 Dexterity Vest", 10, 20))
        self.__itemslist.append(Item("Aged Brie", 2, 0))
        self.__itemslist.append(Item("Elixir of the Mongoose", 5, 7))
        self.__itemslist.append(Item("Sulfuras, Hand of Ragnaros", 0, 80))
        self.__itemslist.append(Item("Backstage passes to a TAFKAL80ETC concert", 15, 20))
        self.__itemslist.append(Item("Conjured Mana Cake", 3, 6))

    def addItem(self, item):
        self.__itemslist.append(item)

    def getList(self):
        return self.__itemslist

    def updateQuality(self):
        for item in self.__itemslist:
            result = update_item(item)
            if result:
                continue
            if item.getQuality()>0:
                if item.getName()!="Sulfuras, Hand of Ragnaros":
                    item.setQuality(item.getQuality()-1)
            else:
                if item.getQuality()<50:
                    item.setQuality(item.getQuality()+1)
                    
                    if item.getName()=="Backstage passes to a TAFKAL80ETC concert":
                        if item.getSellIn()<11:
                            if item.getQuality()<50:
                                item.setQuality(item.getQuality()+1)

                        if item.getSellIn()<6:
                            if item.getQuality()<50:
                                item.setQuality(item.getQuality()+1)

            if item.getName()!="Sulfuras, Hand of Ragnaros":
                item.setSellIn(item.getSellIn()-1)

            if item.getSellIn()<0:
                if item.getName()=="Aged Brie":
                    if item.getQuality()>0:
                        if item.getName()=="Sulfuras, Hand of Ragnaros":
                            item.setQuality(item.getQuality()-1);
                    else:
                        item.setQuality(item.getQuality()-item.getQuality())
                else:
                    if item.getQuality()>0:
                        item.setQuality(item.getQuality()-1)

def main():
    myapp = Inn()
    myapp.updateQuality()

if __name__ == "__main__":
    main()
