
"""Load inception conllu data and convert to spaCy binary format (DocBin)"""
import srsly
import typer
import warnings
from pathlib import Path
import subprocess

import spacy
from spacy.tokens import DocBin
from spacy.util import filter_spans, get_lang_class
from sklearn.model_selection import train_test_split


def convert(export_path: str, n_sents:int=None, lang:str):

    lang = get_lang_class(lang)
    nlp = lang()

    export_path = Path(export_path)
    assert export_path.exists()
    
    conllu_files = [f for f in export_path.iterdir() if f.suffix == ".conllu"]
    #convert conllu to .spacy 
    for conllu in conllu_files:
        subprocess.run(['python', '-m', 'spacy', 'convert', f'{str(conllu)}', "./corpus/conllu", "-n 10"])
        
    conll_files = [f for f in export_path.iterdir() if f.suffix == ".conll"]
    #convert conll to .spacy 
    for conll in conll_files:
        subprocess.run(['python', '-m', 'spacy', 'convert', f'{str(conll)}', "./corpus/conll", "-n 10"])
    #TODO identify 
    

if __name__ == "__main__":
    typer.run(convert)
