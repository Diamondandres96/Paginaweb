# Importa la clase Flask y la función render_template desde el módulo flask
from flask import Flask, render_template

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta '/' que representa la página de inicio
@app.route('/')
def home():
    '''
    Esta es una docstring.
    Se utiliza para documentar lo que hace la función.
    Puedes escribir varias líneas de texto aquí.
    '''
    pass  # No hay ninguna operación definida aquí, solo se pasa al siguiente paso

    # Renderiza el template 'home.html' y devuelve el resultado
    return render_template('home.html')

# Define una ruta '/about' que representa la página 'Acerca de'
@app.route('/about')
def about():
    # Renderiza el template 'about.html' y devuelve el resultado
    return render_template('about.html')

# Define una ruta '/clothing' que representa la página 'ropa'
@app.route('/clothing')
def clothing():
    # Renderiza el template 'clothing.html' y devuelve el resultado
    return render_template('clothing.html')

# Define una ruta '/contactus' que representa la página 'contactanos'
@app.route('/contactus')
def contactus():
    # Renderiza el template 'clothing.html' y devuelve el resultado
    return render_template('contactus.html')

# Comprueba si este script es el script principal que se está ejecutando
if __name__ == '__main__':
    # Inicia la aplicación Flask en modo de depuración (debug=True)
    app.run(debug=True)