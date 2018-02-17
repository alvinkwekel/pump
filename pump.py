from flask import Flask, jsonify
from flask.json import JSONEncoder
from workout import Workout
from exercise import Exercise
from execution import Execution
from set import Set

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

@app.route('/exercises')
def exercise():
    return jsonify([build_exercise_sample()])

@app.route('/workouts')
def workouts():
    return jsonify([build_workout_sample()])

def build_workout_sample():
    workout1 = Workout()
    workout1.date = '2018-02-19'
    execution1 = Execution()
    execution1.exercise = build_exercise_sample()
    set1, set2, set3 = Set(), Set(), Set()
    set1.start_time = '2018-02-19T16:10:35Z'
    set1.repetitions = 10
    set1.weight = 40
    set2.start_time = '2018-02-19T16:12:35Z'
    set2.repetitions = 9
    set2.weight = 42
    set3.start_time = '2018-02-19T16:14:35Z'
    set3.repetitions = 8
    set3.weight = 42
    execution1.sets = [set1, set2, set3]
    workout1.executions = [execution1]
    return workout1

def build_exercise_sample():
    exercise1 = Exercise()
    exercise1.name = 'squats-kevein'
    return exercise1
