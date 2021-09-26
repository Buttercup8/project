import os
import flask
from ma import call_apis
app = flask.Flask(__name__)

artists = ['5cj0lLjcoR7YOSnhnX0Po5', '1G9G7WwrXka3Z1r7aIDjI7', '6TLwD7HPWuiOzvXEa3oCNe', '5K4W6rqBFWDnAN6FQUkS6x', '05fG473iIaoy82BF1aGhL8', '4yvcSjfu4PC0CYQyLy4wSq']

@app.route("/")  # Python decorator
def index():
    return flask("index.html", lst=call_apis(artists=artists))


app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 4141)),
    debug=True
)
