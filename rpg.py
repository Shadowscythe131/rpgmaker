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
class NPC:
    def __init__(self,log: logging.Logger,dialoguepath: str,npcdata: dict):
        self.log=log
        self.DIALOGUEPATH=dialoguepath
        self.npcdata=npcdata
class Item:
    #Base class for all items in the game
    def __init__(self, log: logging.Logger,stats: dict):
        self.log=log
        self.RARITY=stats["rarity"]
        self.ID=stats["id"]
        self.NAME=stats["name"]
        self.LORE=stats["lore"]
        self.EFFECTS=stats["effects"]
        self.log.info(f"Instantiated new Item (id={self.ID}, name={self.NAME}")
class Weapon(Item):
    def __init__(self, log: logging.Logger, stats: dict):
        super().__init__(log,stats)
        self.durability=stats["durability"]
        self.dmax=stats["max_durability"]
        self.damage=stats["damage"]
        
class Tool(Item):
    def __init__(self, log: logging.Logger, stats: dict):
        super().__init__(log,stats)
        self.durability=stats["durability"]
        self.dmax=stats["max_durability"]
        self.TYPE=stats["type"]
        self.speed=stats["speed"]
        
class Consumable(Item):
    def __init__(self, log: logging.Logger, stats: dict):
        super().__init__(log,stats)
        self.ACTIVE_EFFECTS=stats["consume_effects"]
        self.NOURISHMENT=stats["nourishment"]
        
class Wearable(Item):
    def __init__(self, log: logging.Logger, stats: dict):
        super().__init__(log,stats)
        self.durability=stats["durability"]
        self.dmax=stats["max_durability"]
        self.TYPE=stats["type"]
        self.armor=stats["armor"]
        self.active_effects=stats["wear_effects"]
        
class Game:
    def __init__(self, log: logging.Logger):
        self.log=log
    def update(self):
        pass
    def load(self,resourcepath):
        try:
            with open(resourcepath+"/map.json","r") as mapfile:
                content=mapfile.read()
                self.MAP=loadJSON(content)
            self.log.info(f"Loaded map data successfully from {resourcepath}/map.json")
        except Exception as e:
            self.log.error(f"Error loading map data from {resourcepath}/map.json: {e}")

        try:
            with open(resourcepath+"/npcdata.json","r") as npcfile:
                content=npcfile.read()
                self.NPCDATA=loadJSON(content)
            self.log.info(f"Loaded NPC data successfully from {resourcepath}/npcdata.json")
        except Exception as e:
            self.log.error(f"Error loading NPC data from {resourcepath}/npcdata.json: {e}")

        try:
            with open(resourcepath+"/playerdata.json","r") as playerfile:
                content=playerfile.read()
                self.PLAYERDATA=loadJSON(content)
            self.log.info(f"Loaded player data successfully from {resourcepath}/playerdata.json")
        except Exception as e:
            self.log.error(f"Error loading player data from {resourcepath}/playerdata.json: {e}")
        try:
            with open(resourcepath+"/gamedata.json","r") as gamefile:
                content=gamefile.read()
                self.GAMEDATA=loadJSON(content)
            self.log.info(f"Loaded game data successfully from {resourcepath}/gamedata.json")
        except Exception as e:
            self.log.error(f"Error loading game data from {resourcepath}/gamedata.json: {e}")