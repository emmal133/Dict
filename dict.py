chipotle_items=[
    {
        "name": "chicken bowl",
        "price":12.10,
        "description": "grilled chicken, rice, and toppings"
    },
    {
        "name": "pollo asado bowl",
        "price": 12.70,
        "description": "grilled chicken + cilantro and lime, rice, and toppings"
    },
    {
        "name": "barbacoa bowl",
        "price": 14.10,
        "description": "shredded beef, rice, and toppings"
    },
    {
        "name": "steak bowl",
        "price": 14.10,
        "description": "grilled steak, rice, and toppings"
    },
    {
        "name": "veggie bowl",
        "price": 12.10,
        "description": "guacamole, rice, and toppings"
    },
    {
        "name": "carnitas bowl",
        "price": 12.85,
        "description": "grilled pork, rice, and toppings"
    },
    {
        "name": "sofritas bowl",
        "price": 12.85,
        "description": "grilled sofritas, rice, and toppings"
    }
]
def show_items(items):
    for index, item in enumerate(items):
        print(index, ":", item["name"])

def choose_item():
    show_items(chipotle_items)
    x = int(input("Which item number do you want to buy? "))
    print(chipotle_items[x]["name"])

choose_item()
