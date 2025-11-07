import copy
import csv
import random
from typing import List


def check_equal(l1: List[str], l2: List[str]):
    """Checks if two lists contain the same elements, regardless of order."""
    return len(l1) == len(l2) and sorted(l1) == sorted(l2)


if __name__ == '__main__':
    # This list is our master list
    participants = ['Ida', 'Malene', 'Rasmus', 'Mor', 'Far', 'Bettina', 'Michael', 'Jesper', 'Katrine', 'Rikke']

    # The givers list will stay in its original order
    givers = copy.copy(participants)

    # The receivers list is a copy that we will shuffle
    receivers = copy.copy(participants)

    # Keep shuffling the receivers list until no one has themselves
    while True:
        print("Shuffling list...")
        random.shuffle(receivers)

        # Assume the list is good until we find a problem
        is_valid = True

        # Check each pair
        for giver, receiver in zip(givers, receivers):
            if giver == receiver:
                is_valid = False  # Found a self-gift!
                break  # Stop checking, we need to re-shuffle

        # If the loop finished without finding a self-gift, we're done
        if is_valid:
            print("Found a valid pairing!")
            break

    # --- Your original code from here is great ---

    # Assert that the lists still contain the same people
    assert check_equal(givers, receivers)

    # Create the final pairs
    pairs = list(zip(givers, receivers))

    print("\n🎄 Julegaveparringer: 🎄")
    for giver, receiver in pairs:
        print(f"{giver} -> {receiver}")

    # Write to CSV
    # Added newline='' which is recommended for CSVs
    # Added a header row for clarity
    with open('julegaver.csv', 'w') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['Giver', 'Modtager'])  # Header row
        for row in pairs:
            csv_out.writerow(row)

    print("\nSuccessfully saved pairs to 'julegaver.csv'")