from json import loads as loadJSON
from json import dumps as writeJSON
import logging
import os.path
class Player:
    def __init__(self,log: logging.Logger, inventory: dict, stats: dict, name: str):
        self.STATS=stats
        self.INVENTORY=inventory
        self.log=log
        self.NAME=name

    def create(self):
        pass
    def move(self,location: str):
        pass
class World:
    def __init__(self,map: dict):
        self.MAP=map
class NPC:
    def __init__(self,log: logging.Logger,dialoguepath: str):
        self.log=log
        self.dialoguepath=dialoguepath

class Item:
    #Base class for all items in the game
    def __init__(self, log: logging.Logger,stats: dict):
        self.log=log
        self.RARITY=stats["rarity"]
        self.ID=stats["id"]
        self.NAME=stats["name"]
        self.LORE=stats["lore"]
        self.EFFECTS=stats["effects"]
class Weapon(Item):
    def __init__(self, log: logging.Logger, stats: dict):
        super().__init__(log,stats)
        self.DURABILITY=stats["durability"]
        self.DMAX=stats["max_durability"]
        self.DAMAGE=stats["damage"]
class Tool(Item):
    def __init__(self, log: logging.Logger, stats: dict):
        super().__init__(log,stats)
        self.DURABILITY=stats["durability"]
        self.DMAX=stats["max_durability"]
        self.TYPE=stats["type"]
        self.SPEED=stats["speed"]
class Consumable(Item):
    def __init__(self, log: logging.Logger, stats: dict):
        super().__init__(log,stats)
        self.ACTIVE_EFFECTS=stats["consume_effects"]
        self.NOURISHMENT=stats["nourishment"]
class Wearable(Item):
    def __init__(self, log: logging.Logger, stats: dict):
        super().__init__(log,stats)
        self.DURABILITY=stats["durability"]
        self.DMAX=stats["max_durability"]
        self.TYPE=stats["type"]
        self.ARMOR=stats["armor"]
        self.ACTIVE_EFFECTS=stats["wear_effects"]
class Game:
    def __init__(self):
        pass
    def update(self):
        pass