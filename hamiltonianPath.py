from itertools import combinations

def load_instance(input_file_name):
    global NUMBER_OF_VERTECES, NUMBER_OF_EDGES, START_VERTEX, GOAL_VERTEX, ATOMIC_STATEMENTS

    edges = []
    out_edges = {}
    in_edges = {}
    ATOMIC_STATEMENTS = [] # edge is in Hamiltonian path


    with open(input_file_name, "r") as file:
        NUMBER_OF_VERTECES, NUMBER_OF_EDGES = map(int, file.readline().split())
        START_VERTEX, GOAL_VERTEX = map(int, file.readline().split())


        for i in range(NUMBER_OF_VERTECES):
            edges.append([])

        for i in range(NUMBER_OF_EDGES):
            ATOMIC_STATEMENTS.append(i+1)

        for line in range(NUMBER_OF_EDGES):
            line = map(int, file.readline().split())
            if line:
                u, v = [int(i) for i in line]
                edges[u].append(v)

        print(edges)
    

    return edges


def encode():

    cnf = []

    restrict_number_of_edges(cnf)

    print(cnf)



def restrict_number_of_edges(cnf):

    combs = combinations(ATOMIC_STATEMENTS, len(ATOMIC_STATEMENTS) - NUMBER_OF_VERTECES + 2)
    for comb in combs: # at least NUMBER_OF_VERTECES - 1 edges are in Hamiltanian path4
        condition = []

        for atomic_statement in comb:
            condition.append(atomic_statement)
        
        cnf.append(condition)

    combs = combinations(ATOMIC_STATEMENTS, NUMBER_OF_VERTECES)
    for comb in combs:
        condition = []
        
        for atomic_statement in comb:
            condition.append(-atomic_statement)

        cnf.append(condition)

def deg_out_one(): # degree of every vertex, except goal vertex, is 1
    pass




load_instance("./instances/input-triangle.in")
encode()