# CSC 6810 - Artificial Intelligence Final Research Project

Below are instructions you must follow to successfully run any of the files and code within this project. You may also copy directly from the github repository at https://github.com/Sedwards8900/ai_nlp_project.

# 1. Instructions on how to run the program:

In order to successfully run the file b_model.ipynb, you must first install all required modules by implementing the following command from terminal:

pip install -r requirements.txt

It is recommended that you search for a Jupyter Notebook extension for the used IDE in addition to installing Jupyter Notebooks within the IDE. If working with VS Code, please refer to https://code.visualstudio.com/docs/datascience/jupyter-notebooks for more information.

After all modules have been installed, open the file b_model.ipynb in the folder and run each cell in a descending order (top-bottom). Currently all the program will do is extract the already created files and save them into variables. Otherwise, it has the capacity to create the files once more and run the sentiment analysis model. This file also has comment on each of the steps taken towards implementing the code.

# 2. Installed required dependencies

The following are the modules necessary to run the program:
- twint
- torch
- transformers
- pandas
- googletrans (3.1.0a0 version)

# 3. File organization

## A. This project contains the following data files:
- hurricane_ian.csv: Initial original file containing tweets related to one of the most catastrophic disasters in 2022, Hurricane Ian.
- sa_tweets_eng_original.csv: Sentiment Analysis excel sheet file containing original english tweets, category of tweet, and score.
- sa_tweets_eng_snd.csv: Sentiment Analysis excel sheet file containing english tweets after being translated using Google Translate's API. The file also contains the category of tweet and score.

- spanish_tweets_translated.csv: Excel sheet containing translation of original english tweets into Spanish.

## B. The project contains the following additional files:
- a_dataset.py: Program used to extract tweets via Twint's easy to use API. The file does not need to be ran for purposes of analyzing the model anymore as the data has been provided and stored within the project files.
- b_model.ipynb: Jupyter notebook containing the Sentiment Analysis model code and translator.
