# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentPlatform.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/06 11:02:05 by stmaire         #+#    #+#               #
#  Updated: 2026/03/06 15:29:39 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any
from ex4.TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self) -> None:
        self.registry: dict[str, TournamentCard] = {}
        self.total_matches = 0

    def register_card(self, card: TournamentCard) -> str:
        self.registry[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict[str, Any]:
        c1: TournamentCard | None = self.registry.get(card1_id)
        c2: TournamentCard | None = self.registry.get(card2_id)

        if not c1 or not c2:
            missing: str = card1_id if not c1 else card2_id
            raise KeyError(f"Card {missing} doesn't exist in registry.")

        if c1.attack_power >= c2.defense_capacity:
            winner, loser = c1, c2
        else:
            winner, loser = c2, c1
        winner.update_wins(1)
        loser.update_losses(1)
        self.total_matches += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> list[TournamentCard]:
        return sorted(
            self.registry.values(),
            key=lambda player: player.calculate_rating(),
            reverse=True
            )

    def generate_tournament_report(self) -> dict[str, Any]:
        total_cards = len(self.registry)
        all_ratings = [c.calculate_rating() for c in self.registry.values()]
        avg_rating = sum(all_ratings) // total_cards if total_cards != 0 else 0
        return {
            "total_cards": total_cards,
            "matches_played": self.total_matches,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
