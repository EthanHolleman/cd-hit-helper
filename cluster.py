# FASTA FILES HEADER MUST BE UNIQUE FOR THIS TO WORK

from element import ClstrElement
from fasta_tools import read_as_tuples


class Cluster():

    def get_average_similarity(self):
        sum_sim = 0
        l = 0
        if self.num_elements != 0:
            for el in self.elements:
                sum_sim += el.similarity
            return sum_sim / self.num_elements
        else:
            return 0

    def __init__(self, num=None, parent_file=None):
        self.num = num
        self.elements = set([])
        self.parent_file = parent_file
        self.num_elements = len(self.elements)
        self.average_similarity = self.get_average_similarity()

    def add_element(self, el):
        if isinstance(el, ClstrElement):
            self.elements.add(el)
            return True
        else:
            return False

    def get_cluster_elements(self):
        # need to search for elements in the fasta file
        # going to assume that headers is always made to the first space
        fasta = self.parent_file.split('.')[0]
        # fasta duplicate always made by cd hit which has the same
        # file name but no extension as the clstr file
        try:
            lines = []
            fasta_elements = []
            search_dict = {}
            with open(self.parent_file) as parent:
                lines = read_as_tuples(parent)

            for element_tuple in lines:
                search_dict[element_tuple[0].split(' ')[0]] = element_tuple
                # use up to first space as key

            for clstr_element in self.elements:
                if clstr_element.name in search_dict:
                    fasta_elements.append(search_dict[clstr_element.name])
                # adds all elements in a cluster to the fasta elements list

            return fasta_elements  # list of tuples

        except FileNotFoundError as e:
            return e
