"""
IMDB Movie Reviews Word Cloud Project
Author: Sameer Gupta

Description:
This project reads an IMDB movie reviews dataset, performs text cleaning,
and generates a word cloud that visualizes the most frequent words
in the reviews.

Libraries used: pandas, re, matplotlib, wordcloud
"""

# ==============================
# 📦 Import Required Libraries
# ==============================
import pandas as pd
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os

# ==============================
# ⚙️ Configuration
# ==============================
DATA_PATH = 'data/IMDB-Dataset.csv'
OUTPUT_DIR = "output/"
OUTPUT_FILE = "imdb_wordcloud.png"

# ==============================
# 🧩 Step 1 — Load Dataset
# ==============================
print("📥 Loading dataset...")
df = pd.read_csv(DATA_PATH)

print(f"✅ Dataset loaded successfully! Total rows: {len(df)}")
print("Columns available:", list(df.columns))
print("\nSample Review:\n", df['review'][0][:300], "...\n")

# ==============================
# 🧹 Step 2 — Clean Text
# ==============================
print("🧹 Cleaning text...")

# Combine all reviews into one string
text = ' '.join(df['review'].astype(str).tolist())

# Remove non-alphabetic characters
text = re.sub(r'[^A-Za-z\s]', '', text)

# Convert to lowercase
text = text.lower()

# Remove stopwords
stopwords = set(STOPWORDS)
cleaned_text = ' '.join(word for word in text.split() if word not in stopwords)

print("✅ Text cleaned successfully!")

# ==============================
# ☁️ Step 3 — Generate Word Cloud
# ==============================
print("🎨 Generating Word Cloud...")

wordcloud = WordCloud(
    width=1000,
    height=500,
    background_color='white',
    max_words=200,
    colormap='coolwarm'
).generate(cleaned_text)

# Display
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("IMDB Movie Reviews Word Cloud", fontsize=18)
plt.show()

# ==============================
# 💾 Step 4 — Save Output
# ==============================
os.makedirs(OUTPUT_DIR, exist_ok=True)
output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
wordcloud.to_file(output_path)

print(f"✅ Word Cloud image saved to: {output_path}")
