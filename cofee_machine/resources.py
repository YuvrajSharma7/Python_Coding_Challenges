RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def refill_resources():
    """Refill resources to default values"""
    RESOURCES["water"] = 300
    RESOURCES["milk"] = 200
    RESOURCES["coffee"] = 100
    print("Refilled resources")