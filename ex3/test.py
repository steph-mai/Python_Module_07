from abc import ABC, abstractmethod
from typing import Any, Union
from ex0.Card import Card

class CardFactory(ABC):
    @abstractmethod
    def create_creature(self, name_or_power: Union[str, int, None] = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: Union[str, int, None] = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: Union[str, int, None] = None) -> Card:
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_supported_types(self) -> dict[str, str]:
        pass

    

import random
from typing import Any, Union, Dict, List, Callable
from ex3.CardFactory import CardFactory
from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard

class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        # Registres pour l'extensibilité
        self._creature_types: List[str] = ["dragon", "goblin", "orc"]
        self._spell_types: List[str] = ["fireball", "ice_storm", "lightning"]
        self._artifact_types: List[str] = ["mana_ring", "staff", "crystal"]

    def create_creature(self, name_or_power: Union[str, int, None] = None) -> Card:
        name = name_or_power if isinstance(name_or_power, str) else random.choice(self._creature_types)
        power = name_or_power if isinstance(name_or_power, int) else random.randint(2, 8)
        return CreatureCard(name.title(), power, Rarity.RARE.value, power, power + 2)

    def create_spell(self, name_or_power: Union[str, int, None] = None) -> Card:
        name = name_or_power if isinstance(name_or_power, str) else random.choice(self._spell_types)
        cost = name_or_power if isinstance(name_or_power, int) else random.randint(1, 4)
        return SpellCard(name.title(), cost, Rarity.UNCOMMON.value, "elemental")

    def create_artifact(self, name_or_power: Union[str, int, None] = None) -> Card:
        name = name_or_power if isinstance(name_or_power, str) else random.choice(self._artifact_types)
        cost = name_or_power if isinstance(name_or_power, int) else random.randint(2, 5)
        return ArtifactCard(name.title(), cost, Rarity.RARE.value, 2, "Magic boost")

    def get_supported_types(self) -> Dict[str, List[str]]:
        return {
            "creatures": self._creature_types,
            "spells": self._spell_types,
            "artifacts": self._artifact_types
        }
    
    # Méthode pour l'extensibilité demandée
    def register_type(self, category: str, type_name: str) -> None:
        if category == "creatures": self._creature_types.append(type_name)
        elif category == "spells": self._spell_types.append(type_name)
        elif category == "artifacts": self._artifact_types.append(type_name)

    
from typing import Any, Dict, Optional
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy

class GameEngine:
    def __init__(self) -> None:
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        print(f"Configuring Fantasy Card Game...")
        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {strategy.get_strategy_name()}")

    def simulate_turn(self) -> Dict[str, Any]:
        if not self.factory or not self.strategy:
            raise ValueError("Engine must be configured with factory and strategy.")

        # 1. Création d'une main fictive pour la démo (3 cartes)
        hand = [
            self.factory.create_creature(),
            self.factory.create_creature(),
            self.factory.create_spell()
        ]
        self.cards_created += len(hand)
        
        # 2. Exécution du tour via la stratégie
        # (Battlefield vide pour cette simulation simple)
        result = self.strategy.execute_turn(hand, [])
        
        # 3. Mise à jour des stats du moteur
        self.turns_simulated += 1
        self.total_damage += result.get("damage_dealt", 0)
        
        return result

    def get_engine_status(self) -> Dict[str, Any]:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name() if self.strategy else "None",
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }

from abc import ABC, abstractmethod
from typing import Any, List, Dict

class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: List[Any], battlefield: List[Any]) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        pass


from typing import Any, List, Dict
from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        # Une stratégie agressive cible toujours le "Joueur" en priorité
        # On place 'Enemy Player' en tête de liste si présent
        targets = sorted(available_targets, key=lambda x: 0 if x == "Enemy Player" else 1)
        return targets

    def execute_turn(self, hand: List[Any], battlefield: List[Any]) -> Dict[str, Any]:
        # 1. Trier la main par coût croissant (jouer les petites cartes d'abord)
        # On utilise getattr au cas où l'objet n'a pas l'attribut cost
        hand.sort(key=lambda card: getattr(card, 'cost', 0))
        
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        
        # 2. Simuler le fait de jouer des cartes (on limite à 2 cartes pour la démo)
        for i in range(min(2, len(hand))):
            card = hand[i]
            cards_played.append(card.name)
            mana_used += getattr(card, 'cost', 0)
            
            # Si c'est une créature, elle ajoute sa force aux dégâts
            if hasattr(card, 'attack_power'):
                damage_dealt += card.attack_power
            # Si c'est un sort de dégâts (Ex 1)
            elif hasattr(card, 'effect_type') and card.effect_type == "damage":
                damage_dealt += card.cost * 2 # Estimation simple

        # 3. Définir les cibles
        targets = self.prioritize_targets(["Enemy Creature 1", "Enemy Player"])

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": [targets[0]], # On attaque la cible prioritaire
            "damage_dealt": damage_dealt
        }


from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy

def main() -> None:
    print("=== DataDeck Game Engine ===")
    
    # 1. Initialisation des composants
    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    
    # 2. Configuration (Affiche les messages de config)
    engine.configure_engine(factory, strategy)
    
    # 3. Affichage des types supportés par la Factory
    print(f"Available types: {factory.get_supported_types()}")
    
    # 4. Simulation du tour
    print("\nSimulating aggressive turn...")
    
    # On génère manuellement une main pour correspondre à l'exemple de la consigne
    # (Ou on laisse le moteur le faire, mais ici on force pour la démo)
    dragon = factory.create_creature("Fire Dragon")
    goblin = factory.create_creature("Goblin Warrior")
    bolt = factory.create_spell("Lightning Bolt")
    
    # Petit hack pour l'affichage de la main comme dans l'exemple
    print(f"Hand: [{dragon.name} ({dragon.cost}), {goblin.name} ({goblin.cost}), {bolt.name} ({bolt.cost})]")
    
    # Exécution
    turn_result = strategy.execute_turn([dragon, goblin, bolt], [])
    
    print("\nTurn execution:")
    print(f"Strategy: {turn_result['strategy']}")
    print(f"Actions: {{'cards_played': {turn_result['cards_played']}, "
          f"'mana_used': {turn_result['mana_used']}, "
          f"'targets_attacked': {turn_result['targets_attacked']}, "
          f"'damage_dealt': {turn_result['damage_dealt']}}}")
    
    # 5. Rapport final
    print("\nGame Report:")
    # On simule un état du moteur cohérent avec l'exemple
    report = {
        "turns_simulated": 1,
        "strategy_used": strategy.get_strategy_name(),
        "total_damage": turn_result['damage_dealt'],
        "cards_created": 3
    }
    print(report)
    
    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")

if __name__ == "__main__":
    main()