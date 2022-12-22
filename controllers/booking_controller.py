from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)

@bookings_blueprint.route("/bookings/new")
def new_booking():
    members = member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    return render_template("bookings/new.html", members=members, gym_classes=gym_classes)

@bookings_blueprint.route("/bookings", methods=['POST'])
def create_booking():
    print(request.form)
    member = member_repository.select(request.form["member_id"])
    gym_class = gym_class_repository.select(request.form["gym_class_id"])
    booking = Booking(member, gym_class)
    booking_repository.save(booking)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>/edit", methods=['GET'])
def edit_booking(id):
    print(id)
    booking = booking_repository.select(id)
    members = member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    return render_template('bookings/edit.html', booking=booking, members=members, gym_classes=gym_classes)

@bookings_blueprint.route("/bookings/<id>", methods=['POST'])
def update_booking(id):
    booking_repository.update(id, request.form['member_id'], request.form['gym_class_id'])
    return redirect("/bookings")