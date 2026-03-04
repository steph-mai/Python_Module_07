# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  SpellCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/03 16:10:52 by stmaire         #+#    #+#               #
#  Updated: 2026/03/04 14:36:43 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card, Card_Type
from typing import List, Dict, Any


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        valid_effects: List[str] = ["damage", "heal", "buff", "debuff"]
        if effect_type not in valid_effects:
            raise ValueError(
                'The effect type is not valid.'
                '(Valid effects are : '
                '"damage", "heal", "buff"and "debuff"'
                )
        self.effect_type = effect_type.lower()

    def get_card_info(self) -> dict[str, Any]:
        info: Dict[str, Any] = super().get_card_info()
        info["type"] = Card_Type.SPELL.value
        info["effect_type"] = self.effect_type
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

        effect_data = self.resolve_effect([])

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_data["effect"]
        }

    def resolve_effect(self, targets: list[Any]) -> dict[str, str]:
        if not isinstance(targets, list):
            targets = [targets]

        targets_names = [
            t.name if hasattr(t, "name")
            else str(t) for t in targets
            ]

        if len(targets_names) == 1:
            formatted_targets = "target"
        else:
            formatted_targets = (
                ", ".join(targets_names)
                if targets_names
                else "target"
            )

        return {
            "effect":
            f"Deal {self.cost} "
            f"{self.effect_type} to {formatted_targets}"
            }
