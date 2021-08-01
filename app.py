from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/ideaskenya'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kxpdtdmmxauczq:16a4a4960e7763316d5f21f9e84aade9a89fee20665d7dda831ee17a90d893e4@ec2-34-230-115-172.compute-1.amazonaws.com:5432/d5pvlmg830f246'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Startups(db.Model):
    __tablename__ = 'startup'
    id = db.Column(db.Integer, primary_key=True)
    startup_name = db.Column(db.String(200))
    web_address = db.Column(db.String(200))
    pitch = db.Column(db.String(200))
    stage = db.Column(db.String(200))
    founding_month = db.Column(db.String(200))
    founding_year = db.Column(db.String(200))
    incorporated = db.Column(db.String(200))
    county = db.Column(db.String(200))
    user_title = db.Column(db.String(200))
    user_role = db.Column(db.String(200))
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    user_bio = db.Column(db.Text)
    phone_number = db.Column(db.String(200))
    linkedin_address = db.Column(db.String(200))
    elevator_pitch = db.Column(db.Text)
    reason_for_attendance = db.Column(db.Text)

    def __init__(self, startup_name, web_address, pitch, stage, founding_month, founding_year, incorporated, county, user_title, user_role, first_name, last_name, email, user_bio, phone_number, linkedin_address, elevator_pitch, reason_for_attendance):
        self.startup_name = startup_name
        self.web_address = web_address
        self.pitch = pitch
        self.stage = stage
        self.founding_month = founding_month
        self.founding_year = founding_year
        self.incorporated = incorporated
        self.county = county
        self.user_title = user_title
        self.user_role = user_role
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_bio = user_bio
        self.phone_number = phone_number
        self.linkedin_address = linkedin_address
        self.elevator_pitch = elevator_pitch
        self.reason_for_attendance = reason_for_attendance


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new')
def new():
    return render_template('startup.html')


@app.route('/startup', methods=['POST'])
def startup():
    if request.method == 'POST':
        startup_name = request.form['startup_name']
        web_address = request.form['web_address']
        pitch = request.form['pitch']
        stage = request.form.getlist('stage')
        founding_month = request.form.getlist('founding_month')
        founding_year = request.form.getlist('founding_year')
        incorporated = request.form.getlist('incorporated')
        county = request.form.getlist('county')
        user_title = request.form['user_title']
        user_role = request.form.getlist('user_role')
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        user_bio = request.form['user_bio']
        phone_number = request.form['phone_number']
        linkedin_address = request.form['linkedin_address']
        elevator_pitch = request.form['elevator_pitch']
        reason_for_attendance = request.form['reason_for_attendance']

        if db.session.query(Startups).filter(Startups.email == email).count() == 0:
            data = Startups(startup_name, web_address, pitch, stage, founding_month, founding_year, incorporated, county, user_title, user_role, first_name, last_name, email, user_bio, phone_number, linkedin_address, elevator_pitch, reason_for_attendance)
            
            db.session.add(data)
            db.session.commit()
            return render_template('startup.html', message='Startup Submitted successfully', success=f'Thank you {first_name} {last_name}, we will get back to you in 24hrs.')

        return render_template('startup.html', err='You have already submitted a startup for review')

if __name__ == '__main__':
    app.run()