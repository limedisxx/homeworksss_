# Работа со списками
my_list = ["banana", "strawberry", "coconut", "cucumber", "tomato"]
print("List:", my_list)

print("First element:", my_list[0])
print("Last element:", my_list[-1])

print("Sublist:", my_list[2:5])

my_list = ["banana", "strawberry", "coconut", "cucumber", "tomato"]
my_list[2] = "cherry"
print("Modified List:", my_list)



# Работа со словарём
my_dict = {{'apple': "яблоко", 'banana': "банан", 'orange': "апельсин"}}
print("Dictionary:", my_dict)
print(my_dict['orange'])
my_dict.update({'kiwi': 'киви'})
print(my_dict)