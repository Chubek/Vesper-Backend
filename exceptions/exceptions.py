from flask import jsonify


def res_not_found():
    return jsonify({"message": "Resource not found"}), 404


def res_unauthorized():
    return jsonify({"message": "Access unauthorized"}), 401


def res_forbidden():
    return jsonify({"message": "Access denied"}), 403


def res_server_error():
    return jsonify({"message": "Server error"}), 500

