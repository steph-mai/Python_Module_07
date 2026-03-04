# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Combatable.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/04 14:45:02 by stmaire         #+#    #+#               #
#  Updated: 2026/03/04 17:57:42 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from typing import Any


class Combatable(ABC):
    @abstractmethod
    def attack(self, target: Any) -> dict[str, Any]:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict[str, Any]:
        pass
