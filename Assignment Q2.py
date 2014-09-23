#Sam Wade
#Assignment Q2
total_weight = int(input("Please enter total weight as a whole number"))

one_hundered = total_weight // 100
one_hundered_remainder = total_weight %100

fifty = one_hundered_remainder // 50
fifty_remainder = one_hundered_remainder % 50


ten = fifty_remainder // 10
ten_remainder = fifty_remainder % 10

five = ten_remainder // 5
five_remainder = ten_remainder % 5

two = five_remainder // 2
two_remainder = five_remainder % 2

one = two_remainder // 1


print("you will need {0} 100g weights, {1} 50g weights, {2} 10g weigts, {3} 5g weights, {4} 2g weights, {5} 1g weights.".format(one_hundered, fifty,ten, five, two, one))

