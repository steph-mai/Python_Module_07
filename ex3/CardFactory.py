# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  CardFactory.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/05 10:32:23 by stmaire         #+#    #+#               #
#  Updated: 2026/03/05 17:15:53 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from typing import Any
from ex0.Card import Card


class CardFactory (ABC):
    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict[str, Any]:
        pass
