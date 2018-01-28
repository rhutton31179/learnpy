print("I will now count my chickens:")

print("Hens", 25 + 30 / 6) # This should = 30
print("Roosters", 100 - 25 * 3 % 4) # This should equal 97

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6) # This should equal 7 in python2
# Because of the way that python2 handles numbers, 1/4 = 0.  If you
# replace either number with a floating point number (1.0 or 4.0)
# then you get 6.75 as python2 will properly handle the result as a
# floating point number

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7) # This is a boolean and shoulb be False

print("What is 3 + 2?", 3 + 2) # This is 5
print("what is 5 - 7?", 5 - 7) # This is -2

print("Oh, that's why its False.")

print("How about some more.")

print("Is it greater?", 5 > 2) # This is True
print("Is it greater or equal?"), 5 >= -2 # This is True
print("Is it less or equal?", 5 <= -2) #This is False
