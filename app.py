# coding=UTF8
from flask import Flask, jsonify
import BankofTaiwan

app = Flask(__name__)


@app.route("/", methods=['GET'])
def get_rate():
    return jsonify(BankofTaiwan.rates())


if __name__ == "__main__":
    app.run(debug=False)
