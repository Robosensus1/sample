#!/bin/bash

echo "++++++++++ TRAINING MODELS ++++++++++"
python train.py --nlu --dial


echo "++++++++++ EXTRACT CREDENTIALS ++++++++++"
sh ./generate_credentials.sh > credentials.yml


echo "++++++++++ STARTING SERVER ++++++++++"
python -m rasa_core.run -d models/dialogue -u models/current/nlu  --port $PORT --credentials credentials.yml
