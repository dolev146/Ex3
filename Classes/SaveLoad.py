import json
import random

from Classes.DiGraph import DiGraph


def load(file_name):
    file = open(file_name, "r")
    graph_dict = json.load(file)
    file.close()
    graph = DiGraph()

    for n in graph_dict["Nodes"]:
        if "pos" not in n:
            x = None
            y = None
            z = None
            xyz = (x, y, z)
            node_id = int(n["id"])
            graph.add_node(node_id, xyz)
        else:
            pos = n["pos"].split(",")
            xyz = (float(pos[0]), float(pos[1]), float(pos[2]))
            node_id = int(n["id"])
            graph.add_node(node_id, xyz)
    for e in graph_dict["Edges"]:
        graph.add_edge(int(e["src"]), int(e["dest"]), float(e["w"]))
    return graph


def save(file_name, graph) -> bool:
    Nodes = graph.Nodes
    dict_json = {'Nodes': [], 'Edges': []}
    for key, node in Nodes.items():
        id_node = node.id
        if node.x is not None and node.y is not None and node.z is not None:
            pos_string = str(node.x) + ',' + str(node.y) + ',' + str(node.z)
            node_dict_individual = {"id": id_node, "pos": pos_string}
            dict_json['Nodes'].append(node_dict_individual)
        else:
            node_dict_individual = {"id": id_node}
            dict_json['Nodes'].append(node_dict_individual)

    Edges = graph.Edges
    for key, edge in Edges.items():
        src_edge = edge.src
        dest_edge = edge.dest
        w_edge = edge.w
        edge_dict_individual = {'src': src_edge, 'w': w_edge, 'dest': dest_edge}
        dict_json['Edges'].append(edge_dict_individual)
    # str_file = "./save/" + file_name + '.json'
    try:
        with open(file_name, 'w+') as f:
            json.dump(dict_json, f, indent=6)
            return True
    except Exception as e:
        print(e)
        return False
