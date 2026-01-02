from ex0.Card import Card
from ex0.CreatureCard import CreatureCard as CCard


class Deck():
    def __init__(self):
        self.cards_lst = []

    def add_card(self, card: Card) -> None:
        self.cards_lst.append(card)

    def remove_card(self, card_name: str) -> bool:
        for c in self.cards_lst:
            if c.name == card_name:
                self.cards_lst.remove(c)

    def shuffle(self) -> None:
        pass

    def draw_card(self) -> Card:
        pass

    def get_deck_stats(self) -> dict:
        total_cards = 0
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        for c in self.cards_lst:
            card = c.get_card_info()
            if card["type"] == "Creature":
                creatures += 1
            elif card["type"] == "Spell":
                spells += 1
            elif card["type"] == "Artifact":
                artifacts += 1
            total_cost += card["cost"]
            total_cards += 1

        deck_stats = {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": total_cost / total_cards
        }

        return deck_stats
