# coding=UTF8
from flask_api import FlaskAPI
import BankofTaiwan

app = FlaskAPI(__name__)


@app.route("/", methods=['GET'])
def get_rate():
    return BankofTaiwan.rates()


if __name__ == "__main__":
    app.run(debug=True)
