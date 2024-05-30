from flask import Flask, jsonify, render_template
from flask_cors import CORS
import requests
from textblob import TextBlob
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

# @app.route("/myfav")
# def myfav():
# 	return render_template("myfav.html")

@app.route("/", methods=['GET'])
def get_sentiment_analysis():
	# Grab text from quotes web page
	data = requests.get("http://quotes.toscrape.com/tag/inspirational/")

	# Add contents
	data_scraping = BeautifulSoup(data.content, "html.parser")
	spans = data_scraping.select(".text")

	# Initialize empty list to store sentiment analysis results
	sentiment_analysis_results = []

	# Loop through the data and perform sentiment analysis
	for span in spans:
		quote = TextBlob(span.text)
		quote_score = round(quote.sentiment.polarity, 2)

		sentiment_analysis_results.append({
			"quote": span.text,
			"sentiment_analysis": quote_score,
		})

	# Render HTML template with sentiment analysis results
	return render_template("sentiment_template.html", results=sentiment_analysis_results)


if __name__ == "__main__":
	# Run the app on port 5000
	app.run(host='0.0.0.0', port=5001)
