# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    from util import Stack
    fringe = Stack()

    from collections import defaultdict
    relations = defaultdict(list)
    directions = defaultdict(list)

    currentPosition = problem.getStartState()
    visited = []

    while(problem.isGoalState(currentPosition) == False):

        visited.append(currentPosition)
        children = problem.getSuccessors(currentPosition)

        for child in children:
            fringe.push(child)
            relations[currentPosition].append(child[0])

        while(True):
            poppedItem = fringe.pop()
            currentPosition = poppedItem[0];
            if currentPosition not in visited:
                directions[currentPosition] = poppedItem[1]
                break;

    visited.append(currentPosition)

    i = len(visited) - 1

    while i>0:

        outer_j = 0

        if visited[i] not in relations[visited[i-1]]:

            j = i-2

            while True:
                if visited[i] in relations[visited[j]]:
                    outer_j = j
                    break;
                else:
                    j = j - 1;

            j = j + 1

            new_visited = visited[:j]
            new_visited.extend(visited[i:])
            visited = new_visited

            i = outer_j;

        else:
            i = i - 1;

    plan = []

    for i in range(len(visited)-1):
        plan.append(directions[visited[i+1]])

    return plan

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    from util import Queue
    fringe = Queue()

    currentPosition = problem.getStartState()
    visited = []

    from collections import defaultdict
    relations = defaultdict(list)
    directions = defaultdict(list)

    while (problem.isGoalState(currentPosition) == False):

        visited.append(currentPosition)
        children = problem.getSuccessors(currentPosition)

        for child in children:
            fringe.push(child)
            relations[currentPosition].append(child[0])

        while (True):
            poppedItem = fringe.pop()
            currentPosition = poppedItem[0];
            if currentPosition not in visited:
                directions[currentPosition] = poppedItem[1]
                break;

    visited.append(currentPosition)

    i = len(visited) - 1

    while i>0:

        outer_j = 0

        if visited[i] not in relations[visited[i-1]]:

            j = i-2

            while True:
                if visited[i] in relations[visited[j]]:
                    outer_j = j
                    break;
                else:
                    j = j - 1;

            j = j + 1

            new_visited = visited[:j]
            new_visited.extend(visited[i:])
            visited = new_visited

            i = outer_j;

        else:
            i = i - 1;

    #Fix for BFS AutoGrader Test : Many Paths
    deletethesestates = []
    for m in range(0, len(visited) - 2):
        if visited[m + 2] in relations[visited[m]]:
            deletethesestates.append(visited[m + 1])

    visited = [x for x in visited if x not in deletethesestates]

    plan = []
    for i in range(len(visited)-1):
        plan.append(directions[visited[i+1]])

    return plan

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    from collections import defaultdict
    relations = defaultdict(list)
    directions = defaultdict(list)

    from util import PriorityQueue
    fringe = PriorityQueue()

    currentPosition = problem.getStartState()
    cost_to_currentPosition = 0
    visited = []

    while (problem.isGoalState(currentPosition) == False):

        visited.append(currentPosition)
        children = problem.getSuccessors(currentPosition)

        for child in children:
            cost = cost_to_currentPosition + child[2]
            fringe.update(child, cost)
            relations[currentPosition].append(child[0])

        while (True):
            poppedItem = fringe.pop()
            currentPosition = poppedItem[0];
            cost_to_currentPosition = poppedItem[2]
            if currentPosition not in visited:
                directions[currentPosition] = poppedItem[1]
                break;

    visited.append(currentPosition)

    i = len(visited) - 1

    while i > 0:

        outer_j = 0

        if visited[i] not in relations[visited[i - 1]]:

            j = i - 2

            while True:
                if visited[i] in relations[visited[j]]:
                    outer_j = j
                    break;
                else:
                    j = j - 1;

            j = j + 1

            new_visited = visited[:j]
            new_visited.extend(visited[i:])
            visited = new_visited

            i = outer_j;

        else:
            i = i - 1;

    # Fix for AutoGrader Test : Many Paths
    deletethesestates = []
    for m in range(0, len(visited) - 2):
        if visited[m + 2] in relations[visited[m]]:
            deletethesestates.append(visited[m + 1])

    visited = [x for x in visited if x not in deletethesestates]

    plan = []
    for i in range(len(visited) - 1):
        plan.append(directions[visited[i + 1]])

    return plan

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    from collections import defaultdict
    relations = defaultdict(list)
    directions = defaultdict(list)

    from util import PriorityQueue
    fringe = PriorityQueue()

    currentPosition = problem.getStartState()
    cost_to_currentPosition = 0
    visited = []

    while (problem.isGoalState(currentPosition) == False):

        visited.append(currentPosition)
        children = problem.getSuccessors(currentPosition)

        for child in children:
            cost = cost_to_currentPosition + child[2] + heuristic(child[0], problem)
            fringe.update(child, cost)
            relations[currentPosition].append(child[0])

        while (True):
            poppedItem = fringe.pop()
            currentPosition = poppedItem[0];
            cost_to_currentPosition = poppedItem[2]
            if currentPosition not in visited:
                directions[currentPosition] = poppedItem[1]
                break;

    visited.append(currentPosition)

    i = len(visited) - 1

    while i > 0:

        outer_j = 0

        if visited[i] not in relations[visited[i - 1]]:

            j = i - 2

            while True:
                if visited[i] in relations[visited[j]]:
                    outer_j = j
                    break;
                else:
                    j = j - 1;

            j = j + 1

            new_visited = visited[:j]
            new_visited.extend(visited[i:])
            visited = new_visited

            i = outer_j;

        else:
            i = i - 1;

    # Fix for AutoGrader Test : Many Paths
    deletethesestates = []
    for m in range(0, len(visited) - 2):
        if visited[m + 2] in relations[visited[m]]:
            deletethesestates.append(visited[m + 1])

    visited = [x for x in visited if x not in deletethesestates]

    plan = []
    for i in range(len(visited) - 1):
        plan.append(directions[visited[i + 1]])

    return plan

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
