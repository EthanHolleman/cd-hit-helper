from element import element

class cluster():
    def __init__(self, num=None, parent_file=None):
        self.num = num
        self.elements = set([])
        self.parent_file = parent_file
        self.num_elements = len(self.elements)
        self.average_similarity = average_similarity()

    def add_element(self, el):
        if isinstance(el, element):
            self.elements.add(el)
            return True
        else:
            return False

    def average_similarity(self):
        sum_sim = 0
        l = 0
        for el in self.elements:
            sum_sim += el.similarity
        return sum_sim/self.num_elements
