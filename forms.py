from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    FloatField,
    SubmitField
)
from wtforms.validators import (
    DataRequired
)

class Prediction(FlaskForm):
    area = FloatField("Area (in sq feet)", validators= [DataRequired()])
    rooms = IntegerField("Number of Rooms", validators=[DataRequired()])
    submit = SubmitField('Predict the Price')
