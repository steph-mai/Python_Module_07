# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ArtifactCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/04 09:21:42 by stmaire         #+#    #+#               #
#  Updated: 2026/03/04 14:25:25 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card, Card_Type
from typing import Any


class ArtifactCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            durability: int,
            effect: str
            ):
        super().__init__(name, cost, rarity)

        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("Durability must be a positive integer")
        if not isinstance(effect, str) or len(effect.strip()) == 0:
            raise ValueError("Effect parameter can't be an empty string")

        self.durability = durability
        self.effect = effect

    def get_card_info(self) -> dict[str, Any]:
        info: dict[str, Any] = super().get_card_info()
        info["type"] = Card_Type.ARTIFACT.value
        info["durability"] = self.durability
        info["effect"] = self.effect
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
            "effect": self.effect
        }

    def activate_ability(self) -> dict[str, str | int]:
        if self.durability <= 0:
            raise ValueError(f"{self.name} has no durability left!")

        self.durability -= 1

        return {
            "effect_resolved": self.effect,
            "durability_left": self.durability
        }
