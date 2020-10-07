import os
from flask import render_template,  request, redirect, url_for
from app import app
from app.forms import LeadForm, NewsletterForm
from app.odoo import server
from config import Config 
import hashlib 

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LeadForm()
    if form.validate_on_submit():
        crm = server()
        email = form.email.data
        domain = [['|', ('email','=', email), ('email','=', email)]]
        crm.cnn() 
        partner  = crm.get('res.partner',domain, {'fields': ['id']}) 
        if len(partner) > 0:
            partner_id = partner[0]['id']
        else:
            res = {'name':form.name.data, 'email':email}
            partner_id = crm.create('res.partner',res)
        res = {'name': Config.CRM['lead'], 'description':form.message.data, 'partner_id': partner_id}
        crm.create('crm.lead',res)
        return redirect('/gracias/ld')
    form2 = NewsletterForm()
    if form2.validate_on_submit():
        crm = server()
        email = form2.email.data
        domain = [[('name', '=', Config.CRM['newsletter'])]]
        crm.cnn()
        newsletter = crm.get('mailing.list',domain, {'fields': ['id']}) 
        if len(newsletter) > 0:
            list_id = newsletter[0]['id']
            domain = [[('email','=',form2.email.data)]]
            contact = crm.get('mailing.contact',domain, {'fields': ['id', 'list_ids']}) 
            if len(contact)>0:
                if list_id in contact[0]['list_ids']:
                    return redirect('/gracias/ok')
                else:
                    res = {'contact_id':contact[0]['id'], 'list_id':list_id}
                    crm.create('mailing.contact.subscription',res)
                    return redirect('/gracias/add')
            else:
                res = {'email':form2.email.data}
                contact_id = crm.create('mailing.contact',res)
                res = {'contact_id':contact_id, 'list_id':list_id}
                crm.create('mailing.contact.subscription',res)
                return redirect('/gracias/new')
    tracking = {'ga':Config.OPTIONS['google'], 'fb':Config.OPTIONS['facebook'], 'at':Config.OPTIONS['addthis']}
    return render_template('index.html', form=form, form2=form2, tracking=tracking)

@app.route('/gracias')
@app.route('/gracias/<source>')
def gracias(source='ups'):
    source = source
    print(source)
    return render_template('gracias.html', source=source)



    