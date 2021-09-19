shopping_list = ["milk", "eggs", "bread", "rice"]

item_to_find = input("Item to find: ").casefold()  # input item to find
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index + 1
        print(f"{item_to_find} found at position {found_at}")
        break
else:
    print(f"{item_to_find} not in List")
