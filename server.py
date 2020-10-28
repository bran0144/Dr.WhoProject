"""Server for doctor who locations app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

# @app.route('/map_search')
# def create_map_from_search():
#     """Renders template from search criteria"""

# probably a request.form.get using a GET method

#     return render_template('map_search.html')




# @app.route(need to know how to route this to single map)
# def show_single_map(click from map?):
    # """View map of single pin"""

    # renders google map and info box
    # based on click of pin from searched map page

#   return render_template('/single_map.html')





if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)