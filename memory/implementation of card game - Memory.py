# implementation of card game - Memory

import simplegui
import random
import math

turns = 0
list1 = range(0, 8)
list2 = range(0, 8)
list3 = list1 + list2
WIDTH = 800
HEIGHT = 100
state = 0
cards_above = []
list_exposed = []
for x in range(16):
    list_exposed.append(False)   

# helper function to initialize globals
def new_game():
    global list3, state, cards_above, list_exposed, turns
    random.shuffle(list3)
    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))
    for x in range(16):
        list_exposed[x] = False
    cards_above = []
          
# define event handlers
def mouseclick(pos):
    global state, cards_above, turns
    click = int(math.floor(pos[0] / 50))
    
    if click in cards_above or list_exposed[click] == True:
        return
    
    list_exposed[click] = True
    
    if state == 0:
        state = 1
        turns += 1
        label.set_text("Turns = " + str(turns))
        
    elif state == 1:
        state = 2
        list_state = []
     
        for x in range(len(list_exposed)):
            if list_exposed[x] == True:
                list_state.append(x)
        if list3[list_state[0]] == list3[list_state[1]]:
            cards_above.extend(list_state)
    else:
        state = 1
        turns += 1
        label.set_text("Turns = " + str(turns))
        for x in range(16):
            list_exposed[x] = False
        list_exposed[click] = True    
                       
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for n in range(len(list3)):
        canvas.draw_text(str(list3[n]), (12.5 + (WIDTH // 16)  * (n), 60), 40, "White")
        if list_exposed[n] == False and n not in cards_above: 
            canvas.draw_polygon([(50 * n, 0), (50 * (n + 1), 0), (50 * (n + 1), HEIGHT), (50 * n, HEIGHT)], 1, 
                           "Red", "Green")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()