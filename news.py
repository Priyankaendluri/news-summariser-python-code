import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Step 1: Get the news article from a URL
url = "https://www.bbc.com/news/world-asia-68422345"  # replace with any article URL
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Extract all paragraphs from the article
article_text = " ".join([p.get_text() for p in soup.find_all('p')])

# Step 3: Create a parser and summarizer
parser = PlaintextParser.from_string(article_text, Tokenizer("english"))
summarizer = LsaSummarizer()

# Step 4: Generate summary (5 sentences)
summary = summarizer(parser.document, 5)

# Step 5: Print the summarized text
print("\n📰 ORIGINAL ARTICLE TEXT:\n")
print(article_text[:1000] + "...\n")  # show only first 1000 characters

print("🧾 SUMMARY:\n")
for sentence in summary:
    print(sentence)
