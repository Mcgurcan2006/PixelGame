tower_width = int(input("Enter tower width: "))
tower_height = int(input("Enter tower height: "))
car_width = int(input("Enter car width: "))
#---------------HOMEWORK STARTS BELOW---------------#
"""My program puts every character in a line into a list which is in
a nested list. I create the tower and the background first and then 
create the car on top of it. In the last step I print out the lists. 
I believe this gives me more control over the whole picture than just printing."""
x = 1
y = 0
q = 1
t = 1
r = 0
car_width_copy = car_width
car_left_x = 20
car_location = 20
full_list = []
roof_list = []
width_list = []
towerside_list = []
#Creating multiple frames
for picture_number in range(21 + car_width):
    #Creating the roof of the tower and appending it to a nested list
    for roof in range(tower_width // 2):
        for roof_line in range(tower_width):

            if x == tower_width // 2 - y:
                roof_list.append("/")
            elif x == tower_width // 2 + 1 + y:
                roof_list.append("\\")
            else:
                roof_list.append(" ")
            x = x + 1
        while q <= car_width - tower_width + 20:
            roof_list.append(" ")
            q = q + 1
        q = 1
        x = 1
        y = y + 1
        """Appending to a nested list in which one
        list is equal to one line of the picture"""
        full_list.append(roof_list.copy())
        roof_list.clear()
    y = 0
    #Creating the X's under the roof and appending it to the list
    for tower_ceiling in range(tower_width):
        width_list.append("X")
    while q <= car_width - tower_width + 20:
        width_list.append(" ")
        q = q + 1
    q = 1
    full_list.append(width_list.copy())

    #Creating the sides of the tower
    towerside_list.append("|")
    while q <= tower_width - 2:
        towerside_list.append(" ")
        q = q + 1
    q = 1
    towerside_list.append("|")
    while q <= car_width - tower_width + 20:
        towerside_list.append(" ")
        q = q + 1
    q = 1

    #Multiplying the list with the sidewalls of the tower
    for j in range(tower_height - 2):
        full_list.append(towerside_list.copy())

    #Appending for the X's on the floor
    full_list.append(width_list.copy())

    n = 0
    #Adding the car to the picture
    for number1 in range(car_width):
        full_list[-4][car_left_x + n] = "="
        full_list[-5][car_left_x + n] =" "
        full_list[-6][car_left_x + n] = "="
        n = n + 1

    if car_location >= 0:
        full_list[-5][car_left_x] = "("

    if car_location + car_width_copy > 0:
        full_list[-5][car_left_x + car_width - 1] = ")"

    #Moving the car
    car_left_x = car_left_x - 1
    car_location = car_location - 1

    if car_left_x < 0:
        car_width = car_width - 1
        car_left_x = car_left_x + 1
        r = r + 1

    #Printing out the contents of the nested list
    for sublist in full_list:
        for pixel in sublist:
            print(pixel, end="")
        print("")

    #Cleaning the lists to be used for the next loop
    full_list.clear()
    roof_list.clear()
    width_list.clear()
    towerside_list.clear()
