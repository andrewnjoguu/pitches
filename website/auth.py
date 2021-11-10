from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get("password1")
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Email must be greater than 4 charcters.',category='error made')
        elif len(firstName) < 2:
             flash('Name must be greater than 2 charcters.', category='error made')
        elif password1 != password2:
            flash('Your passwords do not match.', category='error made')
        elif len(password1) < 7:
            flash('Your password is too short. It must have at least seven characters', category='error made')
        else:
            flash('Account created!', category='success')
            
            

    return render_template("sign_up.html")
