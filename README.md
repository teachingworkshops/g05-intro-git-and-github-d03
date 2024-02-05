# Text-Based Dungeon Game

## Overview

Text-Based Dungeon Game is a simple text-based adventure game where players explore a dungeon, encountering and fighting enemies, collecting items, and navigating through various rooms to escape. The player must collect a key in order to open the final door and escape.

## Classes Overview

### Room Class

* Attributes:
  * north, east, south, west: References to neighboring rooms.
  * enemy: Reference to an enemy in the room.
  * item: Reference to an item in the room.
  * description: Description of the room.
  * isDark: Boolean indicating if the room is dark.
  * isDoor: Boolean indicating if the room has a door.

### Player Class

* Attributes:
  * name: Player's name.
  * current\_room: Reference to the current room.
  * inventory: List of items in the player's inventory.
  * max\_inventory\_slots: Maximum number of slots in the inventory.
  * health: Player's health.

### Enemy Class

* Attributes:
  * name: Name of the enemy.
  * description: Description of the enemy.

### Item Class

* Attributes:
  * description: Description of the item.
