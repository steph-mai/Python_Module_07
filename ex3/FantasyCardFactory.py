# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  FantasyCardFactory.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/05 10:41:25 by stmaire         #+#    #+#               #
#  Updated: 2026/03/05 17:19:24 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import List, Any
import random
from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creatures_types: list[str] = [
            'dragon', 'goblin', 'orc warrior', 'elf archer',
            'undead skeleton', 'ancient troll', 'phoenix'
        ]
        self.spells_types: list[str] = [
            'fireball', 'ice storm', 'lightning bolt',
            'meteor strike', 'frost nova', 'chain lightning'
        ]
        self.artifacts_types: list[str] = [
            'mana ring', 'staff', 'crystal', 'amulet of power',
            'ancient grimoire', 'sacred relic'
        ]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        name = random.choice(self.creatures_types)
        power = random.randint(2, 8)

        if isinstance(name_or_power, str):
            if name_or_power.strip() != "":
                name = name_or_power

        elif isinstance(name_or_power, int):
            if 1 <= name_or_power <= 7:
                power = name_or_power

        random_rarity = random.choice(list(Rarity))

        return CreatureCard(
            name=name.title(),
            cost=power // 2,
            rarity=random_rarity.value,
            attack=power,
            health=power + 2
            )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        name = random.choice(self.spells_types)
        power = random.randint(2, 8)

        if isinstance(name_or_power, str):
            if name_or_power.strip() != "":
                name = name_or_power

        elif isinstance(name_or_power, int):
            if 1 <= name_or_power <= 7:
                power = name_or_power

        random_rarity = random.choice(list(Rarity))

        return SpellCard(
            name=name.title(),
            cost=power,
            rarity=random_rarity.value,
            effect_type=random.choice(["damage", "heal", "buff", "debuff"])
            )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        name = random.choice(self.artifacts_types)
        power = random.randint(1, 5)

        if isinstance(name_or_power, str):
            if name_or_power.strip() != "":
                name = name_or_power

        elif isinstance(name_or_power, int):
            if 1 <= name_or_power <= 4:
                power = name_or_power

        random_rarity = random.choice(list(Rarity))
        random_durability = random.randint(1, 7)

        possible_effects = [
            f"Increases attack by {power}",
            f"Reduces spell cost by {power // 2 + 1}",
            f"Adds {power} mana points per turn",
            "Provides a protective shield"
        ]

        random_effect = random.choice(possible_effects)

        return ArtifactCard(
            name=name.title(),
            cost=power,
            rarity=random_rarity.value,
            durability=random_durability,
            effect=random_effect
            )

    def create_themed_deck(self, size: int) -> dict[str, Any]:
        """Create a random deck with 'size' cards"""
        themed_deck: List[Card] = []
        if size < 0:
            raise ValueError("Size must be a positive integer")
        for _ in range(size):
            method = random.choice([
                self.create_creature,
                self.create_spell,
                self.create_artifact
                ])
            themed_deck.append(method())

        return {
            "deck_name": "Fantasy deck",
            "deck_cards": themed_deck,
            "size": size
            }

    def get_supported_types(self) -> dict[str, list[str]]:
        """Return all valid types of creatures, spells and artifacts"""
        return {
            "creatures": self.creatures_types,
            "spells": self.spells_types,
            "artifacts": self.artifacts_types
        }
