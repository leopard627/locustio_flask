import logging
from flask import Flask
app = Flask(__name__)

LOGGER = logging.getLogger('gunicorn.error')
# LOGGER.info('my info')
# LOGGER.debug('debug message')

@app.route("/")
def hello():
    return "Hello World!"

# if __name__ == "__main__":
    # app.run()
