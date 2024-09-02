from flask import Blueprint, request, jsonify
from api.classes.length import Length
from api.classes.temperature import Temperature

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