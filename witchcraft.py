import time
import curses

screen = curses.initscr()
h, w = screen.getmaxyx()
menu = 0
menus = [['make ice cream', 'quit'], ['strawberry', 'chocolate', 'vanilla', 'back']] 

#0 - main
#1 - flavours

def text_to_screen(text):
    screen.addstr(
    curses.LINES // 2 - 10,
    curses.COLS // 2 - len(text) // 2,
    text)
    

def print_menu(screen, current_row_idx, current_menu):
    for idx, row in enumerate(current_menu):
        x = w//2 - len(row)//2
        y = h//2 - len(current_menu)//2 + idx
        if idx == current_row_idx:
            screen.attron(curses.color_pair(1))
            screen.addstr(y, x, row)
            screen.attroff(curses.color_pair(1))
        else:
            screen.addstr(y, x, row)

def chocolate():
    return('You lose yourself in the richness of the chocolate ice cream as it melts on your tongue.')

def strawberry():
    return('Memories of a childhood full of carefree summer moments flood back to you as you enjoy the tart strawberry flavour.')
    
def vanilla():
    return('Uniqueness is overrated, and as a vanilla ice cream enjoyer you know that better than anyone. Enjoy!')

def run(current_row):

    global menu
    
    if menu == 0:
        if current_row == 0:
            menu +=  1
        elif current_row == 1:
            quit()
        
    elif menu == 1:
        if current_row == 0:
              text_to_screen(strawberry())
        elif current_row == 1:
              text_to_screen(chocolate())
        elif current_row == 2:
             text_to_screen(vanilla())
        elif current_row == 3:
              menu -=1
                  

def main(screen):
    curses.curs_set(0)
    current_row = 0
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_current_menu = []
    while True:
        current_menu = menus[menu]
        print_menu(screen, current_row, current_menu)
        key = screen.getch()
        screen.clear()
        if key == curses.KEY_UP and current_row > 0:
            current_row -=1 
        elif key == curses.KEY_DOWN and current_row < len(current_menu) - 1:
            current_row +=1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            run(current_row)
        if current_menu != current_current_menu:
            current_row = 0 
        screen.refresh()
        current_current_menu = current_menu        

curses.wrapper(main)
curses.endwin()
