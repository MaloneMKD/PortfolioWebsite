from flask import render_template, redirect, url_for, flash, send_file
from port_web.forms import ContactForm
from port_web import app, db
from port_web.models import Messages
from projects_data import *


@app.route('/')
@app.route('/home')
def home_page():
    return render_template("main_page.html", page="home")


@app.route('/about', methods=["GET", "POST"])
def about_page():
    form = ContactForm()
    if form.validate_on_submit():
        message = Messages(name=form.name.data,
                           email=form.email.data,
                           message=form.message.data)
        db.session.add(message)
        db.session.commit()
        flash(f'Message submitted successfully!', 'success')
        return redirect(url_for('about_page'))

    return render_template("about_page.html", page="about", form=form)


@app.route('/project/<string:project_title>')
def project_page(project_title):
    project_data = None
    if project_title == "journal_by_topic":
        project_data = journal_by_topic
    elif project_title == "tms":
        project_data = tms
    elif project_title == "steak_nation":
        project_data = steak_nation
    elif project_title == "wordsmith":
        project_data = wordsmith
    elif project_title == "eca":
        project_data = eca
    return render_template('project.html', page="project", project_data=project_data)


@app.route('/project_page/download/<string:setup_name>')
def download(setup_name):
    if setup_name == 'Journal By Topic':
        return send_file("static/downloads/JBT-Setup.exe", as_attachment=True)
    elif setup_name == 'Turing Machine Simulator':
        return send_file("static/downloads/TMSInstaller.exe", as_attachment=True)
    elif setup_name == 'Wordsmith':
        return send_file("static/downloads/wordsmith.apk", as_attachment=True)
    elif setup_name == 'Elementary Cellular Automata':
        return send_file("static/downloads/Elementary Cellular Automata.zip", as_attachment=True)
