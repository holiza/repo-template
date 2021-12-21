
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


def convert(export_path: str, n_sents:int, lang:str):

    lang = get_lang_class(lang)
    nlp = lang()

    export_path = Path(export_path)
    assert export_path.exists()
    
    conllu_files = [f for f in export_path.iterdir() if f.suffix == ".conllu"]
    #convert conllu to .spacy 
    for conllu in conllu_files:
        subprocess.run(['python', '-m', 'spacy', 'convert', f'{str(conllu)}', "./corpus/conllu", f"-n {n_sents}"])
        
    conll_files = [f for f in export_path.iterdir() if f.suffix == ".conll"]
    #convert conll to .spacy 
    for conll in conll_files:
        subprocess.run(['python', '-m', 'spacy', 'convert', f'{str(conll)}', "./corpus/conll", f"-n {n_sents}"])

    conllu = [f.stem for f in conllu_files]
    conll  = [f.stem for f in conll_files]
    matches = [x for x in conllu if x in conll] 
    
    for file_ in conllu_files:
        if file_.stem in matches:
            conllu_file = export_path / (match + '.conllu')
            conllu_bin = DocBin().from_bytes(conllu_file.read_bytes())
            conllu_docs = [d for d in conllu_bin.get_docs(nlp.vocab)]

            conll_file = export_path / (match + '.conll')
            conll_bin = DocBin().from_bytes(conll_file.read_bytes())
            conll_docs = [d for d in conll_bin.get_docs(nlp.vocab)]

            joined_docs = []
            for ling, ner in zip(conllu_docs, conll_docs):
                ling.ents = ner.ents
                joined_docs.append(ling)
        else:
            subprocess.run(['cp', f'{str(file_)}', f"./corpus/converted/{str(file_.name)}" ])
            
        # works?
        
if __name__ == "__main__":
    typer.run(convert)
