from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField, TextAreaField
from wtforms.validators import DataRequired, Email

#Default form for creating tickets, available to even anonymous users
class CreateTicketForm(FlaskForm):
    ticket_name = StringField('Name')
    email = StringField('Email', validators=[DataRequired(), Email()])
    urgency = SelectField("Priority", choices=[('low', 'Low'), ('mid','Mid'), ('high', 'High')])
    ticket_type = SelectField('Type', choices=[('task', 'Task'), ('bug', 'Bug'), ('other', 'Other')])
    message = TextAreaField('Message')
    submit = SubmitField('Submit Ticket')

#Logged in users get to edit and comment on the tickets
class EditTicketForm(CreateTicketForm):
    Date = DateTimeField('Time created')
    comment = TextAreaField('Comment')
    status = SelectField('Status', choices=[('open', 'Open'), ('in_progress', 'In Progress'),
                                            ('completed', 'Completed'), ('rejected', 'Rejected')])

#To show all tickets to any logged in user
class ReadTicketForm(FlaskForm):
    first_name = StringField('First Name', render_kw={'readonly': True})
    last_name = StringField('Last Name', render_kw={'readonly': True})
    email = StringField('Email', render_kw={'readonly': True})
    urgency = SelectField("Priority", choices=[('low', 'Low'), ('mid','Mid'),
                                                ('high', 'High')], render_kw={'readonly': True})
    status = SelectField('Status', choices=[('open', 'Open'), ('in_progress', 'In Progress'),
                                            ('completed', 'Completed'), ('rejected', 'Rejected')], render_kw={'readonly': True})
    ticket_type = StringField('Type', render_kw={'readonly': True})
    message = TextAreaField('Massage', render_kw={'readonly': True})