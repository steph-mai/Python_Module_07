# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Magical.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/04 14:45:44 by stmaire         #+#    #+#               #
#  Updated: 2026/03/04 14:58:35 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from typing import Any

class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list[str]) -> dict[str, Any]:
        pass
    
    @abstractmethod
    def channel_mana(self, amount: int) -> dict[str, Any]:
        pass
    
    @abstractmethod
    def get_magic_stats(self) -> dict[str, Any]:
        pass