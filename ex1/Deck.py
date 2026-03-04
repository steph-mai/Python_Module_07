# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Deck.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/04 10:25:43 by stmaire         #+#    #+#               #
#  Updated: 2026/03/04 14:27:52 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from typing import List, Any
import random


class Deck():
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError(f"Expected a Card object, "
                            f"got {type(card).__name__}")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("The deck is empty. You can't draw a card")

        return self.cards.pop(0)

    def get_deck_stats(self) -> dict[str, Any]:
        stats = {
            "total_cards": len(self.cards),
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
            "avg_cost": 0.0
        }
        if stats["total_cards"] == 0:
            return stats

        total_cost = 0

        for card in self.cards:

            total_cost += card.cost

            if isinstance(card, CreatureCard):
                stats["creatures"] += 1
            if isinstance(card, SpellCard):
                stats["spells"] += 1
            if isinstance(card, ArtifactCard):
                stats["artifacts"] += 1

        stats["avg_cost"] = round(total_cost / stats["total_cards"], 1)

        return stats
