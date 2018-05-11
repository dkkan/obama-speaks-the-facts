import os
import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup


app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText().strip()


@app.route('/')
def home():
    """
    Executes POST request
    :url: http://talkobamato.me/synthesize.py
    :data: input_text=This+is+a+small+change%2C+but+a+big+move+for+us.+140+was+an+arbitrary+choice+based+on+the+160+
    character+SMS+limit.+Proud+of+how+thoughtful+the+team+has+been+in+solving+a+real+problem+people+have+when+trying+
    to+tweet.+And+at+the+same+time+maintaining+our+brevity%2C+speed%2C+and+essence%21
    :return:
    """

    r = requests.post(url="http://talkobamato.me/synthesize.py",
                      data={'input_text': get_fact()},
                      allow_redirects=False)

    return r.headers['Location']


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

