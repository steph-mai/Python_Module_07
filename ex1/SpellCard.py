# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  SpellCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/03 16:10:52 by stmaire         #+#    #+#               #
#  Updated: 2026/03/03 18:03:56 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card, Card_Type
from typing import List, Dict

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)

        valid_effects: List = ["damage", "heal", "buff", "debuff"]
        if effect_type not in valid_effects:
            raise ValueError (
                f'The effect type is not valid.'
                f'(Valid effects are : '
                f'"damage", "heal", "buff"and "debuff"')
        self.effect_type = effect_type.lower()

    def get_card_info(self) -> dict:
        info: Dict = super().get_card_info()
        info["type"] = Card_Type.SPELL.value
        info["effect_type"] = self.effect_type
        return info

    def play(self, game_state: dict) -> dict:
        if "available_mana" in game_state:
            game_state["available_mana"] -= self.cost

        effect_description = f"Deal {self.cost} {self.effect_type} to target"
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_description
        }

    def resolve_effect(self, targets: list) -> dict:
        if isinstance(targets, str):
            targets = [targets]
        targets_names = [t.name if hasattr(t, "name") else str(t) for t in targets]
        if len(targets_names) == 1:
            formatted_targets = targets_names[0] 
        else:
            formatted_targets = ", ".join(targets_names) if targets_names else "target" 
        return {
                "effect": f"Deal {self.cost} {self.effect_type} to {formatted_targets}"
            }
    
    #TODO
    # def resolve_effect(self, targets: list) -> dict:
    #     # Sécurité pour les strings passées par erreur
    #     if isinstance(targets, str):
    #         targets = [targets]

    #     # Extraction des noms
    #     targets_names = [t.name if hasattr(t, "name") else str(t) for t in targets]
        
    #     # Si la liste est vide, on met "target" par défaut, sinon on joint
    #     formatted_targets = ", ".join(targets_names) if targets_names else "target"
            
    #     return {
    #         "effect": f"Deal {self.cost} {self.effect_type} to {formatted_targets}"
    #     }