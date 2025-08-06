from flask import Flask, render_template, redirect, url_for, flash
import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# In-memory list to store timestamps
timestamps = []

@app.route('/')
def home():
    """
    Renders the home page.
    """
    return render_template('home.html')

@app.route('/add_time')
def add_time():
    """
    Adds the current timestamp to the list.
    """
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timestamps.append(current_time)
    flash(f'Successfully added the time: {current_time}')
    return redirect(url_for('home'))

@app.route('/remove_last_time')
def remove_last_time():
    """
    Removes the most recently added timestamp.
    """
    if timestamps:
        removed_time = timestamps.pop()
        flash(f'Successfully removed the last time: {removed_time}')
    else:
        flash('No times to remove.')
    return redirect(url_for('home'))

@app.route('/all_times')
def all_times():
    """
    Displays all the recorded timestamps.
    """
    return render_template('all_times.html', times=timestamps)

if __name__ == '__main__':
    app.run(debug=True, port=5173)