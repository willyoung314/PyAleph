'''

inspired by PyILP: https://github.com/danyvarghese/PyILP
'''


from sklearn.base import BaseEstimator
import numpy as np
import sys
import os
from pathlib import Path
import uuid
import subprocess
import pandas as pd
from sklearn.metrics import (
    confusion_matrix, 
    classification_report,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

def read_pl_file(file_location):
    '''
    Takes a prolog file and ouputs list of all the lines.
    '''
    with open(file_location, 'r') as file:
        #reads file and ignores blank and %
        lines = [line.strip() for line in file if line.strip() and not line.startswith('%')]

        return lines

def make_dataset(pos, neg):
    '''
    Turns a list of positive and negative examples into a bool series.
    '''
    examples = pos + neg
    labels = [True] * len(pos) + [False] * len(neg)
    X = pd.Series(examples, name='example')
    y = pd.Series(labels, name='label')
    return X,y

def split_dataset(X, y):
    '''
    Turns bool series into lists of positive and negative examples for prolog.
    '''
    pos = X[y].tolist()
    neg = X[~y].tolist()
    return pos, neg


def generate_theory_aleph(background, settings, X_train, y_train, X_test):

    pos_fold_ex, neg_fold_ex = split_dataset(X_train, y_train)
    
    aleph_swipl = [":- use_module(aleph).", 
                   ":- if(current_predicate(use_rendering/1)).",
                   ":- use_rendering(prolog).", 
                   ":- endif.", 
                   ":- aleph.",
                   ":-style_check(-discontiguous)."]

    run_id = uuid.uuid4().hex
    dir_path = f"tmp/run_{run_id}"
    os.makedirs(dir_path, exist_ok=True)
    bk_file = f"{dir_path}/aleph_bk_temp.pl"

    with open(bk_file, 'w') as file_1:
        # Write aleph_swipl items
        file_1.write("\n".join(aleph_swipl) + "\n")

        # Write settings items
        file_1.write("\n".join(settings) + "\n")
        
        # Write background block
        file_1.write("\n:-begin_bg.\n")
        file_1.write("\n".join(background) + "\n")
        file_1.write(":-end_bg.\n")
        
        # Write pos_fold_ex block
        file_1.write("\n:-begin_in_pos.\n")
        file_1.write("\n".join(map(str, pos_fold_ex)) + "\n")
        file_1.write(":-end_in_pos.\n")
        
        # Write neg_fold_ex block
        file_1.write("\n:-begin_in_neg.\n")
        file_1.write("\n".join(map(str, neg_fold_ex)) + "\n")
        file_1.write(":-end_in_neg.\n")


    test_file = f"{dir_path}/test.csv"
    X_test.to_csv(test_file)
 #   print(X_test)
    #Calls the prolog engine in a subprocess with run_pyswip_aleph.py to prevent contaminisation.
    result = subprocess.run(
            ["python3", 
             "run_pyswip_aleph.py", 
             bk_file,
             test_file],
            capture_output=True,
            text=True
        )
    print(result.stderr)

    test = pd.read_csv(test_file, index_col=0)
    theory = []
    
 #   print(test)
    # f = open("theory.txt")
    
    # for line in f.read().splitlines():
    #     theory.append(line)
        
    print(test)
    import shutil

    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
        
    return theory, test['label']




class aleph_model:
    '''
    Contains all the data for an aleph model allowing easy calling of other pyaleph function with the methods.
    '''
    def __init__(self, background, settings):

        self.background = background
        self.settings = settings

    def train_fit(self, X_train, y_train, X_test):
        theory, y_pred = generate_theory_aleph(
            self.background, 
            self.settings,
            X_train, 
            y_train, 
            X_test
        )
        self.theory = theory
        self.y_pred = y_pred


    def eval(self, y_test):
        y_pred = self.y_pred
        self.metrics = {
            'accuracy'  : accuracy_score(y_test, y_pred),
            'precision' : precision_score(y_test, y_pred),
            'recall'    : recall_score(y_test, y_pred),
            'f1'        : f1_score(y_test, y_pred),
            'cm'        : confusion_matrix(y_test, y_pred),
            'cr'        : classification_report(y_test, y_pred)
           # 'cr'        : classification_report(y_test, y_pred, target_names=['non-carcinogenic', 'carcinogenic'])
        }
        
        print(self.metrics['cr'])

class aleph_wrapper(BaseEstimator):
    '''
    to run in scikitlearn gridsearch, a bit janky, don't use for anything else because everything happens in score method
    '''

    def create_settings(self):
        settings = [
            f':- aleph_set(noise,{self.noise}).',
            f':- aleph_set(minpos,{self.minpos}).',
            f':- aleph_set(clauselength,{self.clauselength}).',
            f':- aleph_set(search,{self.search}).',
            f':- aleph_set(i,{self.i}).',
            ':- style_check(-singleton).',
            ':- style_check(-discontiguous).'
        ]
        select_modes = set()
        if self.bg_pick[0] == 'all':
            select_modes.update(self._modes)
        else:
            self.bg_pick.append('modeh')
            for bg in self.bg_pick:
                select_modes.update([line for line in self._modes if bg in line])
    
        settings += list(select_modes)    
        self.settings = settings
    #    print(settings)
    def __init__(self, noise = 0, minpos = 1, i = 2, clauselength = 4, search = 'bf', bg_pick = ['all'], _modes = None, _background = None):

        
        self._background = _background
        self._modes = _modes
        self.run = False
        self.noise = noise
        self.i = i
        self.bg_pick = bg_pick
        self.minpos = minpos
        self.search = search
        self.clauselength = clauselength
        
        
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
        return self

        
    def score(self, X, y):
        self.create_settings()
        theory, y_pred = generate_theory_aleph(
            self._background, 
            self.settings,
            self.X_train, 
            self.y_train, 
            X
        )
        # print(y)
        # print(y_pred)
        self.theory = theory
        self.run = True
        return accuracy_score(y, y_pred)
        
def read_dataset(path):
    path = Path(path)

    background = []
    for file in path.glob('*.b'):
        background += read_pl_file(file)

    pos_examples = []
    for file in path.glob('*.f'):
        pos_examples += read_pl_file(file)

    neg_examples = []
    for file in path.glob('*.n'):
        neg_examples += read_pl_file(file)

    # Puts settings in a different list
    modes = [line for line in background if 'determination' in line or 'mode' in line]
    background = [line for line in background if line not in modes]

    modes = [':' + line[1:] if line.startswith('!') else line for line in modes]
            
    X, y = make_dataset(pos_examples, neg_examples)
    dataset = {
        'background' : background,
        'modes' : modes,
        'examples' : X,
        'labels' : y,
    }
    
    return dataset
    
def read_carc_dataset(path):
    '''
    Loads the data from the folder into python lists
    data source: https://github.com/mdrl/datasets/tree/master/aleph/carcinogenesis
    '''
    # Load background file and examples
    background = read_pl_file(f'{path}carcinogenesis.b')
    pos_examples = read_pl_file(f'{path}carcinogenesis.f')
    neg_examples = read_pl_file(f'{path}carcinogenesis.n')
    
    # Puts settings in a different list
    modes = [line for line in background if 'determination' in line or 'mode' in line]
    background = [line for line in background if line not in modes]

    #  Remove reference to other background files and loads them
    background.remove(':- [atoms,bonds,ames,newgroups,gentoxprops,ind_pos,ind_nos].')
    pl_files = ['ames', 'atoms', 'bonds', 'gentoxprops', 'ind_nos', 'ind_pos', 'newgroups']
    for file in pl_files:
        background += read_pl_file(f'{path}{file}.pl')
    
    #creates a dict with background info and X y
    X, y = make_dataset(pos_examples, neg_examples)
    dataset = {
        'background' : background,
        'modes' : modes,
        'examples' : X,
        'labels' : y,
    }
    return dataset