from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
pipe = pickle.load(open('pipe.pkl', 'rb'))

teams = [
    'Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa', 
    'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka'
]

cities = [
    'Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 
    'London', 'Pallekele', 'Barbados', 'Sydney', 'Melbourne', 'Durban', 
    'St Lucia', 'Wellington', 'Lauderhill', 'Hamilton', 'Centurion', 
    'Manchester', 'Abu Dhabi', 'Mumbai', 'Nottingham', 'Southampton', 
    'Mount Maunganui', 'Chittagong', 'Kolkata', 'Lahore', 'Delhi', 
    'Nagpur', 'Chandigarh', 'Adelaide', 'Bangalore', 'St Kitts', 'Cardiff', 
    'Christchurch', 'Trinidad'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    # defaults for GET / to re-populate form after POST
    batting_team = ''
    bowling_team = ''
    city = ''
    current_score = ''
    overs_input = ''
    wickets = ''
    last_five = ''

    if request.method == 'POST':
        batting_team = request.form.get('batting_team', '')
        bowling_team = request.form.get('bowling_team', '')
        city = request.form.get('city', '')
        current_score = request.form.get('current_score', '')
        overs_input = request.form.get('overs', '')
        wickets = request.form.get('wickets', '')
        last_five = request.form.get('last_five', '')

        # safe conversions
        try:
            current_score_int = int(current_score)
        except (ValueError, TypeError):
            current_score_int = 0
        try:
            wickets_int = int(wickets)
        except (ValueError, TypeError):
            wickets_int = 0
        try:
            last_five_int = int(last_five)
        except (ValueError, TypeError):
            last_five_int = 0

        # convert overs like "10.3" -> 10*6 + 3 balls
        balls_bowled = 0
        if overs_input:
            if '.' in overs_input:
                over_part, ball_part = overs_input.split('.')
                try:
                    balls_bowled = int(over_part) * 6 + int(ball_part)
                except (ValueError, TypeError):
                    balls_bowled = 0
            else:
                try:
                    balls_bowled = int(overs_input) * 6
                except (ValueError, TypeError):
                    balls_bowled = 0

        balls_left = max(0, 120 - balls_bowled)
        wicket_left = max(0, 10 - wickets_int)
        current_run_rate = (current_score_int * 6) / balls_bowled if balls_bowled > 0 else 0

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [city],
            'current_score': [current_score_int],
            'balls_left': [balls_left],
            'wicket_left': [wicket_left],
            'current_run_rate': [current_run_rate],
            'last_five': [last_five_int]
        })

        result = pipe.predict(input_df)
        prediction = int(result[0])

    return render_template(
        'index.html',
        teams=sorted(teams),
        cities=sorted(cities),
        prediction=prediction,
        batting_team=batting_team,
        bowling_team=bowling_team,
        city=city,
        current_score=current_score,
        overs=overs_input,
        wickets=wickets,
        last_five=last_five
    )
def new_func(input_df):
    result = pipe.predict(input_df)
    return result

if __name__ == '__main__':
    app.run(debug=True)
