# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  AggressiveStrategy.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/05 13:33:30 by stmaire         #+#    #+#               #
#  Updated: 2026/03/05 17:15:36 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any
from ex0.Card import Card
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(
            self,
            hand: list[Card],
            battlefield: list[Any]
            ) -> dict[str, Any]:
        """
        Executes a game turn using an aggressive tactical approach.

        This strategy prioritizes playing as many cards as possible by sorting
        the hand by cost in ascending order. It calculates the total potential
        damage based on the attack power of the Creature cards
        played during the turn.
        """
        sorted_hand: list[Card] = sorted(hand, key=lambda card: card.cost)

        cards_played: list[str] = []
        damage_dealt: int = 0
        mana_used: int = 0

        for card in sorted_hand:
            cards_played.append(card.name)
            mana_used += card.cost

            if hasattr(card, 'attack'):
                damage_dealt += card.attack

        current_targets: list[Any] = battlefield
        prioritized = self.prioritize_targets(current_targets)
        targets_attacked = [prioritized[0]] if prioritized else []

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list[str]) -> list[str]:
        """
        Reorders the list of available targets based on aggressive priorities.

        This method ensures that the "Enemy Player" is moved to the top of
        the target list.
        """
        if not available_targets:
            return []

        targets: list[str] = list(available_targets)
        if "Enemy Player" in targets:
            targets.remove("Enemy Player")
            targets.insert(0, "Enemy Player")
        return targets
