print("Hey There!")

import random

def random_number(min_value, max_value):
    """Generate a random number between min_value and max_value."""
    return random.randint(min_value, max_value)         

random_num = random_number(1, 100)
print(f"Random number generated: {random_num}")