# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/04 16:21:46 by stmaire         #+#    #+#               #
#  Updated: 2026/03/04 18:03:15 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex2.EliteCard import EliteCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Any

def get_methods(cls: Any) -> list[str]:
    return [method for method in dir(cls) if not method.startswith('_')]

def main() -> None:
    try: 
        warrior = EliteCard("Arcane Warrior", 5, "rare", 5, 3, "melee", 4)

        print("\n=== DataDeck Ability System ===\n")
        print("EliteCard capabilities:")
        print(f"- Card: {get_methods(Card)}")
        print(f"- Combatable: {get_methods(Combatable)}")
        print(f"- Magical: {get_methods(Magical)}")
        
        print(f"\nPlaying {warrior.name} (Elite Card):\n")
        
        print("Combat phase:")
        print(f"Attack result: {warrior.attack('Enemy')}")
        print(f"Defense result: {warrior.defend(5)}")
        
        print("\nMagic phase:")
        print(f"Spell cast: {warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
        print(f"Mana channel: {warrior.channel_mana(3)}")
        
        print("\nMultiple interface implementation successful!")
        
    except Exception as e:
        print (e)


if __name__ == "__main__":
    main()

