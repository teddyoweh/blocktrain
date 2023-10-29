from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import pickle
import pandas as pd
import random
from itertools import combinations
from multiprocessing import Pool
from dask.distributed import Client
import time
data = pd.read_csv('train.csv')
data = data[['Action','Card 1','Card 2','Card 3','Card 4','Played']]
ins = data.drop(['Action'],axis="columns")
outs = data['Action']
def whotmodel():
 
  arrs = [__ for _ in ins.values for __ in _]
  tokens  = {_:i for i,_ in enumerate(set(arrs)) }
  outtokens =  {_:i for i,_ in enumerate(set([_ for _ in list(outs.values)])) }
  insdata = []
  for i in ins.values:
      insdata.append([tokens[_] for _ in i])
  newdf = pd.DataFrame(data=insdata,columns=ins.columns)
  newdf.head()
  model = RandomForestClassifier()
  model.fit(newdf,outs)
  return model

arrs = [__ for _ in ins.values for __ in _]

tokens  = {_:i for i,_ in enumerate(set(arrs)) }

def callmodel(cards,played,model1):
  cards.sort()
  card1,card2,card3,card4 = cards
  return model1.predict([[tokens[card1],tokens[card2],tokens[card3],tokens[card4],tokens[played]]])[0]
def save_object_to_file(obj, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(obj, file)
        print(f"Object saved to {filename} successfully.")
    except Exception as e:
        print(f"An error occurred while saving the object: {str(e)}")

def main():
    model = whotmodel()
    save_object_to_file(model, 'mode.pkl')
    save_object_to_file(tokens, 'tokens.pkl')
    print("Done")
 
 
client =  Client('10.66.106.228:8786')  
start_time = time.time()
futures = client.submit(main)
result = futures.result()
end_time = time.time()