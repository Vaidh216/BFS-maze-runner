This is a BFS (Breadh Search search) alogritms visualizer in which the BFS & DFS is implemented to find the sortest path between 2 point on a grid

Here We start the from the "O" positive and want to reach the "X" position, "#" acts as wall for the maze where we cannot cross the wall

Tech Used : 
1.  Curses Module : 
        The curses library supplies a terminal-independent screen-painting and keyboard-handling facility for text-based terminals.
        
        Here Curses are used to clear the screen and to print the Grid everytime on the same position else all the grids 
            will be printed one after another which will look wague.
        
        Second use is to use the color for the text which will able to differentiate between the type of element in the maze and so it looks attractive.

2.  DFS Alogritm  :
        Depth-first search (DFS) is an algorithm for searching a graph or tree data structure. The algorithm starts at the root (top) node of a tree and goes as far as it can down a given branch (path)
            ,then backtracks until it finds an unexplored path, and then explores it.
        
        In DFS we can use reccursion or use the Stack Data structure to implement the algorithm, Here I Used List as a stack Data structure.

3.  BFS Algorithm : 
        Breadth First search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a “search key”') 
            and explores the neighbor nodes first, before moving to the next level neighbors         

        In DFS we can use the Queue Data structure to implement the algorithm, Here I Imported Queue form the library.

Here we have to maintain a visited set such that it does end on a infinite loop and starts to search again the searched algorithm.

Next Version : 
    The work next version of this program is to make a web application having multiple Functionalities other than as follows:

    1.  Improved UI : As it will a web application then the UI can be improved drastically by using CSS and Javascript.
    
    2.  User will be able to select the Size of the maze.

    3.  User will be able to change the state of the maze : Users can select the start point, end point and the walls.

    4.  Machine independent.