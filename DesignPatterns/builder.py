class Burger:
    def __init__(self):
        self.ingredients = []

    def __str__(self):
        return f"Burger with {', '.join(self.ingredients)}"

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_patty(self):
        self.burger.ingredients.append("patty")
        return self

    def add_cheese(self):
        self.burger.ingredients.append("cheese")
        return self

    def add_lettuce(self):
        self.burger.ingredients.append("lettuce")
        return self

    def build(self):
        return self.burger

# Usage
builder = BurgerBuilder()
burger = builder.add_patty().add_cheese().add_lettuce().build()
print(burger)  # Burger with patty, cheese, lettuce
