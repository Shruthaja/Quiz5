from collections import Counter

import nltk
from azure.storage.blob import BlobServiceClient
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize

account_url = "DefaultEndpointsProtocol=https;AccountName=shruthaja;AccountKey=FvxC1NCWJQuBHKf77+JJaniZDHYUsBzqjy9H2o2o4INHFJRAXUTl6E3VB+2wXX3SsjFsMy5Vpm/R+ASto6SosQ==;EndpointSuffix=core.windows.net"
blob_account_client = BlobServiceClient.from_connection_string(account_url)
bc = blob_account_client.get_container_client("assignment5").list_blob_names()
for i in bc:
    j = blob_account_client.get_container_client("assignment5").download_blob(i)
    book = str(j.read())
    raw = ' '.join(word_tokenize(book.lower()))

    tokenizer = RegexpTokenizer(r'[A-Za-z]{2,}')
    words = tokenizer.tokenize(raw)

    # remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # count word frequency, sort and return just 20
    counter = Counter()
    counter.update(words)
    most_common = counter.most_common(20)
    book_name = {}
    book_name[i] = most_common
    # print(i,book_name[i])
    print("for specific word")
    counter = Counter()
    counter.update(words)
    most_common = counter.most_common(100)
    book_name = {}
    book_name[i] = most_common
    # print(i, book_name[i])
    book = book.replace("\\r", "").split('\\n')
    for i in book:
        i = i.replace("\\n", "")
        print(nltk.word_tokenize(i, "English"))
        # print(re.sub(r"[^a-zA-Z0-9]+", " ",i))
    exit()
