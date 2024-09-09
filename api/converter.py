"""
Measure conversion API
It converts:
- Length units between the metric (cm) and imperial (inches) systems
- Temperature units between Celsius, Fahrenheit and Kelvin
- Currency between all currencies in the world
- Academic grades between the Danish and American systems
"""
__author__ = "Arturo Mora-Rioja"
__date__ = "September 2024"

from flask import Blueprint, request, jsonify
from api.classes.length import Length
from api.classes.temperature import Temperature
from api.classes.grading import Grading
from api.classes.currency import Currency

def error_message():
    return jsonify(error='Invalid parameters')

bp = Blueprint('converter', __name__)

@bp.route('/length', methods=['GET'])
def get_length():
    measure = request.args.get('measure')
    system = request.args.get('system')
    
    try:
        measure = float(measure)
        length = Length(measure, system)
        return jsonify(result=str(length.convert())), 200
    except Exception:
        return error_message(), 400
    
@bp.route('/temperature', methods=['GET'])
def get_temperature():
    measure = request.args.get('measure')
    origin_system = request.args.get('origin-scale')
    destination_system = request.args.get('destination-scale')

    try:
        measure = float(measure)
        temperature = Temperature(measure, origin_system)
        return jsonify(result=str(temperature.convert(destination_system))), 200
    except Exception:
        return error_message(), 400
    
@bp.route('/grading', methods=['GET'])
def get_grade():
    measure = request.args.get('measure')
    country = request.args.get('country')

    try:
        grading = Grading()
        return jsonify(result=grading.convert(measure, country)), 200
    except Exception:
        return error_message(), 400
    
@bp.route('/currency', methods=['GET'])
def get_currency():
    amount = request.args.get('measure')
    origin_currency = request.args.get('base-currency')
    destination_currency = request.args.get('destination-currency')

    try:
        currency = Currency()
        if amount == None:
            return currency.get_all(), 200
        else:
            return jsonify(result=currency.convert(amount, origin_currency, destination_currency)), 200
    except Exception:
        return jsonify(error='It was not possible to connect with the Currency API'), 400