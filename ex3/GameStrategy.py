# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameStrategy.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/05 10:14:18 by stmaire         #+#    #+#               #
#  Updated: 2026/03/05 17:26:00 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from typing import Any
from ex0.Card import Card


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(
        self,
        hand: list[Card],
        battlefield: list[Any]
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list[str]) -> list[str]:
        pass
