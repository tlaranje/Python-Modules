
def print_inv_items(p_inv):
    inv_value = 0
    total_items = 0

    for item_type in ["weapon", "consumable", "armor"]:
        i = p_inv.get(item_type)
        count = i.get("count")
        value = i.get("value")

        print(f"{i.get('item')} ({item_type}, {i.get('rarity')}): "
              f"{count}x @ {value} gold each = {count * value} gold")

        inv_value += count * value
        total_items += count

    print(f"\nInventory value: {inv_value} gold")
    print(f"Item count: {total_items} items")
    print(f"Categories: weapon({p_inv.get('weapon').get('count')}), "
          f"consumable({p_inv.get('consumable').get('count')}), "
          f"armor({p_inv.get('armor').get('count')})")


def trans_items(p1, p2, item_type, trans_amount):
    print(f"\n=== Transaction: {p1.get('name')} gives {p2.get('name')} "
          f"{trans_amount} potions ===")

    item1 = p1.get(item_type)
    item2 = p2.get(item_type)

    if item1.get("count") < trans_amount:
        print("Transaction failed: not enough items!")
        return

    item1.update({"count": item1.get("count") - trans_amount})
    item2.update({"count": item2.get("count") + trans_amount})

    print("Transaction successful!\n")
    print("=== Updated Inventories ===")
    print(f"{p1.get('name')} {item1.get('item')}s: {item1.get('count')}")
    print(f"{p2.get('name')} {item2.get('item')}s: {item2.get('count')}")


def inv_analytics(p1, p2):
    print("\n=== Inventory Analytics ===")
    p1_value = 0
    p2_value = 0
    p1_items = 0
    p2_items = 0
    rarest_items = []

    for item_type in ["weapon", "consumable", "armor"]:
        i1 = p1.get(item_type)
        i2 = p2.get(item_type)

        p1_value += i1.get("count") * i1.get("value")
        p2_value += i2.get("count") * i2.get("value")

        p1_items += i1.get("count")
        p2_items += i2.get("count")

        if i1.get("rarity") == "rare":
            rarest_items.append(i1.get("item"))
        if i2.get("rarity") == "rare":
            rarest_items.append(i2.get("item"))

    if p1_value > p2_value:
        print(f"Most valuable player: {p1.get('name')} ({p1_value} gold)")
    elif p2_value > p1_value:
        print(f"Most valuable player: {p2.get('name')} ({p2_value} gold)")
    else:
        print(f"Most valuable player: Tie ({p1_value} gold each)")

    if p1_items > p2_items:
        print(f"Most items: {p1.get('name')} ({p1_items} items)")
    elif p2_items > p1_items:
        print(f"Most items: {p2.get('name')} ({p2_items} items)")
    else:
        print(f"Most items: Tie ({p1_items} items each)")

    print("Rarest items:", ", ".join(rarest_items))


if __name__ == "__main__":
    print("=== Player Inventory System ===\n")
    print("=== Alice's Inventory ===")

    alice_inv = dict(
        name="Alice",
        weapon=dict(item="sword", rarity="rare", count=1, value=500),
        consumable=dict(item="potion", rarity="common", count=5, value=50),
        armor=dict(item="shield", rarity="uncommon", count=1, value=200),)

    bob_inv = dict(
        name="Bob",
        weapon=dict(item="sword", rarity="common", count=1, value=500),
        consumable=dict(item="potion", rarity="common", count=0, value=50),
        armor=dict(item="magic_ring", rarity="rare", count=1, value=100),)

    print_inv_items(alice_inv)
    trans_items(alice_inv, bob_inv, "consumable", 2)
    inv_analytics(alice_inv, bob_inv)
