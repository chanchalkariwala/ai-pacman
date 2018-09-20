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
    startstate=problem.getStartState()
    currentposition=problem.getStartState()
    arewethereyet=problem.isGoalState(currentposition)
    visited=[startstate]
    instructions=[]
    plan=[]
    from collections import defaultdict
    relations=defaultdict(list)
    directions=defaultdict(list)
    import numpy
    from game import Directions
    from game import Actions
    actions=Actions()
    n=Directions.NORTH
    s=Directions.SOUTH
    e=Directions.EAST
    w=Directions.WEST
    from util import Stack
    stack=Stack()
    while (arewethereyet==False):
        successors=problem.getSuccessors(currentposition)
        print("Successors for "+str(currentposition)+" are "+str(successors))
        for item in successors:
            stack.push(item)
            relations[currentposition].append(item[0])
        moved=False
        while (not moved):
            poppeditem=stack.pop()
            if (poppeditem[0] not in visited):
                directions[poppeditem[0]]=poppeditem[1]
                currentposition=poppeditem[0]
                visited.append(currentposition)
                moved=True
        arewethereyet=problem.isGoalState(currentposition)
    print("Relations = "+str(relations))
    print("Length of Relations = "+str(len(relations)))
    print("Directions = "+str(directions))
    print("Length of Directions = "+str(len(directions)))
    numhops=0
    print("Visited = "+str(visited))
    print("Length of Visited = "+str(len(visited)))
    for i in range(0,len(visited)-1):
        print(visited[i+1])
        print(relations[visited[i]])
        if visited[i+1] not in relations[visited[i]]:
            numhops += 1
    print("Number of Hops = "+str(numhops))
    instructions=visited
    print("Original Length of Instructions = "+str(len(instructions)))
    for i in range(0,numhops):
        for j in range(0,len(instructions)-1):
            if visited[j+1] not in relations[visited[j]]:
                rightend=instructions[j+1]
                rightendindex=j+1
                print("Right End = "+str(rightend))
                break
        for k in range(0,len(instructions)-1):
            if rightend in relations[visited[k]]:
                leftend=instructions[k]
                leftendindex=k
                print("Left End = "+str(leftend))
                break
        instructions[leftendindex+1:rightendindex]=[]
    print("Instructions = "+str(instructions))
    print("Final Length of Instructions = "+str(len(instructions)))
    for m in range(0,len(instructions)-1):
        plan.append(directions[visited[m+1]])
    print("Plan = "+str(plan))
    print("Length of Plan = "+str(len(plan)))
    return plan

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    startstate=problem.getStartState()
    currentposition=problem.getStartState()
    arewethereyet=problem.isGoalState(currentposition)
    visited=[startstate]
    instructions=[]
    from collections import defaultdict
    relations=defaultdict(list)
    directions=defaultdict(list)
    import numpy
    from game import Directions
    from game import Actions
    n=Directions.NORTH
    s=Directions.SOUTH
    e=Directions.EAST
    w=Directions.WEST
    from util import Queue
    queue=Queue()
    while (arewethereyet==False):
        successors=problem.getSuccessors(currentposition)
#        print("Successors for "+str(currentposition)+" are "+str(successors))
        for item in successors:
            queue.push(item)
            relations[currentposition].append(item[0])
        moved=False
        while (not moved):
            poppeditem=queue.pop()
            if (poppeditem[0] not in visited):
                directions[poppeditem[0]]=poppeditem[1]
                currentposition=poppeditem[0]
                visited.append(currentposition)
                moved=True
        arewethereyet=problem.isGoalState(currentposition)

#    print("Relations = "+str(relations))
#    print("Length of Relations = "+str(len(relations)))
#    print("Directions = "+str(directions))
#    print("Length of Directions = "+str(len(directions)))
#    print("Visited = "+str(visited))
#    print("Length of Visited = "+str(len(visited)))

    instructions=visited
    length=len(visited)
    goal=instructions[length-1]
#    print("Original Length of Instructions = "+str(len(instructions)))
#    print("Goal = "+str(goal))
    backwardinstructions=[goal]
    edge=goal
    for i in range(0,length-1):
        if edge in relations[instructions[length-i-2]]:
            backwardinstructions.append(instructions[length-i-2])
            edge=instructions[length-i-2]

#    print("Backward Instructions = "+str(backwardinstructions))
#    print("Length of Backward Instructions = "+str(len(backwardinstructions)))

    finalinstructions=[]
    for j in range(0,len(backwardinstructions)):
        finalinstructions.append(backwardinstructions[len(backwardinstructions)-j-1])

#    print("Final Instructions = "+str(finalinstructions))
#    print("Length of Final Instructions = "+str(len(finalinstructions))) 

    deletethesestates=[]
    for m in range(0,len(finalinstructions)-2):
        if finalinstructions[m+2] in relations[finalinstructions[m]]:
            deletethesestates.append(finalinstructions[m+1])

    finalinstructions2 = [x for x in finalinstructions if x not in deletethesestates]

    finalplan=[]
    for k in range(0,len(finalinstructions2)-1):
        finalplan.append(directions[finalinstructions2[k+1]])
#    print("Final Plan = "+str(finalplan))
#    print("Length of Final Plan = "+str(len(finalplan)))

    return finalplan

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    startstate=problem.getStartState()
    print("Start State = "+str(startstate))
    currentposition=problem.getStartState()
    print("Current Position = "+str(currentposition))
    arewethereyet=problem.isGoalState(currentposition)
    print("Current Position is the Goal State: "+str(arewethereyet))
    visited=[startstate]
    instructions=[]
    plan=[]
    import numpy
    from game import Directions
    n=Directions.NORTH
    s=Directions.SOUTH
    e=Directions.EAST
    w=Directions.WEST
    from util import PriorityQueue
    priorityqueue=PriorityQueue()
    from searchAgents import StayEastSearchAgent
    from searchAgents import StayWestSearchAgent
    while (arewethereyet==False):
        successors=problem.getSuccessors(currentposition)
        print("Successors = "+str(successors))
        newsuccessors=[]
        for item in successors:
            newitem=list(item)
            action=[newitem[1]]
            priority=problem.getCostOfActions(action)
            newsuccessors.append([item,priority])
        print("Updated Successors = "+str(newsuccessors))
        for item in newsuccessors:
            priorityqueue.update(item[0],item[1])
        moved=False
        while (not moved):
            poppeditem=priorityqueue.pop()
            if (poppeditem[0] not in visited):
                currentposition=poppeditem[0]
                visited.append(currentposition)
                moved=True
        arewethereyet=problem.isGoalState(currentposition)

    print("Visited = "+str(visited))
    print("Length of Visited = "+str(len(visited)))

    instructions=visited
    length=len(visited)
    goal=instructions[length-1]
    print("Goal = "+str(goal))
    backwardplan=[goal]
    edge=goal
    for i in range(0,length):
        difference=numpy.subtract(edge,instructions[length-i-1])
        print("Difference = "+str(difference))
        if abs(difference[0])+abs(difference[1]) == 1:
            backwardplan.append(instructions[length-i-1])
            edge=instructions[length-i-1]
    print("Backward Plan = "+str(backwardplan))

    for j in range(0,len(backwardplan)):
        plan.append(backwardplan[len(backwardplan)-j-1])
    print("Plan = "+str(plan))

    finalplan=[]
    for m in range(0,len(plan)-1):
        directionmoved=numpy.subtract(plan[m+1],plan[m])
        if directionmoved[0]==0 and directionmoved[1]==1:
            finalplan.append(n)
        if directionmoved[0]==0 and directionmoved[1]==-1:
            finalplan.append(s)
        if directionmoved[0]==1 and directionmoved[1]==0:
            finalplan.append(e)
        if directionmoved[0]==-1 and directionmoved[1]==0:
            finalplan.append(w)
    print("Final Plan = "+str(finalplan))
    return finalplan
#    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
