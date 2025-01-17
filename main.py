from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_numbers():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        return jsonify({
            'operation': 'addition',
            'num1': num1,
            'num2': num2,
            'result': num1 + num2
        })
    except ValueError:
        return jsonify({'error': 'Invalid input. Please provide numbers.'}), 400

@app.route('/multiply', methods=['GET'])
def multiply_numbers():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        return jsonify({
            'operation': 'multiplication',
            'num1': num1,
            'num2': num2,
            'result': num1 * num2
        })
    except ValueError:
        return jsonify({'error': 'Invalid input. Please provide numbers.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
