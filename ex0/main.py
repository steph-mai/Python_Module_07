# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/03 12:17:14 by stmaire         #+#    #+#               #
#  Updated: 2026/03/04 14:22:16 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from typing import Any

if __name__ == "__main__":
    print("\n=== DataDeck Card Foundation ===\n")

    game_state: dict[str, Any] = {
        "available_mana": 6
    }

    print("Testing Abstract Base Class Design:")

    print("\nCreatureCard Info:")
    try:
        fire_dragon = CreatureCard(
            "Fire Dragon",
            5,
            Rarity.LEGENDARY.value,
            7,
            5
            )
        print(fire_dragon.get_card_info())

        print("\nPlaying Fire Dragon with 6 mana available:")
        print(f"Playable: {fire_dragon.is_playable(6)}")
        print(f"Play result: {fire_dragon.play(game_state)}")

        print("\nFire Dragon attacks Goblin Warrior:")
        print(f"Attack result: {fire_dragon.attack_target('Goblin Warrior')}")

        print("\nTesting insufficient mana (3 available):")
        print(f"Playable: {fire_dragon.is_playable(3)}")

        print("\nAbstract pattern successfully demonstrated!")

    except ValueError as e:
        print(e)
