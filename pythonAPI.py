from flask import Flask, request, jsonify

app = Flask(__name__)

items = []

@app.route('/items', methods=['GET', 'POST'])
def handle_items():
    if request.method == 'GET':
        return jsonify({'items': items})
    if request.method == 'POST':
        data = request.get_json()
        items.append(data['item'])
        return jsonify({'items': items})

@app.route('/items/<int:index>', methods=['GET', 'PUT', 'DELETE'])
def handle_item(index):
    if request.method == 'GET':
        return jsonify({'item': items[index]})
    if request.method == 'PUT':
        data = request.get_json()
        items[index] = data['item']
        return jsonify({'item': items[index]})
    if request.method == 'DELETE':
        items.pop(index)
        return jsonify({'items': items})

if __name__ == '__main__':
    app.run()
