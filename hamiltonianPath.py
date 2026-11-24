from itertools import combinations

def load_instance(input_file_name):
    global NUMBER_OF_VERTECES, NUMBER_OF_EDGES, START_VERTEX, GOAL_VERTEX, ATOMIC_STATEMENTS
    global out_edges, in_edges

    edges = {}
    out_edges = {}
    in_edges = {}
    ATOMIC_STATEMENTS = [] # edge is in Hamiltonian path


    with open(input_file_name, "r") as file:
        NUMBER_OF_VERTECES, NUMBER_OF_EDGES = map(int, file.readline().split())
        START_VERTEX, GOAL_VERTEX = map(int, file.readline().split())

        for i in range(NUMBER_OF_EDGES):
            ATOMIC_STATEMENTS.append(i+1)

        number_of_edge = 1

        for line in range(NUMBER_OF_EDGES):
            line = map(int, file.readline().split())
            if line:

                u, v = [int(i) for i in line]

                edges[number_of_edge] = [u, v]

                if u not in out_edges:
                    out_edges[u] = [number_of_edge]
                else:
                    out_edges[u].append(number_of_edge)

                if v not in in_edges:
                    in_edges[v] = [number_of_edge]
                else:
                    in_edges[v].append(number_of_edge)

            number_of_edge += 1

        print(edges)
    

    return edges


def encode():

    cnf = []

    restrict_number_of_edges(cnf)

    print(cnf)



def restrict_number_of_edges(cnf):

        new_cnf = cnf_for_n_from_k(ATOMIC_STATEMENTS, len(ATOMIC_STATEMENTS), NUMBER_OF_VERTECES-1)

        #print(new_cnf)
        cnf += new_cnf

def cnf_for_n_from_k(variables, k, n):

    new_cnf = []
    combs = combinations(variables, k - n + 1)
    for comb in combs:
        condition = []

        for atomic_statement in comb:
            condition.append(atomic_statement)
        
        new_cnf.append(condition)

    combs = combinations(variables, n+1)
    for comb in combs:
        condition = []
        
        for atomic_statement in comb:
            condition.append(-atomic_statement)

        new_cnf.append(condition)

    return new_cnf


def deg_in_one(): # degree of every vertex, except goal vertex, is 1
    print(in_edges)
    print(out_edges)
    for vertex in in_edges:

        if vertex == START_VERTEX: # skip start vertex, because its deg of in edges must be 0
            continue

        variables = in_edges[vertex]
        cnf_for_deg_in = cnf_for_n_from_k(variables, len(variables), 1)
        print(cnf_for_deg_in)



load_instance("./instances/input-triangle.in")
encode()

deg_in_one()