from flask import render_template, url_for, flash, redirect, request, Blueprint

customers = Blueprint('customers', __name__)

@customers.route('/customers')
def find(): 
    return '<h1>customers</h1>'