import random

def welcome():
    print("welcome to python gym")

def create_character():
    name = input("enter your character's name: ")
    return {
        "name": name,
        "strength": 0,
        "stamina": 0,
        "health": 50,
        "money": 0,
        "buff": False
    }

def check_death(player):
    if player["health"] <= 0:
        print("game over you died")
        return True
    return False

def name_status(player):
    return f"{player['name']} | str: {player['strength']} | sta: {player['stamina']} | hp: {player['health']} | $: {player['money']}"

def shop(player):
    print("\nwant to buy anything? (yes/no)")
    choice = input("> ")
    if choice == "yes":
        print("\n--- shop ---")
        print("protein shake - $20 (gain +5 str next day instead of +1)")
        print("type 'protein' to buy or anything else to skip.")
        item = input("> ")
        if item == "protein":
            if player["money"] >= 20:
                player["money"] -= 20
                player["buff"] = True
                print("you bought a protein shake! you'll be super strong tomorrow.")
            else:
                print("u broke")
    else:
        print("skipping shop.")

def lift_weights(player):
    gained = 0
    buff_gain = 5 if player["buff"] else 1
    print(f"\nlifting time! type 'lift' to gain strength. you gain {buff_gain} per lift.")
    print("day ends if you gain 5, get hurt, or avoid a roadblock. type 'back' to quit.")

    while gained < 5:
        action = input("> ")
        if action == "lift":
            player["strength"] += buff_gain
            gained += buff_gain
            print(f"strength: {player['strength']} (+{buff_gain})")
            if random.random() < 0.3:
                print("you're starting to feel pain. keep going? (yes/no)")
                decision = input("> ")
                if decision == "yes":
                    print("ouch! you pulled a muscle. -10 health.")
                    player["health"] -= 10
                    return False
                else:
                    print("returning to menu. ending day.")
                    if player["buff"]:
                        player["buff"] = False
                    return True
        elif action == "back":
            print("ending day early.")
            return True

    if player["buff"]:
        player["buff"] = False
    return True

def run_activity(player):
    gained = 0
    print("\nrunning time! type 'run' to gain stamina.")
    print("day ends if you gain 5, get hurt, or avoid a roadblock. type 'back' to quit.")

    while gained < 5:
        action = input("> ")
        if action == "run":
            player["stamina"] += 1
            gained += 1
            print(f"stamina: {player['stamina']} (+1)")
            if random.random() < 0.3:
                print("a storm is coming. keep running or go home? (run/home)")
                decision = input("> ")
                if decision == "run":
                    if random.random() < 0.5:
                        print("you were struck by lightning! -40 health.")
                        player["health"] -= 40
                        return False
                    else:
                        print("you dodged the storm and kept going!")
                else:
                    print("returning to menu. ending day.")
                    return True
        elif action == "back":
            print("ending day early.")
            return True
    return True

def home_screen(player, day):
    print(f"\n--- day {day}/10 ---")
    print(name_status(player))
    print("choose your activity:")
    print("1. lift weights")
    print("2. run")

    choice = input("> ")
    if choice == "1":
        return lift_weights(player)
    elif choice == "2":
        return run_activity(player)
    else:
        print("invalid choice.")
        return home_screen(player, day)

def start_game():
    welcome()
    player = create_character()
    day = 1

    while day <= 10:
        success = home_screen(player, day)
        if check_death(player):
            return start_game()

        if success:
            player["money"] += 10
            print("successful day! +$10")

        shop(player)
        day += 1

    print("\n--- 10 days over ---")
    print(name_status(player))
    if player["strength"] >= 20 and player["stamina"] >= 20:
        print("u win! you reached your fitness goal.")
    else:
        print("you didn't reach the goal in time. restarting...")
        start_game()

start_game()

