import art
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print(art.logo)

bid_dict = {}

continue_result = True
while continue_result:

    name = input("what is your name?: ").lower()
    price = int(input("what is your bid: $ "))

    bid_dict[name] = price

    answer = input("Are there any other bidders? Type 'yes or 'no'. \n").lower()

    if answer == "no":
        continue_result = False
    elif answer == "yes":
        print("\n" * 100)
        print("")

max_bid = 0
win_name = ""

for name in bid_dict:
    if bid_dict[name] > max_bid:
        max_bid = bid_dict[name]
        win_name = name

print(f"The winner is {win_name} with a bid of $ {bid_dict[win_name]}")

