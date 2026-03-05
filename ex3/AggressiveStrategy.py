# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  AggressiveStrategy.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/05 13:33:30 by stmaire         #+#    #+#               #
#  Updated: 2026/03/05 17:42:34 by stmaire         ###   ########.fr        #
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

        This strategy maximizes the number of actions
        by playing cards in ascending order of cost
        until the mana limit (10) is reached. It calculates the
        total damage dealt by summing the attack power
        of all creatures successfully played
        and identifies the priority target from the battlefield.
        """
        sorted_hand: list[Card] = sorted(hand, key=lambda card: card.cost)

        cards_played: list[str] = []
        damage_dealt: int = 0
        mana_used: int = 0
        mana_limit = 10

        for card in sorted_hand:
            if mana_used + card.cost <= mana_limit:
                cards_played.append(card.name)
                mana_used += card.cost
                if hasattr(card, 'attack'):
                    damage_dealt += card.attack
            else:
                break

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
