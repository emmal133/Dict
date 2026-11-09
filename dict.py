chipotle_items=[
    {
        "name": "chicken bowl",
        "price":12.10,
        "description": "grilled chicken, rice, and toppings of your choice"
    },
    {
        "name": "pollo asado bowl",
        "price": 12.70,
        "description": "grilled chicken + cilantro and lime, rice, and toppings of your choice"
    },
    {
        "name": "barbacoa bowl",
        "price": 14.10,
        "description": "shredded beef, rice, and toppings of your choice"
    },
    {
        "name": "steak bowl",
        "price": 14.10,
        "description": "grilled steak, rice, and toppings of your choice"
    },
    {
        "name": "veggie bowl",
        "price": 12.10,
        "description": "guacamole, rice, and toppings of your choice"
    },
    {
        "name": "carnitas bowl",
        "price": 12.85,
        "description": "grilled pork, rice, and toppings of your choice"
    },
    {
        "name": "sofritas bowl",
        "price": 12.85,
        "description": "grilled sofritas, rice, and toppings of your choice"
    }
]
def show_items(items):
    for index, item in enumerate(items):
        print(index, ":", item["name"])

def choose_item():
    show_items(chipotle_items)
    x = int(input("Which item number do you want to buy? "))
    print(chipotle_items[x]["name"])
cart=[]
continue_shopping = input("Do you want to buy something? (yes/no): ")
while continue_shopping=="yes":
    choose_item()
    continue_shopping = input("Do you want to continue shopping? (yes/no): ")
if continue_shopping=="no":
    print(cart.append(continue_shopping))