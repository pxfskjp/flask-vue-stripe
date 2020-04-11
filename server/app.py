import os
import uuid

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

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
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
    app.run()