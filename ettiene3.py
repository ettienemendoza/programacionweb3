from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ettiene1', methods=['GET', 'POST'])
def notas():
    if request.method == 'POST':

        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        n3 = float(request.form['n3'])
        asis = float(request.form['asis'])
        promedio = (n1+n2+n3)/3
        resultado = 'resultado'
        if asis >= 75 and promedio >= 40.0:
            resultado = 'Alumno aprobado'
        else:
            resultado = 'Alumno reprobado'
        return render_template('ettiene1.html', n1=n1, n2=n2,n3=n3,resultado=resultado,asis=asis, promedio=promedio)
    return render_template('ettiene1.html')


@app.route('/ettiene2', methods=['GET', 'POST'])
def caracteres():
        if request.method == 'POST':
            n1 = str(request.form['n1'])
            n2 = str(request.form['n2'])
            n3 = str(request.form['n3'])
            caracter1 = len(n1)
            caracter2 = len(n2)
            caracter3 = len(n3)
            contar = 0
            lista_caracteres = [caracter1, caracter2, caracter3]
            variable = max(lista_caracteres)
            if variable == caracter1:
                caract = n1
            elif variable == caracter2:
                caract = n2
            elif variable == caracter3:
                caract = n3
            return render_template('ettiene2.html', n1=n1, n2=n2, n3=n3, caracter1=caracter1,
                                   caracter2=caracter2, caracter3=caracter3, variable=variable, caract=caract)
        return render_template('ettiene2.html')

if __name__ == '__main__':
    app.run(debug=True)





