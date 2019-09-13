from element import Element
from cluster import Cluster

def read_cluster(header_line, parent_file=None):
    number = header_line.split(' ')[-1]
    return Cluster(num=number, parent_file=parent_file)


def make_element(element_string, cluster_num=None):
    '''
    Takes in a string with all Element info and returns
    and Element object.
    '''
    # 0	10389nt, >name=RLG_Gmr1_Gm1-1... at +/82.14%
    element_string = element_string.strip()
    similarity = None
    rep = False
    comma_split = element_string.split(',')
    nt = comma_split[0].split(' ')[-1]
    # returns nt by spliting at , so nt now contained in first item of
    # the list split that again by space so nt in second Element of new list
    # finally trim of the last character
    ID = element_string[0]
    name = element_string.split(',')[1]  # needs further processing

    if '*' in set(name):
        rep = True
    else:
        similarity = float(element_string.split('at ')[-1][2:-1])
        # gets the % similarity b/c all non rep lines have 'at ' followed
        # by the percentage in normal output. THen Trim off the first two chars
        # and the percent sign at the end and case to float
    name = name.split(' ')[1]
    if name[-3:] == '...':
        name = name[0:-3]  # removes ... if present in the header
    return Element(ID=ID, similarity=similarity, nt=nt, rep=rep, cluster_num=cluster_num)

def read_cluster_file(path):
    '''
    reads a .cltr type file into a dictionary where each key is the Cluster
    header the values are the elements in that Cluster
    '''
    try:
        with open(path, 'r') as clus_file:
            Cluster_set = set([])
            current_Cluster = None

            for line in clus_file:  # iterate through all lines in file
                if line[0] == '>':  # line is a header
                    new_Cluster = read_cluster(line, parent_file=path)
                    if new_Cluster not in Cluster_set:
                        current_Cluster = new_Cluster  # save the new as current
                        Cluster_set.add(current_Cluster)  # add new Cluster to set
                else:
                    current_Cluster.add_element(make_element(line))
                    # not header so is an Element so add to the Cluster object
                    # designated as current_Cluster
        return Cluster_set
    except (FileNotFoundError, IsADirectoryError) as e:
        print(path, 'gave the following errors', e)
        print('Empty set added')
        return set([])

class ClstrFile():

    def __init__(self, path):
        self.path = path
        Clusters_set = read_cluster_file(path)
