    from pyswip import Prolog
import sys
import pandas as pd

# def aleph_learn():
#     prolog = Prolog()
#     print(list(prolog.query('listing()')))
#     prolog.assertz('parent(john,mary)')
#     print(list(prolog.query('listing()')))
#     return 5

# def run_aleph(dataset_path):
#     prolog = Prolog()
#     prolog.consult("aleph.pl")       # Load Aleph
#     prolog.consult(dataset_path)     # Load your dataset
#     list(prolog.query("induce."))    # Run induction
#     for sol in prolog.query("hypothesis(H)."):
#         print("Hypothesis:", sol["H"])


def induce_aleph(dataset, testset):
    prolog = Prolog()
    prolog.consult(dataset)
    #calling it with list is required to execute a query, not the case with consult
    list(prolog.query("induce(a)"))
    list(prolog.query("aleph:write_rules('theory.txt',a)"))
    
    if testset:
        
        #function for getting predictions
        def query_prolog(example): 
            return bool(list(prolog.query(example)))
        # Loads the saved test set and assigns the predicted value before saving again
        test = pd.read_csv(testset, index_col=0)
        test['label'] = test['example'].apply(query_prolog)
        test.to_csv(testset)
    
    


if __name__ == "__main__":
    
    dataset = sys.argv[1]
    testset = sys.argv[2]
    
    induce_aleph(dataset, testset)
