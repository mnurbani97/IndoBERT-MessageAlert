# -*- coding: utf-8 -*-
"""IndoBERT-Transformers_Text-Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NBA5rpDYhEP5LrdsNbrbuNA_IG4h3CqJ

# **Get Data and Libraries**
"""

! wget https://raw.githubusercontent.com/gevabriel/dataset/main/indo_spam.csv

! pip install -U accelerate

! pip install -U transformers

! pip install datasets

"""# **Import Data**"""

import pandas as pd
from nltk.tokenize import word_tokenize
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
!pip install pysastrawi
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from transformers import AutoModelForSequenceClassification
from transformers import Trainer
from datasets import load_metric

"""# **Load Data**"""

df = pd.read_csv('indo_spam.csv')
df

df.info()

"""## **Data Cleaning**"""

df['Kategori'].value_counts()

df.isnull().sum()

duplicates = df[df.duplicated(keep=False)]
print("Duplicate Rows:\n", duplicates)

df_cleaned = df.drop_duplicates()

# Display the number of duplicates removed
print(f"Number of duplicates removed: {df.duplicated().sum()}")
print("Cleaned DataFrame:\n", df_cleaned.head())

df.shape

"""# **Data Text Processing**"""

df2 = df.copy()

df2['label'] = df2['Kategori'].replace({ 'spam':0,  'ham':1 })
df2

# Define Stopwords
stpwds_id = list(set(stopwords.words('indonesian')))
stpwds_id.append('oh') # Cara lain dari "stpwds_id = stpwds_id + ['oh']"

# Define Stemming
stemmer = StemmerFactory().create_stemmer()

# Create A Function for Text Preprocessing

def text_preprocessing(text):
  # Case folding
  text = text.lower()

  # Mention removal
  text = re.sub("@[A-Za-z0-9_]+", " ", text)

  # Hashtags removal
  text = re.sub("#[A-Za-z0-9_]+", " ", text)

  # Newline removal (\n)
  text = re.sub(r"\\n", " ",text)

  # Whitespace removal
  text = text.strip()

  # URL removal
  text = re.sub(r"http\S+", " ", text)
  text = re.sub(r"www.\S+", " ", text)

  # Non-letter removal (such as emoticon, symbol (like μ, $, 兀), etc
  text = re.sub("[^A-Za-z\s']", " ", text)

  # Tokenization
  tokens = word_tokenize(text)

  # Stopwords removal
  tokens = [word for word in tokens if word not in stpwds_id]

  # Stemming
  tokens = [stemmer.stem(word) for word in tokens]

  # Combining Tokens
  text = ' '.join(tokens)

  return text

df

df['Pesan_processed'] = df['Pesan'].apply(lambda x: text_preprocessing(x))
df

"""# **Exploratory Data Analysis**"""

df2 = df2.rename(columns={'Pesan_processed': 'Pesan_processed', 'label':'label'})
df2['label'] = df2['label'].map({0: 0.0, 1: 1.0})
# # Output first five rows
df2.head()

df2.groupby('label').count().plot(kind='bar')

import matplotlib.pyplot as plt
import seaborn as sns


fig = plt.figure(figsize=(14,7))
df2['length'] = df.Pesan_processed.str.split().apply(len)
ax1 = fig.add_subplot(122)
sns.histplot(df2[df2['Kategori']=='spam']['length'], ax=ax1,color='red')
describe = df2.length[df2.Kategori=='spam'].describe().to_frame().round(2)

ax2 = fig.add_subplot(121)
ax2.axis('off')
font_size = 14
bbox = [0, 0, 1, 1]
table = ax2.table(cellText = describe.values, rowLabels = describe.index, bbox=bbox, colLabels=describe.columns)
table.set_fontsize(font_size)
fig.suptitle('Distribution of text length for Spam Kategori Message.', fontsize=16)

fig = plt.figure(figsize=(14,7))
df2['length'] = df.Pesan_processed.str.split().apply(len)
ax1 = fig.add_subplot(122)
sns.histplot(df2[df2['Kategori']=='ham']['length'], ax=ax1,color='green')
describe = df2.length[df2.Kategori=='ham'].describe().to_frame().round(2)

ax2 = fig.add_subplot(121)
ax2.axis('off')
font_size = 14
bbox = [0, 0, 1, 1]
table = ax2.table(cellText = describe.values, rowLabels = describe.index, bbox=bbox, colLabels=describe.columns)
table.set_fontsize(font_size)
fig.suptitle('Distribution of text length for Ham Kategori Message.', fontsize=16)

plt.show()

"""# **Feature Engineering**"""

df['label'] = df['Kategori'].apply(lambda x:0 if x=="ham" else 1)

df

df = df.drop(columns=['Kategori','Pesan'])
df.rename(columns={"Pesan_processed": "Teks"}, inplace=True)
df

"""# **Data Splitting**"""

RANDOM_SEED = 42

df_train, df_test = train_test_split(
    df,
    test_size=0.2,
    random_state=RANDOM_SEED,
)

df_val, df_test = train_test_split(
    df_test,
    test_size=0.4,
    random_state=RANDOM_SEED,
)

print(f'Total Train: {len(df_train)}')
print(f'Total Val  : {len(df_val)}')
print(f'Total Test : {len(df_test)}')

df_train.to_csv("train.csv", index=False)
df_val.to_csv("eval.csv", index=False)
df_test.to_csv("test.csv", index=False)

from datasets import load_dataset

files = {
    "train": "train.csv",
    "eval": "eval.csv",
    "test": "test.csv",
}

dataset = load_dataset('csv', data_files=files)

"""# **IndoBERT Models**"""

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("indobenchmark/indobert-base-p2")

def tokenize_function(text):
    return tokenizer(text["Teks"], padding='max_length', max_length=256)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

train_dataset = tokenized_datasets["train"]
eval_dataset = tokenized_datasets["eval"]

import torch
torch.cuda.empty_cache()

device = "cuda:0" if torch.cuda.is_available() else "cpu"
device

model = AutoModelForSequenceClassification.from_pretrained("indobenchmark/indobert-base-p2", num_labels=3)

from transformers import TrainingArguments
from torch import clamp

training_args = TrainingArguments(
    "test_trainer",
    per_device_train_batch_size=4,
)

metric = load_metric("accuracy")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)

    return metric.compute(predictions=predictions, references=labels)

torch.cuda.empty_cache()

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    compute_metrics=compute_metrics,
)

training_history = trainer.train()

import numpy as np

evaluation_history = trainer.evaluate()
evaluation_history

test_dataset = tokenized_datasets["test"]

prediction = trainer.predict(test_dataset)
prediction = prediction.predictions.argmax(1)

actual_label = df_test['label']

print(classification_report(prediction, actual_label, target_names=["0", "1"]))

def show_confusion_matrix(confusion_matrix):
        hmap = sns.heatmap(confusion_matrix, annot=True, fmt="d", cmap="Blues")
        hmap.yaxis.set_ticklabels(hmap.yaxis.get_ticklabels(), rotation=0, ha='right')
        hmap.xaxis.set_ticklabels(hmap.xaxis.get_ticklabels(), rotation=30, ha='right')

        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')

cm = confusion_matrix(prediction, actual_label)
show_confusion_matrix(cm)

model.save_pretrained("model")

model = AutoModelForSequenceClassification.from_pretrained("model")

trainer = Trainer(model=model)

def predict(text):
    tokenized = tokenizer(text, padding='max_length', max_length=256)
    label = trainer.predict([tokenized]).predictions.argmax(1)[0]
    if label == 0:
        print(f'Predicted: Ham [{label}]')
    else:
        print(f'Predicted: Spam [{label}]')

predict("""
Apapun profesimu, pasti ada risiko kerjanya. Ayo segera daftar jadi peserta BPJS Ketenagakerjaan biar bisa #KerjaKerasBebasCemas. www.bpjsketenagakerjaan.go.id
""")

predict("""
    Assalamualaikum Pak. Ini dg nama1 ilkom 2012. Maaf Pak td saya ninggalin proposal di meja Bapak di atas printer. Terima kasih Pak.
""")