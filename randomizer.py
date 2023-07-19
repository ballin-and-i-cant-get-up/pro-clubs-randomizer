import random

formations = {
        "3-1-4-2" :
        ["LS", "RS", "LM", "LCM", "CDM", "RCM", "RM", "LCB", "CB", "RCB"],
        "3-4-1-2":
        ["LS", "RS", "CAM", "LM","LCM","RCM","RM","LCB", "CB", "RCB"],
        "3-4-2-1":
        ["LF", "ST", "RF", "LM","LCM", "RCM", "RM", "LCB", "CB", "RCB"],
        "3-4-3 Diamond":
        ["LW", "ST", "RW", "CAM", "LM", "RM", "CDM", "LCB", "CB", "RCB"],
        "3-4-3 Flat":
        ["LW", "ST", "RW", "LM", "LCM", "RCM", "RM", "LCB", "CB", "RCB"],
        "3-5-1-1":
        ["ST", "CF", "LM", "RM", "CM", "LDM", "RDM", "LCB", "CB", "RCB"],
        "3-5-2":
        ["ST", "ST", "LM", "CAM", "LDM", "RDM", "RM", "LCB", "CB", "RCB"],
        "4-1-2-1-2 Narrow":
        ["LS", "RS", "CAM", "LCM", "RCM", "CDM", "LB", "LCB", "RCB", "RB"],
        "4-1-2-1-2 Wide":
        ["LS", "RS", "CAM", "LM", "RM", "CDM", "LB", "LCB", "RCB", "RB"],
        "4-1-3-2":
        ["LS", "RS", "LM", "CM", "RM", "CDM", "LB", "LCB", "RCB", "RB"],
        "4-1-4-1":
        ["ST", "LM", "LCM", "RCM", "RM", "CDM", "LB", "LCB", "RCB", "RB"],
        "4-2-2-2":
        ["LS", "RS", "LAM", "RAM", "LDM", "RDM", "LB", "LCB", "RCB", "RB"],
        "4-2-3-1 Wide":
        ["ST", "CAM", "LM", "RM", "LDM", "RDM", "LB", "LCB", "RCB", "RB"],
        "4-2-3-1 Narrow":
        ["ST", "LAM", "CAM", "RAM", "LDM", "RDM", "LB", "LCB", "RCB", "RB"],
        "4-2-4":
        ["ST", "ST", "LW", "RW", "LCM", "RCM", "LB", "LCB", "RCB", "RB"],
        "4-3-1-2":
        ["LS", "RS", "CAM", "LCM", "CM", "RCM", "LB", "LCB", "RCB", "RB"],
        "4-3-2-1":
        ["ST", "LF", "RF", "LCM", "RCM", "CM", "LB", "LCB", "RCB", "RB"],
        "4-3-3 Flat":
        ["LW", "ST", "RW", "LCM", "CM", "RCM", "LB", "LCB", "RCB", "RB"],
        "4-3-3 False 9":
        ["CF", "LW", "RW", "LCM", "RCM", "CDM", "LB", "LCB", "RCB", "RB"],
        "4-3-3 Attack":
        ["LW", "ST", "RW", "CAM", "LCM", "RCM", "LB", "LCB", "RCB", "RB"],
        "4-3-3 Defend":
        ["LW", "ST", "RW", "CM", "LDM", "RDM", "LB", "LCB", "RCB", "RB"],
        "4-3-3 Holding":
        ["LW", "ST", "RW", "LCM", "RCM", "CDM", "LB", "LCB", "RCB", "RB"],
        "4-4-1-1 Attack":
        ["ST", "CF", "LM", "LCM", "RCM", "RM", "LB", "LCB", "RCB", "RB"],
        "4-4-1-1 Midfield":
        ["ST", "CAM", "LM", "LCM", "RCM", "RM", "LB", "LCB", "RCB", "RB"],
        "4-4-2 Flat":
        ["LS", "RS", "LM", "LCM", "RCM", "RM", "LB", "LCB", "RCB", "RB"],
        "4-4-2 Holding":
        ["LS", "RS", "LM", "LDM", "RDM", "RM", "LB", "LCB", "RCB", "RB"],
        "4-5-1 Attack":
        ["ST", "LAM", "RAM", "LM", "CM", "RM", "LB", "LCB", "RCB", "RB"],
        "4-5-1 Flat":
        ["ST", "LM", "RM", "LCM", "CM", "RCM", "LB", "LCB", "RCB", "RB"],
        "5-2-1-2":
        ["LS", "RS", "CAM", "LCM", "RCM", "LWB", "LCB", "CB", "RCB", "RWB"],
        "5-2-3":
        ["LW", "ST", "RW", "LCM", "RCM", "LWB" ,"LCB", "CB", "RCB", "RWB"],
        "5-3-2 (Holding)":
        ["LS", "RS", "LCM", "CDM", "RCM", "LWB", "LCB", "CB", "RCB", "RWB"],
        "5-4-1 Diamond":
        ["ST", "CAM", "LM", "RM", "CDM", "LWB", "RWB", "LCB", "CB", "RCB"],
        "5-4-1 Flat":
        ["LS", "RS", "LCM", "RCM", "CDM", "LWB", "LCB", "CB", "RCB", "RWB"]
}
players = []
print("Enter each player's name followed by the 'enter' key.")
print("Enter an empty name to finish entering names.")
while (len(players) < 10):
    player_num = len(players) + 1
    player = input("Player " + str(player_num) + ": ")
    if (player == ""):
        break
    players.append(player)
reroll = True
while (reroll):
    reroll = False
    formation, positions = random.choice(list(formations.items()))
    print("\nFormation:\n" + formation)
    curr_positions = positions
    print ("\nPositions:")
    for i in range(len(players)):
        player_pos = curr_positions.pop(random.randrange(len(curr_positions)))
        print(players[i] + ':', player_pos)
    reroll_prompt = input("Would you like to play again? (y/n)\n")
    if (reroll_prompt == 'Y' or reroll_prompt == 'y' or reroll_prompt == 'Yes' or reroll_prompt == 'yes'):
        reroll = True
