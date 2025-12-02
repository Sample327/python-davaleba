import helpers
import random
import datetime as dt

def check_balance():
    print("checking balance")
    return random.choice((True, False))

def current_utc():
    return dt.datetime.now(dt.timezone.utc)

def complete_transaction():
    print("completing transaction ...")

# kwargsis nawili ver mivxvdi raunda meqna bonus davalebashi 

def place_order():
    if check_balance():
        complete_transaction()
        return {
            "order_id": random.randint(0,1000),
            "total": random.randint(500,1000),
            "status": "success"
        }
    return {
        "order_id": None,
        "total": None,
        "status": "failed"
    }


orders = [
    place_order(),
    place_order(),
    place_order(),
    place_order()
 ]

for order in orders:
    if order["status"] == "failed":
        print("check your balance")
    print(order)


print(helpers.square(9))
print(helpers.shift_and_square(5,1))


def safe_place_order(max_attempts=3):
    attempts = 0
    utc = current_utc()
    while attempts < max_attempts:
        attempts += 1
        print(f"\nattempt {attempts}")
        print(utc)
        order = place_order()
        if order["status"] == "success":
            print("order succed")
            return order
    print("all attempt failed")
    return None

result = safe_place_order(max_attempts=3)
print("\nfinal result :", result)


assert helpers.square(2) == 4
assert helpers.square(3) == 9

assert helpers.shift_and_square(4,5) == 81
assert helpers.shift_and_square(3,1) == 16

print("all tests succed")

# timestumpis logic ver mivxvdi yvela jerze rogor unda meqna

