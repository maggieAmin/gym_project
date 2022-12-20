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
    gym_class = member_repository.select(request.form["gym_class_id"])
    booking = Booking(member, gym_class)
    booking_repository.save(booking)
    return redirect("/bookings")