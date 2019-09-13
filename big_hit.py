import os
import subprocess

CDHIT = '/media/ethan/Vault/cdhit'
ELEMENTS = '/media/ethan/Vault/Gypsy_Seperated'
OUT_DIR = '/media/ethan/Vault/Cluster_Analysis'
FILE_EXT = 'fna'


def get_element_files():
    element_list = []
    els = os.listdir(ELEMENTS)
    for el in els:
        ext = str(el.split('.')[-1])
        if FILE_EXT == ext:
            element_list.append(os.path.join(ELEMENTS, el))
    print('Found', str(len(element_list)), 'files')
    return element_list


def HIT_EM_WITH_IT(element_list):
    HIT = os.path.join(CDHIT, 'cd-hit-est')
    for family in element_list:
        output = os.path.join(OUT_DIR, os.path.basename(family).split('.')[0])
        cmd = [HIT, '-i', family, '-o', output,
               '-sc', '-sf', '-T', '6', '-d', '60']
        string = ''
        for letter in cmd:
            string += str(letter + ' ')
        os.system(string)
        # print(string)
        #subprocess.call(cmd, shell=True)
        # for some reason subprocess not working ???

        print('File written to', output)


HIT_EM_WITH_IT(get_element_files())
