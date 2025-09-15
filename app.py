# This is a simple Flask application that serves a "Hello World!" message.
# To run this file, you'll need to have Flask installed.
# You can install it by running: pip install Flask

from flask import Flask

# Create an instance of the Flask application.
app = Flask(__name__)

# Define a route for the root URL ('/').
@app.route('/')
def hello_world():
    """
    This function is called when a user navigates to the root URL.
    It returns a simple "Hello World!" string.
    """
    return 'Hello World!\n'

# This block ensures the application only runs when the script is executed directly.
if __name__ == '__main__':
    # The 'debug=True' option reloads the server automatically when you make code changes.
    app.run(host='0.0.0.0', port=5000)

