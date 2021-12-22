import typer
from pathlib import Path

import spacy


def update_config():
    config_path = Path('config.cfg') 
    config_text = config_path.read_text()
    config_text = config_text.replace('\ntrain = null\n','\ntrain = "corpus/converted/train.spacy"\n')
    config_text = config_text.replace('\ndev = null\n','\ndev = "corpus/converted/dev.spacy"\n')
    config_path.write_text(config_text)

if __name__ == "__main__":
    typer.run(update_config)
