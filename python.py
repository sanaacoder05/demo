from flask import Flask, render_template, request
import numpy as np
import pandas as pd

app = Flask(_name_)

# Initialize student stats using numpy
def initialize_stats():
    stats = {
        'GPA': np.random.uniform(2.0, 4.0),
        'Energy': np.random.randint(50, 100),
        'Social Life': np.random.randint(1, 10)
    }
    return pd.DataFrame(stats, index=['You'])

stats_df = initialize_stats()

def update_stats(choice, stats_df):
    if choice == '1':
        stats_df.loc['You', 'GPA'] += 0.1
        stats_df.loc['You', 'Energy'] -= 10
    elif choice == '2':
        stats_df.loc['You', 'Energy'] += 10
        stats_df.loc['You', 'GPA'] -= 0.1
    return stats_df

@app.route('/')
def index():
    global stats_df
    stats_df = initialize_stats()
    return render_template('index.html', stats=stats_df.to_html())

@app.route('/choice', methods=['POST'])
def choice():
    global stats_df
    choice = request.form['choice']
    stats_df = update_stats(choice, stats_df)
    return render_template('index.html', stats=stats_df.to_html())

if _name_ == '_main_':
    app.run(debug=True)
