# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/03 17:25:22 by stmaire         #+#    #+#               #
#  Updated: 2026/03/04 14:40:15 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from typing import Any


if __name__ == "__main__":

    game_state: dict[str, Any] = {
        "available_mana": 30
    }

    print("\n=== DataDeck Deck Builder ===\n")

    try:
        print("Building deck with different card types...")
        lightning_bolt = SpellCard(
            "Lightning Bolt",
            3,
            "common",
            "damage"
            )
        mana_crystal = ArtifactCard(
            "Mana Crystal",
            2,
            "common",
            3,
            "Permanent: +1 mana per turn"
            )
        fire_dragon = CreatureCard(
            "Fire Dragon",
            5,
            "legendary",
            6,
            3
            )

        my_deck: Deck = Deck()

        my_deck.add_card(lightning_bolt)
        my_deck.add_card(mana_crystal)
        my_deck.add_card(fire_dragon)

        print(f"Deck stats: {my_deck.get_deck_stats()}")

        print("\nDrawing and playing cards:\n")

        while len(my_deck.cards) > 0:
            card = my_deck.draw_card()
            info = card.get_card_info()
            print(f"Drew: {card.name} ({info['type']})")
            print(f"Play result: {card.play(game_state)}\n")

        print("Polymorphism in action: "
              "Same interface, different card behaviors!")
    except Exception as e:
        print(e)
