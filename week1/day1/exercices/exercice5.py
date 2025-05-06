my_fav_numbers = {1, 2, 3, 4, 5}
my_fav_numbers.add(6)
my_fav_numbers.add(7)
my_fav_numbers.remove(7)

friend_fav_numbers = {8, 9, 10, 11, 12}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)