from flask import Flask, request, render_template

app = Flask(__name__)

def read_sensor_data():
    try:
        with open('sensor_data.txt', 'r') as file:
            lines = file.readlines()
            data = {}
            for line in lines:
                key, value = line.split(':')
                data[key.strip()] = value.strip()
            print(data)  # Print the data to the console
            return data
    except FileNotFoundError:
        print("File not found.")
        return {}

@app.route('/')
def index():
    data = read_sensor_data()
    return render_template('index.html', data=data)

@app.route('/update')
def update():
    data = read_sensor_data()
    return render_template('update.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
