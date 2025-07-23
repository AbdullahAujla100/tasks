from wordcloud import WordCloud
import os
import matplotlib.pyplot as plt

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "mytext.txt")
with open(file_path, "r") as file:
    text = file.read()

wordcloud = WordCloud(width=700, height=450, background_color='black').generate(text)


plt.figure(figsize=(12,7))
plt.imshow(wordcloud,interpolation="bilinear") 
plt.axis('off')  
plt.title("Word Cloud Example", fontsize=20,color="blue")
plt.show()
