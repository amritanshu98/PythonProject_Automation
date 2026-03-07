def make_pizza(*topings):
    print(topings)
    for topin in topings:
        # print(topin)
        return topin


pramod = make_pizza("tomato")
# bhargava = make_pizza("Olives", "mushroom", "paneer")
# vinay = make_pizza("mushroom", "pineapple", "paneer", "sweetcorn")

print(pramod)
