import math
import datetime as dt
from random import randint as roll

PI_TWO_DECIMALS = round(math.pi, 2)

def current_utc():
    return dt.datetime.now(dt.timezone.utc)

def roll_dice(sides=6):
    return roll(1,sides)

print(f"pi two decimals: {PI_TWO_DECIMALS}")
print("\nCurrent utc: ", current_utc())
print("\nTwo dice rolls", roll_dice(), roll_dice())

#Write announce(event, *audiences, prefix="[INFO]") that formats a message similar to the example in workshop_7/arguments_examples.py.

# am nawils ver vxvdebi prefix info da ase shemdeg da dro tu iqneba ro axsna dzaan mokled .

def average_score(*scores):
    if not scores:                    
        raise ValueError("write at least one score")
    return round(sum(scores) / len(scores), 1)


