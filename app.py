"""Pets application"""

from flask import Flask, request, redirect, render_template, flash, url_for
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "555667111key"

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

# ROUTES
@app.route('/')
def pets_list():
    """List all the pets in the agency db"""
    pets = Pet.query.all()
    return render_template('/pet-list.html', pets=pets)

# error handling route
@app.errorhandler(404)
def page_404(e):
    """Display 404 page for route not found"""
    return render_template('/404.html'), 404

@app.route('/pets/<int:pet_id>')
def pet_details(pet_id):
    """Display specific pet info page"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('/pet-details.html', pet=pet)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Form to add a pet and post submission route"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name,species=species,photo_url=photo_url or None,age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()
        flash("New pet added.")
        return redirect(url_for('pets_list'))
    else:
        """GET route so show form"""
        return render_template('add-pet.html', form=form)

@app.route("/pets/<int:pet_id>/edit", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit a pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.commit()
        flash('Pet edited!')
        return redirect(url_for('pets_list'))
    else:
        return render_template('/edit-pet.html', form=form, pet=pet)



