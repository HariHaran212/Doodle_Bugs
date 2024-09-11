from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # Create a bar chart using Matplotlib
    fig, ax = plt.subplots()
    x = ['A', 'B', 'C', 'D']
    y = [10, 20, 15, 25]
    ax.bar(x, y)

    # Save the plot to a PNG image in memory
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()

    return render_template('Graph.html', graph=graph_url)

if __name__ == '__main__':
    app.run(debug=True)
