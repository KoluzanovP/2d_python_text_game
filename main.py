from graphics import *

def draw_room(win, name, descr_place, descr):
    ht = win.getHeight()
    wd = win.getWidth()

    if(name == 'Dungeon'):
        act_zone = Rectangle(Point(wd/2, 0), Point(wd, ht))
        act_zone.setFill("white")

        inner_act_zone = Rectangle(Point(wd*(1/2+1/8), ht*(2/8)), Point(wd*(1-1/8), ht*(1-2/8)))
        inner_act_zone.setFill("black")

        left_door = Rectangle(Point(wd*(1/2+1/8), ht*(3/8)), Point(wd*(1/2+1/8)+10, ht*(4/8)))
        left_door.setFill("brown")

        act_zone.draw(win)
        inner_act_zone.draw(win)
        left_door.draw(win)

    if (name == 'Laboratory'):
        act_zone = Rectangle(Point(500, 0), Point(1000, 1000))
        act_zone.setFill("white")

        inner_act_zone = Rectangle(Point(wd*(1/2+1/8), ht*(2/8)), Point(wd*(1-1/8), ht*(1-2/8)))
        inner_act_zone.setFill("yellow")

        top_door = Rectangle(Point(wd * (1/2 + 1/4 - 1/32),  ht*(2/8)), Point(wd*(1/2 + 1/4 + 1/32),  ht*(2/8)+10))
        top_door.setFill("brown")

        act_zone.draw(win)
        inner_act_zone.draw(win)
        top_door.draw(win)

    if (name == 'The Great Hall'):
        act_zone = Rectangle(Point(500, 0), Point(1000, 1000))
        act_zone.setFill("white")

        inner_act_zone = Rectangle(Point(wd*(1/2+1/8), ht*(2/8)), Point(wd*(1-1/8), ht*(1-2/8)))
        inner_act_zone.setFill("blue")

        left_door = Rectangle(Point(wd * (1 / 2 + 1 / 8), ht * (3 / 8)), Point(wd * (1 / 2 + 1 / 8) + 10, ht * (4 / 8)))
        left_door.setFill("brown")

        top_door = Rectangle(Point(wd * (1 / 2 + 1 / 4 - 1 / 32), ht * (2 / 8)), Point(wd * (1 / 2 + 1 / 4 + 1 / 32), ht * (2 / 8) + 10))
        top_door.setFill("brown")

        right_door = Rectangle(Point(wd * (1 - 1 / 8), ht * (3 / 8)), Point(wd * (1 - 1 / 8) - 10, ht * (4 / 8)))
        right_door.setFill("brown")

        bottom_door = Rectangle(Point(wd * (1 / 2 + 1 / 4 - 1 / 32), ht * (1 - 2 / 8)),Point(wd * (1 / 2 + 1 / 4 + 1 / 32), ht * (1 - 2/8) - 10))
        bottom_door.setFill("brown")

        act_zone.draw(win)
        inner_act_zone.draw(win)
        left_door.draw(win)
        top_door.draw(win)
        right_door.draw(win)
        bottom_door.draw(win)

    if (name == 'Kitchen'):
        act_zone = Rectangle(Point(500, 0), Point(1000, 1000))
        act_zone.setFill("white")

        inner_act_zone = Rectangle(Point(wd*(1/2+1/8), ht*(2/8)), Point(wd*(1-1/8), ht*(1-2/8)))
        inner_act_zone.setFill("gray")

        right_door = Rectangle(Point(wd*(1-1/8), ht * (3 / 8)), Point(wd*(1-1/8)-10, ht * (4/8)))
        right_door.setFill("brown")

        act_zone.draw(win)
        inner_act_zone.draw(win)
        right_door.draw(win)

    if (name == 'Elevator'):
        act_zone = Rectangle(Point(500, 0), Point(1000, 1000))
        act_zone.setFill("white")

        inner_act_zone = Rectangle(Point(wd*(1/2+1/8), ht*(3/8)), Point(wd*(1-1/8), ht*(1-3/8)))
        inner_act_zone.setFill("gray")

        bottom_door = Rectangle(Point(wd * (1 / 2 + 1 / 4 - 1 / 32), ht*(1-3/8)),Point(wd * (1 / 2 + 1 / 4 + 1 / 32), ht*(1-3/8)-10) )
        bottom_door.setFill("brown")


        act_zone.draw(win)
        inner_act_zone.draw(win)
        bottom_door.draw(win)

    if (name == 'Main entrance'):
        act_zone = Rectangle(Point(500, 0), Point(1000, 1000))
        act_zone.setFill("white")

        inner_act_zone = Rectangle(Point(wd*(1/2+3/16), ht*(3/8)), Point(wd*(1-3/16), ht*(1-3/8)))
        inner_act_zone.setFill("yellow")

        bottom_door = Rectangle(Point(wd * (1 / 2 + 1 / 4 - 1 / 32), ht * (1 - 3 / 8)),Point(wd * (1 / 2 + 1 / 4 + 1 / 32), ht * (1 - 3 / 8) - 10))
        bottom_door.setFill("brown")

        top_door = Rectangle(Point(wd * (1 / 2 + 1 / 4 - 1 / 32), ht * (3 / 8)), Point(wd * (1 / 2 + 1 / 4 + 1 / 32), ht * (3 / 8) + 10))
        bottom_door.setFill("brown")

        entrance_text = Text(Point(wd * (1 / 2 + 1 / 4 - 1 / 32)+30, ht * (3 / 8)-10), "Main entrance")

        act_zone.draw(win)
        inner_act_zone.draw(win)
        bottom_door.draw(win)
        top_door.draw(win)
        entrance_text.draw(win)

    descr_place.setText(descr)

    place = Text(Point(750, 50), name)
    place.draw(win)

    hero = Circle(Point(wd*3/4, ht*1/2), wd/100)
    hero.setFill("red")
    hero.draw(win)

    return

def validation(command, things):
    sep = command.split(' ')
    if(len(sep) > 2):
        return 0
    if(len(sep) == 1 and sep[0] != 'look'):
        return 0

    if(len(sep) == 2):
        if( sep[0] == 'go' and not(sep[1] in ['north','west', 'east', 'south'])):
            return 0
        if( sep[0] == 'get' and not(sep[1] in things)):
            return 0
    return 1

def view_invent(inv, win, inv_text):
    if(sum(inv.values()) == 0):
        text = 'You have got nothing'
        inv_text.setText(text)
        return
    else:
        line = 'You have got '
        k = 0
        for i in range(len(inv.values())):
            if(list(inv.values())[i] == 1):
                if(k == 0):
                    line = line  + list(inv.keys())[i]
                else:
                    line = line + ', ' + list(inv.keys())[i]
                k+=1
        print(line)
        inv_text.setText(line)
        return

def look(curr_place, inv, inv_text):
    line = ""
    if(curr_place == "Dungeon"):
        if(inv['map'] + inv['key'] == 0):
            line = 'You see a map and a key. '
        elif(inv['map'] == 0):
            line = 'You see a map. '
        elif (inv['key'] == 0):
            line = 'You see a key. '
        line = line + 'You see a door on the west'

    if(curr_place == "Laboratory"):
        if(inv['energy'] == 0):
            line = 'You see an energy locked inside the safe. '
        line = line + 'You see a door on the north.'

    if (curr_place == "The Great Hall"):
        line = "There are 1 doors in each part of the world."

    if (curr_place == "Kitchen"):
        if (inv['garlic'] + inv['paper'] == 0):
            line = 'You see a garlic and a paper. '
        elif (inv['garlic'] == 0):
            line = 'You see a garlic. '
        elif (inv['paper'] == 0):
            line = 'You see a paper. '
        line = line + 'You see a door on the east'

    if (curr_place == "Elevator"):
        line = 'There is a door on the south.'

    if (curr_place == "Main entrance"):
        line = 'There is exit on north and a door on the south.'

    print(line)
    inv_text.setText(line)
    return

def get(curr_place, inv, inv_text, thing):
    line = ""
    if (curr_place == "Dungeon"):
        if (thing == 'map' and inv['map'] == 1):
            line = 'You already have it.'
        elif (thing == 'map' and inv['map'] == 0):
            line = 'You picked a map.'
            inv['map']=1
        elif (thing == 'key' and inv['key'] == 1):
            line = 'You already have it.'
        elif (thing == 'key' and inv['key'] == 0):
            line = 'You picked a key.'
            inv['key']=1
        else:
            line = "Can't do it."

    if (curr_place == "Laboratory"):
        if (inv['energy'] == 1):
            line = 'You already have it.'
        elif (inv['energy'] == 0 and inv['paper'] == 1):
            line = 'You picked an energy.'
            inv['energy']=1
        elif (inv['energy'] == 0 and inv['paper'] == 0):
            line = "You can't open the safe."
        else:
            line = "Can't do it."

    if (curr_place == "The Great Hall"):
        line = "There is nothing to pick here."

    if (curr_place == "Kitchen"):
        if (thing == 'garlic' and inv['garlic'] == 1):
            line = 'You already have it.'
        elif(thing == 'garlic' and inv['garlic'] == 0):
            line = 'You picked a garlic.'
            inv['garlic'] = 1

        elif (thing == 'paper' and inv['paper'] == 1):
            line = 'You already have it.'
        elif(thing == 'paper' and inv['paper'] == 0):
            line = 'You picked a paper.'
            inv['paper'] = 1
        else:
            line = "Can't do it."

    if (curr_place == "Elevator"):
        line = "Can't do it."

    if (curr_place == "Main entrance"):
        line = "Can't do it."

    print(line)
    inv_text.setText(line)
    return

def go(curr_place, direct, inv, win, inv_text, descr_place):
    if (curr_place == "Dungeon"):
        if(direct == 'west'):
            if(inv['key'] == 0):
                inv_text.setText("The door is locked")
                return "Dungeon"
            else:
                draw_room(win, 'The Great Hall', descr_place,'Great Hall description')
                inv_text.setText('Moved to the Great Hall')
                return "The Great Hall"
        else:
            inv_text.setText("Can't move that way")
            return curr_place


    if (curr_place == "Laboratory"):
        if(direct == 'north'):
            draw_room(win, 'The Great Hall', descr_place, 'Great Hall description')
            inv_text.setText('Moved to the Great Hall')
            return "The Great Hall"
        else:
            inv_text.setText("Can't move that way")
            return curr_place

    if (curr_place == "The Great Hall"):
        if(direct == 'west'):
            draw_room(win, 'Kitchen', descr_place, 'Kitchen description')
            inv_text.setText('Moved to Kitchen')
            return "Kitchen"
        if(direct == 'east'):
            draw_room(win, 'Dungeon', descr_place, 'Dungeon description')
            inv_text.setText('Moved to Dungeon')
            return "Dungeon"
        if (direct == 'south'):
            draw_room(win, 'Laboratory', descr_place, 'Laboratory description')
            inv_text.setText('Moved to Laboratory')
            return "Laboratory"
        if(direct == 'north'):
            if(inv['energy'] == 1):
                if(inv['garlic'] == 0):
                    draw_room(win, 'Main entrance', descr_place, 'You are in Main entrance and you are dead, game is over for you, buddy.')
                    inv_text.setText('Moved to Main entrance using elevator')
                    return "Exit"
                if (inv['garlic'] == 1):
                    draw_room(win, 'Main entrance', descr_place, 'There was a boss! You killed him using garlic! Game over, you win!')
                    inv_text.setText('Moved to Main entrance using elevator')
                    return "Exit"
            else:
                draw_room(win, 'Elevator', descr_place, 'Elevator description')
                inv_text.setText('Moved to Elevator')
                return "Elevator"

    if (curr_place == "Kitchen"):
        if(direct == "east"):
            draw_room(win, 'The Great Hall', descr_place, 'Great Hall description')
            inv_text.setText('Moved to the Great Hall')
            return "The Great Hall"
        else:
            inv_text.setText("Can't move that way")
            return curr_place

    if (curr_place == "Elevator"):
        if (direct == "south"):
            draw_room(win, 'The Great Hall', descr_place, 'Great Hall description')
            inv_text.setText('Moved to the Great Hall')
            return "The Great Hall"
        else:
            inv_text.setText("Can't move that way")
            return curr_place


def main():
    win = GraphWin("Dungeon master", 1000, 500)

    Text(Point(50, 50), "Command:").draw(win)

    validity = Text(Point(350, 50), "Waiting for command...")
    validity.draw(win)

    inputText1 = Entry(Point(200, 50), 10)
    #inputText1.setText(" ")
    inputText1.draw(win)

    button = Text(Point(150, 150), "Send command")
    button.draw(win)
    Rectangle(Point(75, 125), Point(225, 175)).draw(win)

    inv = dict.fromkeys(['map', 'key', 'garlic', 'paper', 'energy'], 0)

    inv_text = Text(Point(250, 450), " ")
    inv_text.draw(win)

    descr_place = Text(Point(250, 250), "")
    descr_place.draw(win)

    curr_place = "Dungeon"
    draw_room(win, curr_place, descr_place,"Starting description")

    f = open('logs.txt', 'w')
    step = 1
    exit_flag = 0
    while(exit_flag == 0):
        win.getMouse()
        inv_text.setText('')
        command = inputText1.getText()
        command = command.lower()
        f.write('Action ' + str(step) + ': '  + command + '\n')
        step = step + 1

        if(validation(command, list(inv.keys())) == 1):
            validity.setText("Command is valid")
        else:
            validity.setText("Command is invalid")
            continue

        com = command.split(' ')

        if(com[0] == 'look'):
            look(curr_place, inv, inv_text)

        if(com[0] == 'go'):
            curr_place = go(curr_place, com[1], inv, win, inv_text, descr_place)

        if(com[0] == 'get'):
            get(curr_place, inv, inv_text, com[1])

        if(com[0] == 'view' and com[1] == 'inventory'):
            view_invent(inv, win, inv_text)

        if(curr_place == 'Exit'):
            exit_flag = 1

    total_score = 100*sum(list(inv.values()))
    inv_text.setText('Total score is ' + str(total_score))
    button.setText('Exit')

    win.getMouse()
    win.close()
    f.close()
main()