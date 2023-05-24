from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://okoride0:lindahst1@database1.a17zh8w.mongodb.net/?retryWrites=true&w=majority")

@app.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('query')
    
    # Connect to the MongoDB collection
    db = client['your_database']
    collection = db['products']
    
    # Search the collection for matching products
    matching_products = collection.find({'product_name': {'$regex': query, '$options': 'i'}})
    
    # Prepare the response
    results = []
    for product in matching_products:
        results.append({
            'name': product['product_name'],
            'price': product['product_price'],
            'shipped_from_abroad': product['shipped_from_abroad']
        })
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
