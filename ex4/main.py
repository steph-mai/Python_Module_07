# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/06 13:35:08 by stmaire         #+#    #+#               #
#  Updated: 2026/03/06 15:24:28 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


if __name__ == "__main__":
    print("\n=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")
    tournament = TournamentPlatform()

    fire_dragon = TournamentCard(
        "Fire Dragon",
        4,
        "rare",
        7,
        4,
        "dragon_001",
        1200)
    ice_wizard = TournamentCard(
        "Ice Wizard",
        3,
        "common",
        2,
        3,
        "wizard_001",
        1150
        )
    cards: list[TournamentCard] = [fire_dragon, ice_wizard]
    try:
        fire_dragon_id = tournament.register_card(fire_dragon)
        ice_wizard_id = tournament.register_card(ice_wizard)

        for card in cards:
            print(f"{card.name} (ID: {card.card_id}):")
            interfaces = [cls.__name__ for cls in card.__class__.__bases__]
            interfaces_str = ", ".join(interfaces)
            print(f"- Interfaces: [{interfaces_str}]")
            card_info = card.get_rank_info()
            print(f"- Rating: {card.base_rating}")
            print(f"- Record: {card_info['record']}\n")

        print("Creating tournament match...")
        result = tournament.create_match("dragon_001", "wizard_001")
        print(f"Match result: {result}")

        print("\nTournament Leaderboard:")
        leaderboard = tournament.get_leaderboard()
        for i, card in enumerate(leaderboard, 1):
            stats = card.get_tournament_stats()
            print(f"{i}. {stats['name']} "
                  f"- Rating: {stats['rating']} ({stats['record']})")

        print("\nPlatform Report:")
        print(tournament.generate_tournament_report())

        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except Exception as e:
        print(e)
