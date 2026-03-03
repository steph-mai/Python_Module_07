# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/03 17:25:22 by stmaire         #+#    #+#               #
#  Updated: 2026/03/03 18:03:11 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card_Type, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard


if __name__ == "__main__":
    game_state: dict = {
        "available_mana": 6
    }
    lightning_bolt = SpellCard("Lightning Bolt", 3, Rarity.COMMON, "damage")
    print(lightning_bolt.play(game_state))
    print(lightning_bolt.resolve_effect("Fire Dragon"))
    