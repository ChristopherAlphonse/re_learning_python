# Problem 1: Counting Treasure
# Captain Blackbeard has a treasure map with several clues that point to different locations on an island. Each clue is associated with a specific location and the number of treasures buried there. Given a dictionary treasure_map where keys are location names and values are integers representing the number of treasures buried at those locations, write a function total_treasures() that returns the total number of treasures buried on the island.


import unittest


def total_treasure(treasure_map):

    total = 0
    for items in treasure_map.values():
        if isinstance(items, int):
            total += int(items)
        else:
            return
    return total


class TestTotalTreasure(unittest.TestCase):

    def test_total_treasure_valid(self):
        treasure_map1 = {
            "Cove": 3,
            "Beach": 7,
            "Forest": 5
        }
        self.assertEqual(total_treasure(treasure_map1), 15)

        treasure_map2 = {
            "Shipwreck": 10,
            "Cave": 20,
            "Lagoon": 15,
            "Island Peak": 5
        }
        self.assertEqual(total_treasure(treasure_map2), 50)

    def test_total_treasure_empty(self):
        treasure_map = {}
        self.assertEqual(total_treasure(treasure_map), 0)


if __name__ == "__main__":
    unittest.main()
