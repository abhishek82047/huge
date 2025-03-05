# Advanced Game Software: Knave

import random

# User Data
user_balance = 0
user_inventory = []
user_relationships = {
    'girlfriends': [],
    'sidechicks': [],
    'sugarmommies': []
}
user_children = []
relationship_affection = {}

# Command Handler
def handle_command(command):
    global user_balance
    if command == "!work":
        earnings = random.randint(10, 100)
        user_balance += earnings
        print(f"🛠️ You worked and earned {earnings} coins!")

    elif command == "!balance":
        print(f"💰 Your current balance is: {user_balance} coins")

    elif command == "!beg":
        earnings = random.choice([0, 5, 20, 50])
        user_balance += earnings
        if earnings == 0:
            print("🚫 No one gave you anything!")
        else:
            print(f"🙏 Someone gave you {earnings} coins!")

    elif command == "!rps":
        play_rps()

    elif command == "!shop":
        display_shop()

    elif command.startswith("!buy"):
        _, item = command.split(" ", 1)
        buy_item(item)

    elif command == "!profile":
        display_profile()

    elif command == "!dig":
        dig_treasure()

    elif command == "!fish":
        fish_treasure()

    elif command == "!search":
        search_for_items()

    elif command.startswith("!use"):
        _, item = command.split(" ", 1)
        use_item(item)

    elif command == "!daily":
        collect_daily()

    elif command == "!steal":
        steal_money()

    elif command == "!hunt":
        hunt_animals()

    elif command == "!love":
        show_love()

    elif command == "!gift":
        give_gift()

    elif command == "!segs":
        reproduce()

    elif command == "!ccode":
        cheat_code()

    elif command == "!exit":
        print("Thanks for playing Knave!")
        exit()

    else:
        print("❌ Invalid command!")

# Rock-Paper-Scissors Game
def play_rps():
    global user_balance

    choices = ["rock", "paper", "scissors"]
    print("Choose rock, paper, or scissors:")

    try:
        user_choice = input("Your choice: ").strip().lower()
    except (EOFError, ValueError):
        print("Input error. Skipping...")
        return

    if user_choice not in choices:
        print("❌ Invalid choice! Try again.")
        return

    print(f"You chose: {user_choice}")

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("🎉 You win! You earned 50 coins!")
        user_balance += 50
    else:
        print("😢 You lose!")

# Shop System
shop_items = {
    'shovel': 100,
    'fishing_rod': 150,
    'girlfriend': 500,
    'sidechick': 750,
    'sugarmommy': 1000,
    'mysterious_box': 2000,
    'dragon': 10000,
    'kraken': 8000,
    'gold_bar': 15000,
    'gun': 5000
}

def display_shop():
    print(f"💰 Your current balance is: {user_balance} coins")
    print("🛒 Shop Items:")
    for item, price in shop_items.items():
        emoji = get_item_emoji(item)
        print(f"{emoji} {item} - {price} coins")

def get_item_emoji(item):
    emojis = {
        'shovel': '⛏️',
        'fishing_rod': '🎣',
        'girlfriend': '💖',
        'sidechick': '💋',
        'sugarmommy': '💸',
        'mysterious_box': '📦',
        'dragon': '🐉',
        'kraken': '🦑',
        'gold_bar': '🏅',
        'gun': '🔫'
    }
    return emojis.get(item, '❔')

def buy_item(item):
    global user_balance
    if item not in shop_items:
        print("❌ Item not found in the shop!")
        return

    cost = shop_items[item]
    if user_balance < cost:
        print("❌ You don't have enough coins!")
        return

    user_balance -= cost
    user_inventory.append(item)
    print(f"✅ You bought a {item}!")

    if item == 'sugarmommy':
        sugarmommy_name = random.choice(["Linda", "Jessica", "Monica", "Samantha"])
        user_relationships['sugarmommies'].append(sugarmommy_name)
        relationship_affection[sugarmommy_name] = 50
        print(f"💸 Your sugarmommy {sugarmommy_name} joined you! Keep her happy for rewards.")

    elif item == 'girlfriend':
        gf_name = random.choice(["Emma", "Sophia", "Isabella", "Ava"])
        user_relationships['girlfriends'].append(gf_name)
        relationship_affection[gf_name] = 50
        print(f"💖 Your girlfriend {gf_name} joined you! Keep her happy for surprises.")

    elif item == 'sidechick':
        sc_name = random.choice(["Bella", "Zoe", "Lily", "Chloe"])
        user_relationships['sidechicks'].append(sc_name)
        relationship_affection[sc_name] = 30
        print(f"💋 Your sidechick {sc_name} joined you! Careful, she's demanding!")

def cheat_code():
    global user_balance
    if "cheat_used" not in user_inventory:
        user_balance += 10000
        user_inventory.append("cheat_used")
        print("🎉 Cheat activated! You received 10,000 coins!")
    else:
        print("❌ Cheat code can only be used once!")

# Main Game Loop
while True:
    command = input("Enter a command: ").strip()
    handle_command(command)
