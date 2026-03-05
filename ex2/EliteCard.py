# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  EliteCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/04 14:46:23 by stmaire         #+#    #+#               #
#  Updated: 2026/03/04 17:59:20 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import List, Dict, Any
from enum import Enum
from random import randint


class CombatTypes(Enum):
    MELEE = "melee"
    HAND_TO_HAND = "hand-to-hand"
    
class MagicSpells(Enum):
    FIREBALL = ("fireball", 4)
    SHIELD = ("shield", 3)
    HEAL = ("heal", 2)
    
    def __init__(self, spell_name: str, mana_to_use: int) -> None:
        self.spell_name = spell_name
        self.mana_to_use = mana_to_use


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack_power: int, defense_capacity: int, combat_type: str, mana_pool: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.mana_pool = mana_pool
        self.defense_capacity = defense_capacity
        self.combat_type = combat_type
        
    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        available_mana = game_state.get("available_mana", 0)
        if self.is_playable(available_mana) is True:
            game_state["available_mana"] -= self.cost
            return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }
        else:
            return {
                "card_played": self.name,
                "status": "Failed",
                "reason": "Not enough mana"
            }

    def attack(self, target: Any) -> dict[str, Any]:
        if self.combat_type.lower() not in [t.value for t in CombatTypes]:
                raise AttributeError('Invalid combat type: Valid types are "melee" and "hand-to-hand"')
        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self.attack_power,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        block_roll = randint(0, self.defense_capacity)
        damage_taken = max(0, incoming_damage - block_roll)
        if damage_taken < 10:
            still_alive = True
        else:
            still_alive = False

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": block_roll,
            "still_alive": still_alive
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {"attack": self.attack_power, "defense": self.defense_capacity}

    def cast_spell(
            self,
            spell_name: str,
            targets: List[Any]
            ) -> Dict[str, Any]:

        mana_to_use = 0

        for spell in MagicSpells:
            if spell_name.lower() == spell.spell_name:
                mana_to_use += spell.mana_to_use
                break

        if mana_to_use == 0:
            raise AttributeError("This spell doesn't exist. "
                                 "Valid spells are 'heal', "
                                 "'shield' and 'fireball'")
                                 
        self.mana_pool -= mana_to_use
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_to_use
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        self.mana_pool += amount
        return {"channeled": amount, "total_mana": self.mana_pool}

    def get_magic_stats(self) -> Dict[str, Any]:
        return {"mana_pool": self.mana_pool}
