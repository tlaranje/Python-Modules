from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard as CCard
from ex1.ArtifactCard import ArtifactCard as ACard
from ex1.SpellCard import SpellCard as SCard
from ex0.Card import CardRarity, EffectType

if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===\n")

    deck = Deck()
    print("Building deck with different card types...")
    dragon = CCard(
        "Fire Dragon", 4, CardRarity.Legendary, 7, 5)
    spell = SCard(
        "Lightning Bolt", 4, CardRarity.Common, EffectType.Damage)
    artifact = ACard(
        "Mana Crystal", 4, CardRarity.Common, 5, "Permanent: +1 mana per turn")
    deck.add_card(dragon)
    deck.add_card(spell)
    deck.add_card(artifact)
    print(deck.get_deck_stats())
