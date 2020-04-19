from textblob import TextBlob

wiki = TextBlob("Python is a high-level, general-purpose programming language.")

print(wiki.tags)
print(wiki.noun_phrases)
testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
monty = TextBlob("We are no longer the Knights who say Ni. "
                "We are now the Knights who say gotcha gotcha gotcha PTANG.")
print(testimonial.sentiment)
print(testimonial.sentiment.polarity)
zen = TextBlob("Beautiful is better than ugly. and the " 
                "Explicit is better than implicit.and the "
               "Simple is better than complex.")
print(zen.words)
print(zen.sentences)
print(monty.word_counts['gotcha'])
