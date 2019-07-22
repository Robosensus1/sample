""" A set of command line utilities to 
simplify RASA commands eg. to train the models since these 
commands are insanely long. 
"""

import click
from subprocess import call

@click.command()
@click.option('--dial', is_flag=True, help="Train the dialogue model (domain.yml and stories.md)")
@click.option('--nlu', is_flag=True, help="Train the NLU model (nlu.md)")
def train(dial, nlu):
    """
    Train dialogue and/or nlu model (to be done after any change in one of 
    domain.yml, nlu.md, stories.md).
    :param dial: Train the dialogue model (domain.yml and stories.md)
    :param nlu: Train the NLU model (nlu.md)
    :return: None
    """
    if dial:
        call(['python', '-m', 'rasa_core.train', '-d', 'domain.yml', '-s', 'stories.md', '-o', 'models/dialogue', '--verbose'])
    if nlu:
        call(['python', '-m', 'rasa_nlu.train', '-c', 'nlu_config.yml', '--data', 'nlu.md', '-o', 'models', '--fixed_model_name', 'nlu', '--project', 'current', '--verbose'])

        
if __name__ == '__main__':
    train()





