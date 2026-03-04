# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Card.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/03 12:02:55 by stmaire         #+#    #+#               #
#  Updated: 2026/03/04 14:22:58 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card_Type(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"


class Card (ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("The card name is not valid")
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("Cost must be a positive integer")

        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        pass

    def get_card_info(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
