# app/home/views.py

from ..models import User

from flask import render_template, flash
from flask_login import login_required, current_user

from . import home
from forms import CreateTicketForm, EditTicketForm, ReadTicketForm
from ..models import Ticket
from .. import db

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    form = CreateTicketForm()
    if form.validate_on_submit():
        ticket = Ticket(first_name = form.first_name.data,
                        last_name = form.last_name.data,
                        status = "open", #every tickets defaults to open on creation. logged in users can change it
                        priority = form.priority.data,
                        ticket_type = form.ticket_type.data,
                        message = form.message.data
                        )

    try:
        db.session.add(ticket)
        db.session.commit()
        flash('Your Ticket has been added. Log in to make further changes')
    except:
        db.session.rollback()
        raise

    return render_template('home/index.html', title='Create Ticket')


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Logged in User")

