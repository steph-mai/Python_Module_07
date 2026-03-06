# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentCard.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/06 09:17:09 by stmaire         #+#    #+#               #
#  Updated: 2026/03/06 15:28:20 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack_power: int,
            defense_capacity: int,
            card_id: str, base_rating: int
            ) -> None:

        if not isinstance(attack_power, int) or attack_power < 0:
            raise ValueError("Attack must be a positive integer.")
        if not isinstance(defense_capacity, int) or defense_capacity < 0:
            raise ValueError("Defense must be a positive integer.")
        if not isinstance(base_rating, int) or base_rating < 0:
            raise ValueError("Base rating must be a positive integer.")
        if not isinstance(card_id, str) or not card_id.strip():
            raise ValueError("Card ID is not valid.")

        Card.__init__(self, name, cost, rarity)
        self.attack_power = attack_power
        self.defense_capacity = defense_capacity
        self.card_id = card_id
        self.base_rating = base_rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        card_name = game_state.get("name", self.name)
        return {"action": "played", "card": card_name}

    def attack(self, target: Any) -> dict[str, Any]:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power
            }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        if incoming_damage < 0:
            incoming_damage = 0
        if incoming_damage > self.defense_capacity:
            absorbed = self.defense_capacity
        else:
            absorbed = incoming_damage

        return {
            "defender": self.name,
            "incoming_damage": incoming_damage,
            "absorbed": absorbed
            }

    def get_combat_stats(self) -> dict[str, Any]:
        return {"attack": self.attack_power, "defense": self.defense_capacity}

    def calculate_rating(self) -> int:
        result = self.base_rating + self.wins * 16 - self.losses * 16
        return max(0, result)

    def update_wins(self, wins: int) -> None:
        if not isinstance(wins, int) or wins < 0:
            raise ValueError("wins must be a positive integer.")
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        if not isinstance(losses, int) or losses < 0:
            raise ValueError("losses must be a positive integer.")
        self.losses += losses

    def get_rank_info(self) -> dict[str, Any]:
        return {
            "rating": self.calculate_rating(),
            "record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> dict[str, Any]:
        stats = self.get_rank_info()
        stats["name"] = self.name
        return stats
