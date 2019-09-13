from element import element

def read_cluster_file(path):
    '''
    reads a .cltr type file into a dictionary where each key is the cluster
    header the values are the elements in that cluster
    '''
    try:
        with open(path, 'r') as clus_file:
            cluster_dict = {}
            current_cluster = ''
            for line in clus_file:  # iterate through all lines in file
                if line[0] == '>' and line not in cluster_dict:
                    # check if current line is a header
                    # if true make it the current header and add to dict
                    current_cluster = line
                    cluster_dict[current_cluster] = []
                else:
                    cluster_dict[current_cluster].append(line)
                    # not at a header and must be at a line after a header
                    # so we know to add this line to the value of the current
                    # header in cluster_dict
    except (FileNotFoundError, IsADirectoryError) as e:
        return e

def make_element(element_string):
    '''
    Takes in a string with all element info and returns
    and element object.
    '''
    temp_list_a = element_string.split('^I') #['0\t15518nt, >name=RLG_Gmr12_Gm15-9... *']

    temp_list_b = element_string.split(',') #['0\t15518nt', ' >name=RLG_Gmr12_Gm15-9... *']

    #return element(ID=temp_list_a[0], )
