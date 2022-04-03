import curses
from curses import wrapper
import queue
import time
from sklearn import neighbors
maze = [
    [" ", " ", " ", "#", "#", "O", "#", "#", "#", "#"],
    [" ", "#", " ", " ", " ", " ", " ", " ", " ", "#"],
    [" ", " ", "#", "#", " ", " ", "#", " ", "#", "#"],
    [" ", " ", "#", "#", "#", " ", "#", " ", "#", "#"],
    ["#", " ", " ", " ", "#", "#", "#", " ", "#", "#"],
    ["#", " ", "#", "#", " ", " ", "#", " ", " ", " "],
    ["#", "#", "#", "#", "#", "#", "#", " ", "#", " "],
    ["#", "X", "#", " ", " ", " ", " ", " ", "#", " "],
    ["#", "#", " ", " ", "#", "#", "#", " ", " ", " "],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

def print_maze(maze,stdscr, path, way):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    GREEN = curses.color_pair(3)
    stdscr.addstr(0,0,f"Searching Via {way} Alogorithms", GREEN)
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i+3,j*2,"X",RED)
            else:
                stdscr.addstr(i+3,j*2,value,BLUE)

def find_start(maze,start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i,j

    return None;

def find_path_BFS(maze, stdscr):
    YELLOW = curses.color_pair(4)
    start = "O"
    end = "X"
    start_pos = find_start(maze,start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos
        
        stdscr.clear()
        print_maze(maze,stdscr,path,"BFS")
        time.sleep(0.2)
        stdscr.refresh()

        if(maze[row][col] == end):
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
                
            r,c = neighbor
            if maze[r][c] == '#':
                continue
        
            new_path = path + [neighbor]
            q.put((neighbor,new_path))
            visited.add(neighbor)
    
    stdscr.addstr(len(maze)+4,0,"NO path found",YELLOW)
            
def find_path_DFS(maze,stdscr):
    YELLOW = curses.color_pair(4)
    start = "O"
    end = "X"
    start_pos = find_start(maze,start)

    stack = []
    visited = set()

    stack.append((start_pos,[start_pos]))
    while len(stack):
        current_pos ,path = stack.pop()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze,stdscr,path,"DFS")
        time.sleep(0.2)
        stdscr.refresh()

        if(maze[row][col] == end):
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
                
            r,c = neighbor
            if maze[r][c] == '#':
                continue
        
            new_path = path + [neighbor]
            stack.append((neighbor,new_path))
            visited.add(neighbor)

    stdscr.addstr(len(maze)+4,0,"NO path found",YELLOW)


def find_neighbors(maze, row, col):
    neighbour = []
    if row > 0:
        neighbour.append((row-1,col))
    if row+1 < len(maze):
        neighbour.append((row+1,col))
    if col > 0:
        neighbour.append((row,col-1))
    if col+1 < len(maze[0]):
        neighbour.append((row,col+1))

    return neighbour

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    
    find_path_DFS(maze,stdscr)
    stdscr.getch()
    find_path_BFS(maze,stdscr)
    stdscr.getch()
    
wrapper(main)