import pandas as pd
import numpy as np
import re
import warnings
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from konlpy.tag import Okt 
# nltk.download('all') # 처음 실행 시 주석 제거
warnings.filterwarnings(action='ignore')

# 결측치 확인과 데이터 확인은 filetest에서 진행

# data road
train = pd.read_csv("./dataset/train.csv")
test = pd.read_csv("./dataset/test.csv")
submission = pd.read_csv("./dataset/sample_submission.csv")

# ??
trainset, valset = train_test_split(train)
# 전처리 과정에서 데이터가 뒤섞이지 않도록 인덱스 초기화
trainset.reset_index(inplace=True)
valset.reset_index(inplace=True)

# cread preprocessed column and remove asterisk
trainset['preprocessed'] = trainset['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
trainset['preprocessed'] = trainset['preprocessed'].str.replace(" +", " ")

# tokenize
tokenized = [] # new column
for sentence in trainset['preprocessed']:
    tokens = okt.morphs(sentence, stem = True) # 형태소 분석 (stem = True로 설정해 어간 추출)
    tokenize = " ".join(tokens) # 띄어쓰기 단위로 합침
    tokenized.append(tokenize) # 형태소 단위로 띄어쓰기된 문자열 추가
trainset["tokenized_stem"] = pd.DataFrame(tokenized)

# POS Tagging
main_pos = [] # new column
for sentence in trainset['document']:
    pos = okt.pos(sentence) # 분석된 리스트 = pos
    # ?? taking Noun, Adverb, Adjective, Verb
    main_words = [word_pos[0] for word_pos in pos if word_pos[1] in ("Noun", "Adverb", "Adjective", "Verb")]
    main_words_str = " ".join(main_words)
    main_pos.append(main_words_str)
trainset["main_pos"] = pd.DataFrame(main_pos)

# vectorizer
X_train = train.main_pos
y_train = train.label
vectorizer = CountVectorizer()
vectorizer.fit(X_train)
X_train_vec = vectorizer.transform(X_train)

# learning model
model = LogisticRegression()
model.fit(X_train_vec, y_train)