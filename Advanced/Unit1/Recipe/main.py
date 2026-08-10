# Recipe: name, ingredients, cooking time, cooking instructions.

class Recipe:
    def __init__(self, name, ingredients, time, instructions):
        self.name=name
        self.ingredients=ingredients
        self.time=time
        self.instructions=instructions

    def display(self):
        print("Recipe: ",self.name)
        print("---------------------")
        print("Ingredients:","\n-".join(self.ingredients))
        print("Cooking Time: ",self.time)
        print("Cooking Instructions:", "\n-".join(self.instructions))

recipe=Recipe(input("Enter the recipe name: "), input("Enter the reipe ingredients (-comma-seperated): ").split(", "), input("Enter cooking time: "), input("Enter the cooking instructions (-comma-seperated): ").split(", "))

print("Recipe Added Successfully!")
recipe.display()