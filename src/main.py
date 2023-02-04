import os

from src.api import app
import jwt

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")



