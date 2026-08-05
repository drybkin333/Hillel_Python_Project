from flask import Flask, render_template

app = Flask(__name__)

schedule = [

    {"day": "Понеділок", "workout": "Груди + трицепс"},

    {"day": "Вівторок", "workout": "Біг 5 км"},

    {"day": "Середа", "workout": "Спина + біцепс"},

    {"day": "Четвер", "workout": "CrossFit"},

    {"day": "П'ятниця", "workout": "Ноги"},

    {"day": "Субота", "workout": "Турнік + прес"},

    {"day": "Неділя", "workout": "Відпочинок"}
]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/schedule')
def workout_schedule():
    return render_template("schedule.html", schedule=schedule)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)