from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import db, PersonalAccount, User

personal_account_bp = Blueprint('personal_account_bp', __name__)

@personal_account_bp.route('/personal_account', methods=['GET', 'POST'])
@login_required
def create_personal_account():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        transaction_with = request.form.get('transaction_with') or None
        source = request.form.get('source') or None  # Get source from form
        debited_amount = request.form.get('debited_amount') or None
        credited_amount = request.form.get('credited_amount') or None
        total_balance = request.form.get('total_balance')

        new_entry = PersonalAccount(
            user_id=user_id,
            transaction_with=transaction_with,
            source=source,  # Save source
            debited_amount=debited_amount,
            credited_amount=credited_amount,
            total_balance=total_balance
        )

        db.session.add(new_entry)
        db.session.commit()

        return redirect(url_for('personal_account_bp.create_personal_account'))

    users = User.query.filter(User.id != current_user.id).all()

    return render_template('personal_account.html', users=users)

