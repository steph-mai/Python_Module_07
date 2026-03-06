# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/05 15:18:16 by stmaire         #+#    #+#               #
#  Updated: 2026/03/06 15:12:13 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


if __name__ == "__main__":
    print("\n=== DataDeck Game Engine ===\n")
    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Configuring Fantasy Card Game...")
    try:
        engine.configure_engine(factory, strategy)

        status = engine.get_engine_status()
        print(f"Factory: {type(factory).__name__}")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"Available types: {factory.get_supported_types()}")

        print("\nSimulating aggressive turn...")
        turn_actions = engine.simulate_turn()

        print("\nTurn execution:")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"Actions: {turn_actions}")

        print("\nGame Report:")
        print(engine.get_engine_status())
    except Exception as e:
        print(e)

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")
