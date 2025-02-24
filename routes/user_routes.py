from flask import Blueprint, request, render_template, redirect
from models import db, User  # Import from models.py

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user')
def user_list():
    users = User.query.all()
    return render_template('users.html', users=users)

@user_bp.route('/create-user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        is_family_member = request.form.get('is_family_member') == 'on'
        relation = request.form.get('relation') if is_family_member else None
        is_financer = request.form.get('is_financer') == 'on'

        new_user = User(
            full_name=full_name,
            user_name=user_name,
            is_family_member=is_family_member,
            relation=relation,
            is_financer=is_financer
        )
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return redirect('/user')

    return render_template("create_user.html")
