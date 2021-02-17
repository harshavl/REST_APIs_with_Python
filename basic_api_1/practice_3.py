
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [{
        'name': 'MyStore',
        'items': [
                {'name': 'my item',
                 'price': 15.99 
                 } ]
        }]


@app.route('/')
def home():
    return render_template('index.html')


# POST - used to recive the data
# GET - used to send the data back

# POST /store data:{name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass


# GET /store/<string:name>
@app.route('/store/<string:name>' )
def get_store():
    pass

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({ 'stores': stores })


# POST /store/<string:name>/item {name:, price: }
@app.route('/store/<string:name>', methods=['POST'] )
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass



app.run(port=5000)
