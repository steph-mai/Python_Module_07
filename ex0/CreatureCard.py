# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  CreatureCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/03 12:06:57 by stmaire         #+#    #+#               #
#  Updated: 2026/03/04 14:23:21 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card, Card_Type
from typing import Dict, Any


class CreatureCard (Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int
            ):
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health must be a positive integer")

        self.attack = attack
        self.health = health

    def get_card_info(self) -> dict[str, Any]:
        info: Dict[str, Any] = super().get_card_info()
        info["type"] = Card_Type.CREATURE.value
        info["attack"] = self.attack
        info["health"] = self.health
        return info

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        available_mana = game_state.get("available_mana", 0)

        if self.is_playable(available_mana) is True:
            game_state["available_mana"] -= self.cost
        else:
            return {
                "card_played": self.name,
                "status": "Failed",
                "reason": "Not enough mana"
            }

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: Any) -> dict[str, Any]:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
