from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route("/compute")
def home():
    if request.method == 'POST':
        #Check for format
        if not request.is_json:
            return Response(
                    json.dumps("{ 'error': 'bad input format' }"),
                    status=400,
                    mimetype='application/json')

        content = request.get_json()
        moments = []
        Zs = []
        matrix = []
        Xs = []

        L = float(content['L'])
        q = float(content['q'])
        EI = float(content['EI'])
        n = float(content['n'])
        h = L/n #interval

        Xs = [float(input("Enter X" + str(i) + ":")) for i in range(0,int(n)-1)]
        moments = [(0.5*q*L*X) - (0.5*q*(X**2)) for X in Xs]
        Zs = [(-h**2 * moments[i]) / EI for i in range(0,int(n)-1)]
        A = np.array([[-2,1,0],[1,-2,1],[0,1,-2]])
        b = np.array(Zs)
        z = np.linalg.solve(A,b)
        
        return Response(
                    json.dumps("{ 'result':"+z+" }"),
                    status=200,
                    mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True)
