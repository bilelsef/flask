from api import app
import os


print("hi")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=os.getenv("PORT"))



