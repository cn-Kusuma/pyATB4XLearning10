my_shopping_list = ["bread", "milk", "butter"]

print(my_shopping_list[0])
print(len(my_shopping_list))


def bring_more_food(My_list):
    more_item = input("Enter the item")
    my_shopping_list.append(more_item)

    return my_shopping_list