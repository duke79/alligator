# from flask import request
# from app import app
# from app.data import db
#
#
# @app.route('/api/auth')
# def auth():
#     return "Seriously! What are you looking for? ;)"
#
#
# @app.route('/api/auth/get_user_uid_by_session_id', methods=["POST"])
# def get_user_uid_by_session_id():
#     try:
#         session_id = request.form["session_id"]
#         uid = db.get_user_uid_from_session(session_id)
#         return uid
#     except Exception as e:
#         return str(e), 400  # 400 = Bad Request
