import os
import random

from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from bll.dataservice import get_data, insert_data, get_data_by_id, delete_data, save, update_data, req1, req2, req3
from dal import db
from dal.db import db_string
from dal.dto import UserSkillDTO
from dal.model import Person, Skill, UserSkill, Country
from forms.skill_form import SkillForm
from forms.user_form import UserForm
from forms.user_has_skill import UserSkillForm
from forms.county_form import CountryForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_string

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods=['GET', 'POST'])
def user():
    result = get_data(Person)
    form = UserForm(request.form)
    if request.method == 'POST':
        print(form.id.data)

        if(form.id.data == ''):
            user = Person(int(random.getrandbits(31)), first_name = form.first_name.data, second_name = form.second_name.data, birthday = form.birthday.data, city = form.city.data)
            insert_data(user)
        else:
            user = Person(id = int(form.id.data), first_name = form.first_name.data, second_name = form.second_name.data, birthday = form.birthday.data, city = form.city.data)
            update_data(user, Person)
        save()
        return redirect('/user')

    return render_template('users.html', users = result, form = form)

@app.route('/user/delete/<id>')
def user_delete(id):
    delete_data(Person, id)
    save()
    return redirect('/user')

@app.route('/user/edit/<id>', methods=['GET'])
def user_edit(id):
    if request.method == 'GET':
        user = get_data_by_id(Person, id)
        result = get_data(Person)
        form = UserForm()
        form.id.data = user.id
        form.first_name.data = user.first_name
        form.second_name.data = user.second_name
        form.birthday.data = user.birthday
        form.city.data = user.city
        return render_template('users.html', users = result, form = form)


@app.route('/skill', methods=['GET', 'POST'])
def skill():
    result = get_data(Skill)
    form = SkillForm(request.form)
    if request.method == 'POST':
        print(form.id.data)
        ''''''
        if(form.id.data == ''):
            skill = Skill(int(random.getrandbits(31)), form.name.data)
            insert_data(skill)
        else:
            skill = Skill(int(form.id.data), form.name.data)
            update_data(skill, Skill)
        save()
        return redirect('/skill')

    return render_template('skill.html', skills = result, form = form)

@app.route('/skill/delete/<id>')
def skill_delete(id):
    delete_data(Skill, id)
    save()
    return redirect('/skill')

@app.route('/skill/edit/<id>', methods=['GET'])
def skill_edit(id):
    if request.method == 'GET':
        skill = get_data_by_id(Skill, id)
        result = get_data(Skill)
        form = SkillForm()
        form.id.data = skill.id
        form.name.data = skill.name
        return render_template('skill.html', skills = result, form = form)

@app.route('/userskill', methods=['GET', 'POST'])
def userskill():
    users = get_data(Person)
    skills = get_data(Skill)
    req = req2(Person, UserSkill, Skill)
    userskills = [UserSkillDTO(i[0], i[1] + ' ' + i[2], i[3]) for i in req]
    form = UserSkillForm(request.form)
    form.skill_id.choices = [(skill.id, skill.name) for skill in skills]
    form.user_id.choices = [(user.id, user.first_name) for user in users]
    if request.method == 'POST':
        print(form.id.data)

        if form.id.data == '':
            userskill = UserSkill(int(random.getrandbits(31)), form.user_id.data, form.skill_id.data)
            insert_data(userskill)
        else:
            userskill = UserSkill(int(form.id.data), form.user_id.data, form.skill_id.data)
            update_data(userskill, UserSkill)
        save()
        return redirect('/userskill')

    return render_template('user_has_skill.html', userskills = userskills, form = form)

@app.route('/userskill/delete/<id>')
def userskill_delete(id):
    delete_data(UserSkill, id)
    save()
    return redirect('/userskill')

@app.route('/userskill/edit/<id>', methods=['GET'])
def userskill_edit(id):
    if request.method == 'GET':
        userskill = get_data_by_id(UserSkill, id)

        users = get_data(Person)
        skills = get_data(Skill)
        req = req2(Person, UserSkill, Skill)
        userskills = [UserSkillDTO(i[0], i[1] + ' ' + i[2], i[3]) for i in req]

        form = UserSkillForm(request.form)
        form.skill_id.choices = [(skill.id, skill.name) for skill in skills]
        form.user_id.choices = [(user.id, user.first_name) for user in users]
        form.id.data = userskill.id
        form.skill_id.data = userskill.skill_id
        form.user_id.data = userskill.user_id
        return render_template('user_has_skill.html', userskills = userskills, form = form)


@app.route('/get')
def sk1():

    country1 = Country(int(random.getrandbits(31)), name='Ukraine', president = 'Zelenskiy',
                  population = 3500000, year_creation=1991)
    country2 = Country(int(random.getrandbits(31)), name='Russia', president='Putin',
                       population=13500000, year_creation=1991)
    country3 = Country(int(random.getrandbits(31)), name='Belodussia', president='Lukashenko',
                       population=3000000, year_creation=1991)

    insert_data(country1)
    insert_data(country2)
    insert_data(country3)
    save()

    return 'added'

@app.route('/show', methods=['GET'])
def show():
    result = get_data(Country)
    return render_template('country.html', countries=result)



@app.route('/dashboard')
def dashboard():
    res1 = req1(Person, UserSkill, Skill)
    res2 = req3(Person, UserSkill, Skill)
    values1 = [i[1] for i in res1]
    labels1 = [i[0] for i in res1]
    values2 = [i[1] for i in res2]
    labels2 = [i[0] for i in res2]

    return render_template('dashboard.html', val1 = values1, lab1 = labels1, val2 = values2, lab2 = labels2)

@app.route('/update/<id>',  methods=['GET', 'POST'])
def update(id):
    print(id)

    country = get_data_by_id(Country, id)
    form = CountryForm()
    if request.method == 'GET':
        form.id.data = id
        form.name.data = country.name
        form.president.data = country.president
        form.year_creation.data = country.year_creation
        form.population.data = country.population

    return render_template('update.html', form = form)


@app.route('/bar',  methods=['GET'])
def bar():
    res2 = get_data(Country)
    values2 = [i.population for i in res2]
    labels2 = [i.name for i in res2]

    return render_template('bar.html', val2 = values2, lab2 = labels2)

if __name__ == '__main__':
    app.run(debug=True)