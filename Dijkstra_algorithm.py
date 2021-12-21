"""PROJECT 1
Dijkstra algorithm"""


import math
from termcolor import colored
import heapq


def distance(first_height: int, second_height: int, step: int) -> float:
    """
    This function finds real distance between two points.
    :param first_height: the height of the first point.
    :param second_height: the height of the second point.
    :param step: horizontal distance between to neighbour points.
    :return: distance between two points.
    """
    return math.sqrt((first_height - second_height) ** 2 + step ** 2)


def dictionary_generator(inputed, step):
    """
    Returns the dictionary with vertexes as keys and lists of tuples with two elements:
    the neighbour vertex and distances to it as valueses
    :param inputed: the list of lists of hights of vertexes
    :param step: the distanse between every vertex in 2D dimension
    :return: dictionary, that represents the graph
    >>> dictionary_generator([[1,3,4],[4,2,3],[6,4,3],[2,4,7]], 5)
    {(0, 1): [((1, 1), 5.0990195135927845), ((0, 2), 5.0990195135927845), \
((0, 0), 5.385164807134504)], (1, 1): [((0, 1), 5.0990195135927845), \
((1, 0), 5.385164807134504), ((2, 1), 5.385164807134504)], (0, 2): \
[((0, 1), 5.0990195135927845)], (0, 0): [((0, 1), 5.385164807134504), \
((1, 0), 5.830951894845301)], (1, 0): [((0, 0), 5.830951894845301), \
((2, 0), 5.385164807134504), ((1, 1), 5.385164807134504)], (2, 0): \
[((1, 0), 5.385164807134504), ((2, 1), 5.385164807134504), ((3, 0), \
6.4031242374328485)], (2, 1): [((1, 1), 5.385164807134504), ((3, 1), \
5.0), ((2, 2), 5.0990195135927845), ((2, 0), 5.385164807134504)], \
(3, 1): [((2, 1), 5.0), ((3, 0), 5.385164807134504)], (2, 2): \
[((2, 1), 5.0990195135927845)], (3, 0): [((2, 0), 6.4031242374328485), ((3, 1), 5.385164807134504)]}
    """
    # This is matrix rewritten as a dictionary. The key is a point and value contains
    # neighbour points and distance to them.
    dictionary_of_matrix = {}
    for row in range(len(inputed)):
        # row - - number of line in matrix(starts with 0)
        for vertex in range((1 if row % 2 == 0 else 0), len(inputed[row]) - (1 if len(inputed[row]) % 2 == 1 else 0),
                            2):
            # vertex - number of the element in the row(starts with 0)
            # check on the neighbor above
            if row - 1 >= 0:
                # distance between two points.
                dist = distance(inputed[row][vertex], inputed[row - 1][vertex], step)
                # adds value to the dictionary, if there is no key then it is created
                dictionary_of_matrix[(row, vertex)] = dictionary_of_matrix.get((row, vertex), []) + [((row - 1, vertex), dist)]
                # adds an adjacent vertex to the dictionary as the key and value of the point
                dictionary_of_matrix[(row - 1, vertex)] = dictionary_of_matrix.get((row - 1, vertex), []) + [((row, vertex), dist)]
            # check on the neighbor below
            if row + 1 <= len(inputed) - 1:
                dist = distance(inputed[row][vertex], inputed[row + 1][vertex], step)
                dictionary_of_matrix[(row, vertex)] = dictionary_of_matrix.get((row, vertex), []) + [((row + 1, vertex), dist)]
                dictionary_of_matrix[(row + 1, vertex)] = dictionary_of_matrix.get((row + 1, vertex), []) + [((row, vertex), dist)]
            # check on the neighbor on the right
            if vertex + 1 <= len(inputed[row]) - 1:
                dist = distance(inputed[row][vertex], inputed[row][vertex + 1], step)
                dictionary_of_matrix[(row, vertex)] = dictionary_of_matrix.get((row, vertex), []) + [((row, vertex + 1), dist)]
                dictionary_of_matrix[(row, vertex + 1)] = dictionary_of_matrix.get((row, vertex + 1), []) + [((row, vertex), dist)]
            # check on the neighbor on the left
            if vertex - 1 >= 0:
                dist = distance(inputed[row][vertex], inputed[row][vertex - 1], step)
                dictionary_of_matrix[(row, vertex)] = dictionary_of_matrix.get((row, vertex), []) + [((row, vertex - 1), dist)]
                dictionary_of_matrix[(row, vertex - 1)] = dictionary_of_matrix.get((row, vertex - 1), []) + [((row, vertex), dist)]
    return dictionary_of_matrix


def dijkstra(graph: dict, points: tuple) -> list:
    """
    Returns the shortest path from points[0] to points[1] using Dijkstra algorithm
    :param graph: the dictionary, that represents the graph
    :param points: tuple with coordnates of start and final point
    :return: the shortes path from start to final point
    >>> dijkstra({(0, 1): [((1, 1), 5.0990195135927845), ((0, 2), 5.0990195135927845), \
((0, 0), 5.385164807134504)], (1, 1): [((0, 1), 5.0990195135927845), \
((1, 0), 5.385164807134504), ((2, 1), 5.385164807134504)], (0, 2): \
[((0, 1), 5.0990195135927845)], (0, 0): [((0, 1), 5.385164807134504), \
((1, 0), 5.830951894845301)], (1, 0): [((0, 0), 5.830951894845301), \
((2, 0), 5.385164807134504), ((1, 1), 5.385164807134504)], (2, 0): \
[((1, 0), 5.385164807134504), ((2, 1), 5.385164807134504), ((3, 0), \
6.4031242374328485)], (2, 1): [((1, 1), 5.385164807134504), ((3, 1), \
5.0), ((2, 2), 5.0990195135927845), ((2, 0), 5.385164807134504)], \
(3, 1): [((2, 1), 5.0), ((3, 0), 5.385164807134504)], (2, 2): \
[((2, 1), 5.0990195135927845)], (3, 0): [((2, 0), 6.4031242374328485), \
((3, 1), 5.385164807134504)]}, ((0,0), (2,2)))
    [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
    """
    # dictionary that
    dist = {key: float("inf") for key in graph.keys()}
    visited = set()  # points that we have already visited
    before = dict()  # dictionary that has a point as a key and shortest way as a value
    start = points[0]
    end = points[1]
    min_dist = [(0, start)]  # list of points to choose from
    dist[start] = 0
    before[start] = -1
    #
    while min_dist:
        cur_dist, current_point = heapq.heappop(min_dist)
        # if we have already considered this point
        if current_point in visited:
            continue
        visited.add(current_point)
        # we pass through the neighbour points
        for neighbor in graph[current_point]:
            point = neighbor[0]
            dist_to_point = neighbor[1]
            if point in visited:
                continue
            # distance from the current to this neighboring point.
            this_dist = cur_dist + dist_to_point
            # if the distance is less then we change it
            if this_dist < dist[point]:
                dist[point] = this_dist
                before[point] = current_point
                heapq.heappush(min_dist, (this_dist, point))
    # error check
    if len(visited) != len(dist):
        return []
    result = [end]
    # adding points to result
    while before[end] != -1:
        result.append((before[end][0], before[end][1]))
        end = before[end]
    # because we added from the end we need to reverse the list
    result.reverse()
    return result


if __name__ == "__main__":
    path_to_file = input("Input path to the test file: ")
    file1 = open(path_to_file, 'r')
    # Size of the matrix
    (n, m) = list(map(int, file1.readline().split(' ')))
    matrix = []
    # forming matrix
    for i in range(n):
        matrix.append(list(map(int, file1.readline().split(' '))))
    step = int(file1.readline())
    # point from which we has to find a shortest distance
    point1 = tuple(list(map(int, file1.readline().split(' '))))
    # point to which we has to find a shortest distance
    point2 = tuple(list(map(int, file1.readline().split(' '))))
    # the shortest way
    answer = dijkstra(dictionary_generator(matrix, step), (point1, point2))
    print(answer)
    draw = input("Do you want the graph to be drawn? y/N: ")
    if draw == "y":
        # drawing the matrix with shown the shortest way between to points.
        print("  ", end="")
        for i in range(m):
            print(f'{i}    ', end="")
        print()
        for lines in range(n):
            print(f'{lines} ', end="")
            for line in range(m):
                if (lines, line) in answer and line != m - 1:
                    # the shortest way will be coloured in green
                    text = colored("X    ", color="green")
                    print(text, end="")
                elif line != m - 1:
                    print("*    ", end="")
                else:
                    if(lines, line) in answer:
                        text = colored("X", color="green")
                        print(text, end="")
                    else:
                        print("*", end="")
            print()
