import os
import uuid
import stripe
import firebase_admin

from firebase_admin import credentials
from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'publisher': post_data.get('publisher'),
            'instock': post_data.get('instock'),
						'price': post_data.get('price')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)
    # return jsonify({
    #     'status': 'success',
    #     'books': BOOKS
    # })

@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        return_book = ''
        for book in BOOKS:
            if book['id'] == book_id:
                return_book = book
        response_object['book'] = return_book
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'publisher': post_data.get('publisher'),
            'instock': post_data.get('instock'),
						'price': post_data.get('price')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)

@app.route('/charge', methods=['POST'])
def create_charge():
	post_data = request.get_json()
	amount = round(float(post_data.get('book')['price']) * 100)
	stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
	charge = stripe.Charge.create(
		amount=amount,
		currency='cad',
		card=post_data.get('token'),
		description=post_data.get('book')['title']
	)
	response_object = {
		'status': 'success',
		'charge': charge
	}
	return jsonify(response_object), 200

@app.route('/charge/<charge_id>')
def get_charge(charge_id):
	stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
	response_object = {
		'status': 'success',
		'charge': stripe.Charge.retrieve(charge_id)
	}
	return jsonify(response_object), 200

BOOKS = [
    {   
        'id': uuid.uuid4().hex,
        'title': 'Seasons',
        'publisher': 'Azmodee',
        'instock': True,
        'price': '5.99'
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Dungeons \'n\' Dragons',
        'publisher': 'Wizards of the Coast?',
        'instock': False,
        'price': '5.99'
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Monoply',
        'publisher': 'John Carpenter',
        'instock': True,
        'price': '5.99'
    }
]


if __name__ == '__main__':
    app.run(host='0.0.0.0')