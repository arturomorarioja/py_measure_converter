from flask import Blueprint, request, jsonify
from api.classes.length import Length

def error_message():
    return jsonify(error='Invalid parameters')

bp = Blueprint('converter', __name__)

@bp.route('/length', methods=['GET'])
def get_length():
    measure = request.args.get('measure')
    system = request.args.get('system')

    if not measure.isnumeric():
        return error_message(), 400
    
    try:
        length = Length(measure, system)
        return jsonify(result=str(length.convert())), 200
    except Exception:
        return error_message(), 400
    
