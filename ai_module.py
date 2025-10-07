from textblob import TextBlob
def analyze_feedback(text):
    sentiment=TextBlob(text).sentiment.polarity
    return round(sentiment,2)