# app/home/views.py

from ..models import User

from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

from . import home
from forms import CreateTicketForm, EditTicketForm, ReadTicketForm
from ..models import Ticket
from .. import db

@home.route('/', methods=['GET', 'POST'])
def homepage():
    """
    Render the homepage template on the / route
    """
    form = CreateTicketForm()
    if form.validate_on_submit():
        ticket = Ticket(ticket_name = form.ticket_name.data,
                        status = "open", #every tickets defaults to open on creation. logged in users can change it
                        urgency = form.urgency.data,
                        type = form.ticket_type.data,
                        message = form.message.data,
                        ticket_email =form.email.data
                        )

        db.session.add(ticket)
        db.session.commit()
        flash('Your Ticket has been added. Log in to make further changes')
        return redirect(url_for('home.homepage'))

    return render_template('home/index.html', form= form, title='Create Ticket')


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    ticket_list = Ticket.query.all()

    return render_template('home/dashboard.html', title="List of tickets", ticket_list = ticket_list)

@home.route('/tickets/delete/<int:id>', methods = ['GET','POST'])
@login_required
def delete_ticket(id):
    """
    Delete a ticket from the database
    :param id:
    :return:
    """
    ticket = Ticket.query.get_or_404(id)
    db.session.delete(ticket)
    db.session.commit()

    flash('You have successfully deleted the department.')

    # redirect to the dashboard
    return redirect(url_for('home.dashboard'))

@home.route('/tickets/edit/<int:id>', methods = ['GET','POST'])
@login_required
def edit_ticket(id):
    """
    Edit a ticket
    :return:
    """
    ticket = Ticket.query.get_or_404(id)
    form = EditTicketForm(obj=ticket)
    if form.validate_on_submit():

        ticket.ticket_name = form.ticket_name
        ticket.ticket_email = form.email

        db.session.commit()
        flash('The changes to ticket have been saved')

        # redirect to the dashboard
        return redirect(url_for('home.dashboard'))

    form.email.data = ticket.ticket_email
    form.ticket_name = ticket.ticket_name

    return render_template('home/edit_ticket.html', form= form)
