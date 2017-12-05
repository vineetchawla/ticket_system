from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
from wtforms_components import DateTimeField, read_only, DateRange
from wtforms.fields.html5 import DateField
from datetime import datetime

from ..models import User

class FlightForm(FlaskForm):
    """
    Forms for users to select the flights
    """
    flight_id = StringField('FlightID', validators=[DataRequired()])
    departure_airport = StringField('Departure Airport', render_kw={'readonly': True})
    departure_city = StringField('Departure City', render_kw={'readonly': True})
    arrival_airport = StringField('Arrival Airport', render_kw={'readonly': True})
    arrival_city = StringField('Arrival City', render_kw={'readonly': True})
    airline = StringField('Airline', render_kw={'readonly': True})
    arrival_time = StringField('Arrival time', render_kw={'readonly': True})
    departure_time = DateTimeField('Departure Time', render_kw={'readonly': True})
    date = DateField('Flight Date', validators=[DataRequired(), DateRange(min=datetime(2017,9,1))])
    aircraft = HiddenField('Aircraft')
    flight_duration = HiddenField('Duration')
    airport_code = HiddenField('Airport_code')

    submit = SubmitField('Calculate Insurance rates')

class InsuranceForm(FlaskForm):
    """
    Form for user to select insurance
    """
    get_insurance = SubmitField('Select Insurance')
    

