import nltk
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

nltk.download('stopwords')
nltk.download('punkt')
nltk.download.stopwords('hi')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

example_sent = "तो क्या विश्व कप 2019 में मैच का बॉस टॉस है? यानी मैच में हार-जीत में \
टॉस की भूमिका अहम है? आप ऐसा सोच सकते हैं। विश्वकप के अपने-अपने पहले मैच में बुरी तरह हारने वाली एशिया की दो टीमों \
पाकिस्तान और श्रीलंका के कप्तान ने हालांकि अपने हार के पीछे टॉस की दलील तो नहीं दी, लेकिन यह जरूर कहा था कि वह एक अहम टॉस हार गए थे।"

stop_words = set(stopwords.words('hi'))

word_tokens = word_tokenize(example_sent)
punct_tokens=pun

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)


wordfreq = []
for w in filtered_sentence:
    wordfreq.append(filtered_sentence.count(w))

FreqDist(filtered_sentence)
print("\n\n...................FILTERED SENTENCE...........................\n\n")
print(filtered_sentence)
print("\n\n................FREQUENCY OF WORDS..............................\n\n")
print(wordfreq)

all_fdist = pd.Series(wordfreq)

fig, ax = plt.subplots(figsize=(10,10))
all_plot = sns.barplot(x=filtered_sentence, y=all_fdist.values, ax=ax)
print("\n\n................GRAPHICAL REPRESENTATION..............................\n\n")
plt.xticks(rotation=30);    