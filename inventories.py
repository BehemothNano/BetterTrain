"""
The inventory library behind the BetterTrain roguelike.
Used for players, chests, loot tables, etc.
Copyright (C) 2023-2024 Dylan Buchanan
"""

itemIDS = genItemIDS()

class LootTable():
    tables = {}
    def __init__(self, name, items):
        """
        Creates a loot table for a given set of items, a matrix.
        Name should be a unique name that references this loot table.
        Items is a dict in the form itemID: drop chance.
        """
        self.itmDict = items
        self.name = name
    
    def __str__(self):
        s = f"---------\nTable ID: {self.name}\n-----\n"
        for itemID in self.itmDict:
            s = s + f"{itemID}: {self.itmDict[itemID]}"
        return s + "\n---------"
    
    def generate(self):
        l = len(self.itmDict)
        