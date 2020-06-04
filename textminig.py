text="the sky is blue.there are kites,flying in the sky.there are clouds in the sky."
from nltk.tokenize import sent_tokenize
sent=sent_tokenize(text)
from nltk.tokenize import word_tokenize
word=word_tokenize(text)
punct=":;'!$%@\/*[].,"
w=""
for i in text:
    if i not in punct:
        w=w+i
w=w.lower()
word=word_tokenize(w)
from nltk.corpus import stopwords
sw=set(stopwords.words("english"))
filtered=[]
for i in word:
    if i not in sw:
        filtered.append(i)
from nltk.probability import FreqDist
fr=FreqDist(filtered)
fr.plot(10)
t=str(filtered)
punct=":;'!$%@\/*[].,"
w=""
for i in t:
    if i not in punct:
        w=w+i
w=w.lower()
from wordcloud import WordCloud
wc=WordCloud()
wc.generate(text)
plt.imshow(wc)