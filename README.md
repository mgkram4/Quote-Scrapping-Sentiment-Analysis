# Sentiment Analysis Web App

This is a simple web application that performs sentiment analysis on inspirational quotes from the [Quotes to Scrape](http://quotes.toscrape.com/) website.

## Features

- Scrapes inspirational quotes from the Quotes to Scrape website
- Performs sentiment analysis on each quote using the TextBlob library
- Displays the quotes and their corresponding sentiment analysis scores on a web page

## Technologies Used

- Flask (Python web framework)
- Flask-CORS (for handling Cross-Origin Resource Sharing)
- Requests (for making HTTP requests)
- TextBlob (for performing sentiment analysis)
- BeautifulSoup (for web scraping)

## Installation and Setup

1. Clone the repository:
git clone https://github.com/your-username/sentiment-analysis-webapp.git

2. Navigate to the project directory:
cd sentiment-analysis-webapp

3. Create a virtual environment (optional, but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

4. Install the required dependencies:
pip install -r requirements.txt

5. Run the Flask application:
python app.py

6. Open your web browser and navigate to `http://localhost:5001/` to see the sentiment analysis results.

## Usage

The web application fetches inspirational quotes from the Quotes to Scrape website and performs sentiment analysis on each quote. The sentiment analysis score ranges from -1 (negative) to 1 (positive), with 0 being neutral.

The results are displayed on a web page, showing the quote and its corresponding sentiment analysis score.

## Future Improvements

- Add user input to allow for custom text to be analyzed
- Implement more advanced sentiment analysis techniques
- Improve the web page design and user interface

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
