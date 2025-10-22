import time
import random


line_list = []
game_list = []
yy = 0
loop_status = True
chosen_block = 0

# Creating a 10 width line in list
for i in range(10):
    line_list.append(" ")

# Appending 20 lists for a 20x10 grid
for i in range(20):
    game_list.append(line_list.copy())

line_list.clear()

# Game floor
for i in range(10):
    line_list.append("*")

game_list.append(line_list.copy())
line_list.clear()


def block_done():
    global chosen_block
    chosen_block = random.randint(1,7)


#Square Block
def block1(x,y):
    global yy
    if y != 0 and game_list[y + 1][4 + x] not in ["□", "*"] and game_list[y + 1][5 + x] not in ["□", "*"]:
        game_list[y - 1][4 + x] = " "
        game_list[y - 1][5 + x] = " "
        game_list[y][4 + x] = " "
        game_list[y][5 + x] = " "
    if game_list[y + 1][4 + x] not in ["□", "*"] and game_list[y + 1][5 + x] not in ["□", "*"]:
        game_list[y][4 + x] = "□"
        game_list[y][5 + x] = "□"
        game_list[y + 1][4 + x] = "□"
        game_list[y + 1][5 + x] = "□"
    else:
        yy = 0
        block_done()

#Line Block
def block2(x,y):
    global yy
    if y != 0 and game_list[y + 3][4 + x] not in ["□", "*"]:
        game_list[y - 1][4 + x] = " "
        game_list[y][4 + x] = " "
        game_list[y + 1][4 + x] = " "
        game_list[y + 2][4 + x] = " "
    if game_list[y + 3][4 + x] not in ["□", "*"]:
        game_list[y][4 + x] = "□"
        game_list[y + 1][4 + x] = "□"
        game_list[y + 2][4 + x] = "□"
        game_list[y + 3][4 + x] = "□"
    else:
        yy = 0
        block_done()


#L Shaped Block
def block3(x,y):
    global yy
    if y != 0 and game_list[y + 2][4 + x] not in ["□", "*"] and game_list[y + 2][5 + x] not in ["□", "*"]:
        game_list[y - 1][4 + x] = " "
        game_list[y][4 + x] = " "
        game_list[y + 1][4 + x] = " "
        game_list[y + 1][5 + x] = " "
    if game_list[y + 2][4 + x] not in ["□", "*"] and game_list[y + 2][5 + x] not in ["□", "*"]:
        game_list[y][4 + x] = "□"
        game_list[y + 1][4 + x] = "□"
        game_list[y + 2][4 + x] = "□"
        game_list[y + 2][5 + x] = "□"
    else:
        yy = 0
        block_done()

#Reversed L Shaped Block
def block4(x,y):
    global yy
    if y != 0 and game_list[y + 2][4 + x] not in ["□", "*"] and game_list[y + 2][3 + x] not in ["□", "*"]:
        game_list[y - 1][4 + x] = " "
        game_list[y][4 + x] = " "
        game_list[y + 1][4 + x] = " "
        game_list[y + 1][3 + x] = " "
    if game_list[y + 2][4 + x] not in ["□", "*"] and game_list[y + 2][3 + x] not in ["□", "*"]:
        game_list[y][4 + x] = "□"
        game_list[y + 1][4 + x] = "□"
        game_list[y + 2][4 + x] = "□"
        game_list[y + 2][3 + x] = "□"
    else:
        yy = 0
        block_done()

#T Shaped Block
def block5(x,y):
    global yy
    if y != 0 and game_list[y + 1][4 + x] not in ["□", "*"]:
        game_list[y - 1][3 + x] = " "
        game_list[y - 1][4 + x] = " "
        game_list[y - 1][5 + x] = " "
        game_list[y][4 + x] = " "
    if game_list[y + 1][4 + x] not in ["□", "*"]:
        game_list[y][3 + x] = "□"
        game_list[y][4 + x] = "□"
        game_list[y][5 + x] = "□"
        game_list[y + 1][4 + x] = "□"
    else:
        yy = 0
        block_done()


#2/2 Block
def block6(x,y):
    global yy
    if y != 0 and game_list[y + 1][4 + x] not in ["□", "*"] and game_list[y + 1][5 + x] not in ["□", "*"]:
        game_list[y - 1][3 + x] = " "
        game_list[y - 1][4 + x] = " "
        game_list[y][4 + x] = " "
        game_list[y][5 + x] = " "
    if game_list[y + 1][4 + x] not in ["□", "*"] and game_list[y + 1][5 + x] not in ["□", "*"]:
        game_list[y][3 + x] = "□"
        game_list[y][4 + x] = "□"
        game_list[y + 1][4 + x] = "□"
        game_list[y + 1][5 + x] = "□"
    else:
        yy = 0
        block_done()

#Reversed 2/2 Block
def block7(x,y):
    global yy
    if y != 0 and game_list[y + 1][4 + x] not in ["□", "*"] and game_list[y + 1][3 + x] not in ["□", "*"]:
        game_list[y - 1][5 + x] = " "
        game_list[y - 1][4 + x] = " "
        game_list[y][4 + x] = " "
        game_list[y][3 + x] = " "
    if game_list[y + 1][4 + x] not in ["□", "*"] and game_list[y + 1][3 + x] not in ["□", "*"]:
        game_list[y][5 + x] = "□"
        game_list[y][4 + x] = "□"
        game_list[y + 1][4 + x] = "□"
        game_list[y + 1][3 + x] = "□"
    else:
        yy = 0
        block_done()

def tetris():
    global yy
    global chosen_block

    if chosen_block == 1:
        block1(0, yy)
    if chosen_block == 2:
        block2(0, yy)
    if chosen_block == 3:
        block3(0, yy)
    if chosen_block == 4:
        block4(0, yy)
    if chosen_block == 5:
        block5(0, yy)
    if chosen_block == 6:
        block6(0, yy)
    if chosen_block == 7:
        block7(0, yy)

    yy += 1

    #Printing out the game
    for sub_list in game_list:
        print("".join(sub_list))


block_done()
while loop_status:

    tetris()
    time.sleep(0.1)