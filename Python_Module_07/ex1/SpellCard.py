from ex0.Card import Card
from ex0.Card import CardRarity, CardType, EffectType

class SpellCard(Card):
    def __init__(self,
            name: str,
            cost: int,
            rarity: CardRarity,
            effect_type: EffectType) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = CardType.Spell

    def get_card_info(self) -> dict:
        card_info = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.name,
            "effect_type": self.effect_type,
            "type": self.type.name,
        }
        return card_info

    def play(self, game_state: dict) -> dict:
        pass

    def resolve_effect(self, targets: list) -> dict:
        pass