from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, from the Isolated Venv App GG!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4949) # change the port here