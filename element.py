class Element():

    def __init__(self, cluster_num, ID, similarity, nt, rep=False):
        self.cluster = cluster_num
        self.ID = ID
        self.similarity = similarity
        self.nt = nt
        self.rep = rep
