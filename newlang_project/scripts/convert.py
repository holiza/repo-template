
"""Load inception conllu data and convert to spaCy binary format (DocBin)"""
import srsly
import typer
import warnings
from pathlib import Path
import subprocess

import spacy
from spacy.tokens import DocBin
from spacy.util import filter_spans
from sklearn.model_selection import train_test_split


def convert(export_path: str, n_sents:int=None, lang:str):

    lang = get_lang_class(lang)
    nlp = lang()

    export_path = Path.cwd() / export_path
    assert export_path.exists()
    conllu_files = [f for f in export_path.iterdir()]
    
    #convert conllu to .spacy 
    for conllu in conllu_files:
        subprocess.run(['python', '-m', 'spacy', 'convert', f'{str(conllu)}', "./corpus", "-n 10"])
        
    

if __name__ == "__main__":
    typer.run(convert)
