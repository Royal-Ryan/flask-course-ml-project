from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField,SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    N= IntegerField(
        label="Nitrogen",
        validators=[DataRequired()])
    
    P=IntegerField(
        label="Phosphorus",
        validators=[DataRequired()])
    
    K=IntegerField(
        label="Potassium",
        validators=[DataRequired()])
    
    temperature=IntegerField(
        label="Temperature",
        validators=[DataRequired()])
    
    humidity=IntegerField(
        label="Humidity",
        validators=[DataRequired()])
    
    ph=IntegerField(
        label="pH",
        validators=[DataRequired()])
    
    rainfall=IntegerField(
        label="Rainfall",
        validators=[DataRequired()])
    
    submit=SubmitField("Recommend")