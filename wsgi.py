"""Driver for Web server"""

from view import app

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port='8080')