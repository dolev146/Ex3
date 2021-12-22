import json

from src.Classes import SaveLoad
from src.Classes.DiGraph import DiGraph
from src.interfaces.GraphAlgoInterface import GraphAlgoInterface



class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g=None):
        self.g = DiGraph(g)

    def load_from_json(self, file_name: str) -> bool:
        self.g = SaveLoad.load(file_name)

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def plot_graph(self) -> None:
        pass


if __name__ == '__main__':
    ga = GraphAlgo()
    ga.load_from_json("../../data/A0.json")
    ga.g.all_in_edges_of_node(1)
    a = 5
