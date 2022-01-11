from random import choice
options = ["rock", "paper", "scissors", "rock"]
bot_points = 0
user_points = 0


def calc_points(bot_i, user_i):
    """Will determine who gets the point"""

    user_win = options[bot_i+1]
    bot_win = options[user_i+1]

    global user_points; global bot_points

    if user_i != bot_i:
        if options[user_i] == user_win:                
            user_points = user_points +1
        if options[bot_i] == bot_win:
            bot_points = bot_points +1


print("Let's play a game of Rock, Paper and Scissors!")
menu_message = "Choose \n1. rock\n2. paper\3. scissors"
while True:
    print("Choose \n1. rock\n2. paper\n3. scissors\n4. finish game")
    global user; global bot
    user = int(input("Enter Choice: ")) -1
    if user in [0, 1, 2]:
        bot = choice([0, 1 ,2 ])
        calc_points(bot, user)
        print("User: ", user_points, "(", options[user], ")")
        print("Bot: ", bot_points, "(", options[bot], ")")

    elif user == 3:
        print("\nFinal scores \nUser: ", user_points, "\nBot: ", bot_points)
        break

    else:
        print("Invalid response. Try again")
    print()
        
        



