import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    #Membuat title
    # st.title('Text-Based Twitter Sentiment Analysis')

    #Tambahkan gambar
    image = Image.open('ecentrix.png')
    st.image(image, caption = 'eCentrix Solutions')

    #Membuat garis
    # st.markdown('----')

    #Masukkan pandas dataframe

    #Show dataframe
    df = pd.read_csv('../spam.csv')
    # st.dataframe(df)
    # st.write('Source : https://www.kaggle.com/datasets/yasserh/twitter-tweets-sentiment-dataset')

    st.markdown('----')
    st.title('Exploratory Data Analysis')
    st.write('Comming Soon!')
    st.markdown('----')
    st.title('Model Architecture')
    st.markdown('----')
    image = Image.open('LSTM.png')
    st.image(image, caption = 'LSTM Model Architecture')
    #Bar Plot
    # st.write('#### Distribution of Sentiments')
    # fig_sentiments = plt.figure(figsize=(10, 6))
    # sns.countplot(x='sentiment', data=df)
    # plt.xlabel('Sentiment Label')
    # plt.ylabel('Count')
    # plt.title('Distribution of Sentiments')
    # st.pyplot(fig_sentiments)

    # # Positive Sentiment Tweets Bar
    # st.write('#### Distribution of Text Length for Positive Sentiment Tweets')
    # fig_length_positive = plt.figure(figsize=(14, 7))

    # # Handle NaN values in 'text_processed'
    # df['length'] = df['text_processed'].apply(lambda x: len(str(x).split()) if pd.notna(x) else 0)

    # ax1 = fig_length_positive.add_subplot(122)
    # sns.histplot(df[df['sentiment']=='positive']['length'], ax=ax1, color='green')
    # describe_positive = df.length[df.sentiment=='positive'].describe().to_frame().round(2)

    # ax2 = fig_length_positive.add_subplot(121)
    # ax2.axis('off')
    # font_size = 14
    # bbox = [0, 0, 1, 1]
    # table_positive = ax2.table(cellText=describe_positive.values, rowLabels=describe_positive.index, bbox=bbox, colLabels=describe_positive.columns)
    # table_positive.set_fontsize(font_size)
    # fig_length_positive.suptitle('Distribution of text length for positive sentiment tweets.', fontsize=16)

    # st.pyplot(fig_length_positive)

    # # negative Sentiment Tweets Bar
    # st.write('#### Distribution of Text Length for negative Sentiment Tweets')
    # fig_length_negative = plt.figure(figsize=(14, 7))

    # # Handle NaN values in 'text_processed'
    # df['length'] = df['text_processed'].apply(lambda x: len(str(x).split()) if pd.notna(x) else 0)

    # ax1 = fig_length_negative.add_subplot(122)
    # sns.histplot(df[df['sentiment']=='negative']['length'], ax=ax1, color='red')
    # describe_negative = df.length[df.sentiment=='negative'].describe().to_frame().round(2)

    # ax2 = fig_length_negative.add_subplot(121)
    # ax2.axis('off')
    # font_size = 14
    # bbox = [0, 0, 1, 1]
    # table_negative = ax2.table(cellText=describe_negative.values, rowLabels=describe_negative.index, bbox=bbox, colLabels=describe_negative.columns)
    # table_negative.set_fontsize(font_size)
    # fig_length_negative.suptitle('Distribution of text length for negative sentiment tweets.', fontsize=16)

    # st.pyplot(fig_length_negative)

    # # neutral Sentiment Tweets Bar
    # st.write('#### Distribution of Text Length for neutral Sentiment Tweets')
    # fig_length_neutral = plt.figure(figsize=(14, 7))

    # # Handle NaN values in 'text_processed'
    # df['length'] = df['text_processed'].apply(lambda x: len(str(x).split()) if pd.notna(x) else 0)

    # ax1 = fig_length_neutral.add_subplot(122)
    # sns.histplot(df[df['sentiment']=='neutral']['length'], ax=ax1, color='blue')
    # describe_neutral = df.length[df.sentiment=='neutral'].describe().to_frame().round(2)

    # ax2 = fig_length_neutral.add_subplot(121)
    # ax2.axis('off')
    # font_size = 14
    # bbox = [0, 0, 1, 1]
    # table_neutral = ax2.table(cellText=describe_neutral.values, rowLabels=describe_neutral.index, bbox=bbox, colLabels=describe_neutral.columns)
    # table_neutral.set_fontsize(font_size)
    # fig_length_neutral.suptitle('Distribution of text length for neutral sentiment tweets.', fontsize=16)

    # st.pyplot(fig_length_neutral)

    # # Membuat pie chart
    # st.write('#### Pie Chart - Sentiment Distribution')
    # labels = ['Neutral', 'Positive', 'Negative']
    # size = df['sentiment'].value_counts()
    # colors = ['lightgreen', 'lightskyblue', 'lightcoral']
    # explode = [0.01, 0.01, 0.1]

    # fig, axes = plt.subplots(figsize=(6, 5))
    # plt.pie(size, colors=colors, explode=explode,
    #         labels=labels, shadow=True, startangle=90, autopct='%.2f%%')
    # plt.title('Sentiment Distribution', fontsize=20)
    # plt.legend()

    # st.pyplot(fig)
    # #Membuat histogram
    # st.write('#### Histogram of Age')
    # fig = plt.figure(figsize=(15,5))
    # sns.histplot(df['Overall'], bins = 30, kde = True)
    # st.pyplot(fig)

    # #membuat histogram berdasarkan inputan user
    # st.write('#### Histogram berdasarkan input user')
    # #kalo mau pake radio button, ganti selectbox jadi radio
    # option = st.selectbox('Pilih Column : ', ('Age', 'Weight', 'Height', 'ShootingTotal'))
    # fig = plt.figure(figsize= (15,5))
    # sns.histplot(df[option], bins = 30, kde = True)
    # st.pyplot(fig)

    # #Membuat Plotly plot

    # st.write('#### Plotly Plot - ValueEUR vs Overall')
    # fig = px.scatter(df, x = 'ValueEUR', y = 'Overall', hover_data = ['Name', 'Age'])
    # st.plotly_chart(fig)

if __name__ == '__main__':
    run()
