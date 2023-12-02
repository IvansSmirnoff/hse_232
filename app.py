from flask import Flask, request, render_template
import pandas as pd

from utils import check_hypothesis, locate_genres


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('check.html')

@app.route('/plots')
def plots():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def check():
    our_string = [str(x) for x in request.form.values()][0].split(',')
    columns = [s.strip() for s in our_string]
    print(columns)
    df = pd.read_csv('data/games.csv')

    return render_template(
        'check.html',
        result=check_hypothesis(
            *locate_genres(df, columns[0], columns[1])
        ),
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
