from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Email

#Default form for creating tickets, available to even anonymous users
class CreateTicketForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email', validators=[DataRequired(), Email()])
    priority = StringField("Priority")
    ticket_type = StringField('Type')
    message = StringField('Massage')
    submit = SubmitField('Submit Ticket')

#Logged in users get to edit and comment on the tickets
class EditTicketForm(CreateTicketForm):
    Date = DateTimeField('Time created')
    comment = StringField('Comment')
    status = SelectField('Status', choices=[('open', 'Open'), ('in_progress', 'In Progress'),
                                            ('completed', 'Completed'), ('rejected', 'Rejected')])

#To show all tickets to any logged in user
class ReadTicketForm(FlaskForm):
    first_name = StringField('First Name', render_kw={'readonly': True})
    last_name = StringField('Last Name', render_kw={'readonly': True})
    email = StringField('Email', render_kw={'readonly': True})
    priority = StringField("Priority", render_kw={'readonly': True})
    ticket_type = StringField('Type', render_kw={'readonly': True})
    message = StringField('Massage', render_kw={'readonly': True})