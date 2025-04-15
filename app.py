from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>" # return HTML

@app.route('/describe')
def get_description():
    return """
    <h1>
        Flask API
    </h1>
    <p>
        This app supports the endpoint listed below. You can change the data being sent to the API by updating the URI.
        </p>
        <p>The four request methods we will use are GET, POST, PUT, and DELETE. GET requests can be used in a browser. The other methods can be used via CURL or another API platform, such as Postman or Thunder Client in VS Code.
    <p>
    <ul>
        <li><a href='http://127.0.0.1:5000/describe'>GET This Page</a></li>
        <li><a href='http://127.0.0.1:5000/username/1'>GET a username from ID</a></li>
        <li><a href='http://127.0.0.1:5000/users/'>GET all user info</a></li>
    </ul>
    <p>The endpoints below can be accessed over CURL using the correct request method.</p>
    </ul>
        <li>curl -X POST 'http://127.0.0.1:5000/new_user/Georgina/' # POST a new user</a></li>
        <li>curl -X PUT 'http://127.0.0.1:5000/update_username/1/Hazel/' # PUT updates</li>
        <li>curl -X DELETE 'http://127.0.0.1:5000/delete_user/1/' # DELETE a user by ID</a></li>
    <ul>
    """

app.run(host="0.0.0.0", port=5000)