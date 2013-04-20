from time import sleep
from flask import Flask


sleep(2)
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()
