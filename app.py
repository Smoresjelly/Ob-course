from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/start_course')
def start_course():
    # Add your obstacle course logic here
    # For demonstration purposes, just return a message
    return jsonify({'message': 'Obstacle course started!'})

if __name__ == '__main__':
    app.run(debug=True)
