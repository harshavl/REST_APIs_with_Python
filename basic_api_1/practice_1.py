
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [{
        'name': 'MyStore',
        'items': [{'name': 'my item', 'price': 15.99 } ]
        }]


@app.route('/')
def home():
    return render_template('index.html')


# POST - used to recive the data
# GET - used to send the data back


# GET /store/<string:name>
# GET /store
# POST /store/<string:name>/item {name:, price: }
# GET /store
# POST /store/<string:name>/item {name:, price: }
# GET /store/<string:name>/item



app.run(port=5000)
