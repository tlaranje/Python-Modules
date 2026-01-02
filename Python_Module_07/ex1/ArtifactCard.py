from ex0.Card import Card
from ex0.Card import CardRarity, CardType

class ArtifactCard(Card):
    def __init__(self,
            name: str,
            cost: int,
            rarity: CardRarity,
            durability: int,
            effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = CardType.Artifact

    def get_card_info(self) -> dict:
        card_info = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.name,
            "durability": self.durability,
            "effect": self.effect,
            "type": self.type.name,
        }
        return card_info

    def play(self, game_state: dict) -> dict:
        pass

    def activate_ability(self) -> dict:
        pass