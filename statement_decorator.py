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

zebra_token = " You got a Zebra "
zebra_sides = "z" * 3

zebra_token = "{} {} {}".format(zebra_sides, zebra_token, zebra_sides)

zebra_top_bottom = "z" * len(zebra_token)

print(zebra_top_bottom)
print(zebra_token)
print(zebra_top_bottom)

horse_token = " You got a Horse "
horse_sides = "h" * 3

horse_token = "{} {} {}".format(horse_sides, horse_token, horse_sides)

horse_top_bottom = "h" * len(horse_token)

print(horse_top_bottom)
print(horse_token)
print(horse_top_bottom)

donkey_token = " You got a Donkey "
donkey_sides = "d" * 3

donkey_token = "{} {} {}".format(donkey_sides, donkey_token, donkey_sides)

donkey_top_bottom = "d" * len(donkey_token)

print(donkey_top_bottom)
print(donkey_token)
print(donkey_top_bottom)
