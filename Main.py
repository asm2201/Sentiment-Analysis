import string
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('all')

text = open('Speech.txt', encoding='UTF-8').read()
lower = text.lower()
cleaned_text = lower.translate(str.maketrans('', '', string.punctuation))

'''tokenization is breaking up of a sentence into small words'''
tokenized_words = word_tokenize(cleaned_text, "english")
'''stop words are the words that don't add any meaning to the sentence. They can be removed'''
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
'''removing stop words from our text'''
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)
'''reading emotions.txt'''
'''if the emotion is present in current text, add it tp emotions_list'''
emotion_list = []
file =  open('emotions.txt', 'r') 
for line in file:
    clean_line = line.replace("\n",'').replace(",", '').replace("'",'').replace(" ",'').strip()
    word, emotion = clean_line.split(':')
    if word in final_words:
        emotion_list.append(emotion)
print(emotion_list)
'''check the number of times an emotion appears in emotion list'''
w = Counter(emotion_list)
print(w)

def sentimentAnalyser(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    negativeEmotion = score['neg']
    positiveEmotion = score['pos']
    if (negativeEmotion > positiveEmotion):
        print("Negative")
    elif(positiveEmotion > negativeEmotion):
        print("Positive")
    else:
        print("Neutral")
    print(score)

sentimentAnalyser(cleaned_text)

'''creating a bar graph'''
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
#plt.savefig('graph.png')
plt.show()
