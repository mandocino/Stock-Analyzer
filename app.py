from flask import Flask, render_template
import yfinance as yahooFinance

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('analyzerHomepage.html')

@app.route('/analyze/<query>', methods=['GET'])
def analyze(query):
    GetTickerInformation = None
    try:
        app.logger.debug(query)
        GetTickerInformation = yahooFinance.Ticker(query)
        return render_template('stockAnalyzed.html', GetTickerInformation=GetTickerInformation)
    except:
        return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True)
