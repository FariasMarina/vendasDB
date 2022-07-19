from time import sleep
from PIL import Image
from time import sleep

print("What you want: (1)Chocolate Cake ")
choice = int(input(":"))

trigo = Image.open("trigos.jpeg")
trigo.load()
trigo.show()
trigo.close()
sleep(1)

if choice == 1:
    CakeDough = ["3 cups of wheat", "2 cups of sugar", "1 cup of powdered chocolate",
             "1 glass of oil", "3 eggs", "1 cup of hot water",
             "1 tablespoon of baking powder"]

    Cover = ["3 spoons of margarine", "4 spoons of chocolate powder", "4 spoons of sugar",
            "3 cups of milk"]

    Make_cakedough = ["In a bowl, mix the sugar and cocoa powder","Then mix the egg yolks and the oil",
        "Gradually add the water and wheat.",
        "Then add the yeast and finally add the snow whites",
        "Pour into a greased shape and bake for approximately 40 minutes"]

    MakeCover = ["Mix everything in a pan over low heat",
        "Don't stop stirring until it's creamy",
        "Then pour over the still warm cake."]

    print(30*"~=")
    print("Ingredients for to make a cake dough")
    for i in CakeDough:
        sleep(1)
        print(i)

    sleep(1)
    print(30*"~=")
    print("Ingredients for to make a Cover")
    for j in Cover:
        sleep(1)
        print(j)

    sleep(1)
    print(30*"~=")
    for k in Make_cakedough:
        sleep(1)
        print(k)

    sleep(1)
    print(30*"~=")
    for l in MakeCover:
        sleep(1)
        print(l)
    print(30*"~=")
else:
    print("ERROR")

