from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import Gym_class
import repositories.gym_class_repository as gym_class_repository
import repositories.booking_repository as booking_repository

gym_classes_blueprint = Blueprint('gym_classes', __name__)

@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/index.html", gym_classes=gym_classes)

@gym_classes_blueprint.route("/gym_classes/new")
def new_class():
    return render_template("gym_classes/new.html")

@gym_classes_blueprint.route("/gym_classes", methods=['POST'])
def create_gym_class():
    title = request.form['title']
    capacity = int(request.form['capacity'])
    gym_class = Gym_class(title, capacity)
    gym_class_repository.save(gym_class)
    return redirect("/gym_classes")

@gym_classes_blueprint.route("/gym_classes/<id>", methods=['GET'])
def show_gym_class(id):
    gym_class = gym_class_repository.select(id)
    bookings = booking_repository.select_members_for_class(id)
    return render_template("/gym_classes/show.html", gym_class=gym_class, bookings=bookings )

@gym_classes_blueprint.route("/gym_classes/<id>/edit", methods=['GET'])
def edit_gym_class(id):
    gym_class = gym_class_repository.select(id)
    return render_template("gym_classes/edit.html", gym_class=gym_class)

@gym_classes_blueprint.route("/gym_classes/<id>", methods=['POST'])
def update_gym_class(id):
    title = request.form['title']
    capacity = int(request.form['capacity'])
    gym_class = Gym_class(title, capacity, id)
    gym_class_repository.update(gym_class)
    return redirect('/gym_classes')



