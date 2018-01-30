print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("."*10) # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = '' at the end.  try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
# By default the print function adds a newline as the last character
# Which if written out would be end = '\n'
# If we want something other than a new line we need to specify it
# In this case we are specifying a space
# Which gets you the output Cheese Burger
# Instead of
# Cheese
# Burger
