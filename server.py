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




# @app.route("/single_map/<location_id>")
# def show_single_map(location_id):
    # """View map of single pin"""

    # renders google map and info box
    # based on click of pin from searched map page
    #location = crud.get_location_by_id(location_id)

#   return render_template('/single_map.html', location=location)





if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)