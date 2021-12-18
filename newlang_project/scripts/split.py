
"""Load inception conllu data and split into train and test files"""
import srsly
import typer
import warnings
from pathlib import Path

import spacy
from spacy.tokens import DocBin
from spacy.util import filter_spans
from sklearn.model_selection import train_test_split


def split(export_path: str, test_size:float, random_state:int):
    export_path = Path.cwd() / export_path
    assert entities_path.exists()
    #TODO load all conllu file, make list that can be split 
    # split should be stratified so that text-types are evenly distributed in the training data https://scikit-learn.org/stable/modules/cross_validation.html#stratification
    #train_set, validation_set = train_test_split(docs, test_size=test_size)
    #print(f'Created {len(train_set)} training docs')
    #print(f'Created {len(validation_set)} validation docs')
    

if __name__ == "__main__":
    typer.run(split)
