import curses

mylist = []
items = []
size = 20
tittle = "LESSA'S INVESTIMENT ANALYZIS"

top = 0
bottom = 0

for i in range(size):
    mylist.append(str(i))

for i in range(100):
    items.append(str(i))


def print_menu(stdscr, selected_row_idx, mvindex):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    bottom = stdscr.getmaxyx()[0]

    # Title
    stdscr.attron(curses.color_pair(3))
    # stdscr.hline(0, 0, " ", w)
    stdscr.addstr(0, w // 2 - len(tittle) // 2, tittle)
    stdscr.attroff(curses.color_pair(3))

    # Colums
    stdscr.attron(curses.color_pair(3))
    # stdscr.hline(2, 0, " ", w)
    stdscr.addstr(2, 0, "PAPEL")
    stdscr.attroff(curses.color_pair(3))

    # print(len(items)-bottom+3)
    # if mvindex >= len(items)-bottom+3:
    #     mvindex = len(items)-bottom+3

    if mvindex >= 1:

        # if mvindex >= len(items)-bottom+3:
        #     selected_row_idx = len(items)-20

        for idx, row in enumerate(items[top+mvindex:bottom-3+mvindex]):
            if idx == selected_row_idx:
                # print(selected_row_idx)
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(idx + 3, 0, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(idx + 3, 0, row)
    else:
        for idx, row in enumerate(items[top:bottom-3]):

            if idx == selected_row_idx:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(idx + 3, 0, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(idx + 3, 0, row)
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr):
    # turn off cursor blinking
    bottom = stdscr.getmaxyx()[0]
    top = 0
    mvindex = 0
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_menu(stdscr, current_row, 0)

    while 1:
        key = stdscr.getch()
        if key == curses.KEY_PPAGE and mvindex > stdscr.getmaxyx()[0] -1:
            mvindex -= stdscr.getmaxyx()[0]
        if key == curses.KEY_UP and current_row <= 0 < mvindex:
            mvindex -= 1
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < bottom - 4:
            current_row += 1
        elif key == curses.KEY_DOWN and current_row >= bottom - 4 and mvindex < len(items)-stdscr.getmaxyx()[0]+3:
            mvindex += 1
        if key == curses.KEY_NPAGE and mvindex < len(items)-stdscr.getmaxyx()[0]+3:
            mvindex += stdscr.getmaxyx()[0]

        elif key == curses.KEY_RESIZE:
            if current_row > stdscr.getmaxyx()[0]-4:
                current_row = stdscr.getmaxyx()[0]-4
        elif key == curses.KEY_ENTER or key in [10, 13]:
            break
        # print(mvindex)
        print_menu(stdscr, current_row, mvindex)


curses.wrapper(main)