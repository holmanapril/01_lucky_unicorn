greeting = "Welcome to the Lucky Unicorn Game"
sides = "*" * 3

greeting = "{} {} {}".format(sides, greeting, sides)

top_bottom = "*" * len(greeting)

print(top_bottom)
print(greeting)
print(top_bottom)


unicorn_token = "Congratulations you got a Unicorn "
unicorn_sides = "!" * 3

unicorn_token = "{} {} {}".format(unicorn_sides, unicorn_token, unicorn_sides)

unicorn_top_bottom = "!" * len(unicorn_token)

print(unicorn_top_bottom)
print(unicorn_token)
print(unicorn_top_bottom)

