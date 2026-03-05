# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameEngine.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/05 14:41:43 by stmaire         #+#    #+#               #
#  Updated: 2026/03/05 17:25:10 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory
        self.strategy: GameStrategy
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(
            self,
            factory: CardFactory,
            strategy: GameStrategy
            ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict[str, Any]:
        if self.factory is None or self.strategy is None:
            raise ValueError(
                "The game engine needs a valid factory and a valid strategy"
                )

        num_cards = 3

        deck = self.factory.create_themed_deck(num_cards)
        hand = deck["deck_cards"]
        self.cards_created += num_cards

        hand_display = [f"{card.name} ({card.cost})" for card in hand]
        print(f'Hand: [{", ".join(hand_display)}]')

        battlefield = ["Enemy Player", "Goblin Minion"]
        result = self.strategy.execute_turn(hand, battlefield)

        self.turns_simulated += 1

        self.total_damage += result["damage_dealt"]

        return result

    def get_engine_status(self) -> dict[str, Any]:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": (
                self.strategy.get_strategy_name()
                if self.strategy else "None"
            ),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
