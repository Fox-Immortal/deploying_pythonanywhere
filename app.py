from flask import Flask, request
import git
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/update_server', methods=['POST', 'GET'])
def update():
	if request.method == 'POST':
		
	return 'hey there'



if __name__ == '__main__':
    app.run()

