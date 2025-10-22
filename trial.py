import tkinter as tk
import random
from idlelib.configdialog import font_sample_text

root = tk.Tk()

root.geometry("500x500")
root.title("TETRIS")


line_list = []
game_list = []
yy = 0
xx = 0
x_status = True
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

def refresh_board():
    board_label.config(text="\n".join("".join(row) for row in game_list))

def update_x(dx):
    global yy
    global xx
    global chosen_block
    xx += dx

    if chosen_block == 1:
        block1(xx, yy)
    if chosen_block == 2:
        block2(xx, yy)
    if chosen_block == 3:
        block3(xx, yy)
    if chosen_block == 4:
        block4(xx, yy)
    if chosen_block == 5:
        block5(xx, yy)
    if chosen_block == 6:
        block6(xx, yy)
    if chosen_block == 7:
        block7(xx, yy)

    refresh_board()

def update_y(dy):
    global yy
    global xx
    global chosen_block
    yy += dy

    if chosen_block == 1:
        block1(xx, yy)
    if chosen_block == 2:
        block2(xx, yy)
    if chosen_block == 3:
        block3(xx, yy)
    if chosen_block == 4:
        block4(xx, yy)
    if chosen_block == 5:
        block5(xx, yy)
    if chosen_block == 6:
        block6(xx, yy)
    if chosen_block == 7:
        block7(xx, yy)

    refresh_board()

def move_left(event):
    update_x(-1)

def move_right(event):
    update_x(1)

def move_down(event):
    update_y(1)

def rotate_block(event):
    pass

def block_done():
    global chosen_block
    chosen_block = random.randint(1,7)

def clear_block(x, y):
    pass

#Square Block
def block1(x,y):
    global yy
    global xx
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
        xx = 0
        block_done()

#Line Block
def block2(x,y):
    global yy
    global xx
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
        xx = 0
        block_done()


#L Shaped Block
def block3(x,y):
    global yy
    global xx
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
        xx = 0
        block_done()

#Reversed L Shaped Block
def block4(x,y):
    global yy
    global xx
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
        xx = 0
        block_done()

#T Shaped Block
def block5(x,y):
    global yy
    global xx
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
        xx = 0
        block_done()


#2/2 Block
def block6(x,y):
    global yy
    global xx
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
        xx = 0
        block_done()

#Reversed 2/2 Block
def block7(x,y):
    global yy
    global xx
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
        xx = 0
        block_done()

def tetris():
    global yy

    update_y(1)
    refresh_board()

    root.after(1000, tetris)


board_label = tk.Label(root, font=('Arial', 18))
board_label.pack()

#Choosing the first block
block_done()

#Starting the game process
tetris()

root.bind("<s>", move_down)

if x_status:
    root.bind("<d>", move_left)
    root.bind("<a>", move_right)

root.bind("<space>", rotate_block)

#Starting the Tkinter
root.mainloop()








