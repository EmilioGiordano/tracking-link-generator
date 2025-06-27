from flask import Flask, render_template, request, redirect, url_for, session
import re
from agencies import AGENCIES

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Necesario para usar session

def detectar_agencia(texto):
    texto_lower = texto.lower()
    for agencia, data in AGENCIES.items():
        for alias in data['aliases']:
            if alias in texto_lower:
                return agencia
    return None

def detectar_numero_seguimiento(texto):
    match = re.search(r'\b(\d{6,})\b', texto)
    if match:
        return match.group(1)
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        texto = request.form.get('mensaje', '')
        numero_pedido = request.form.get('numero-pedido', '')
        
        # Guardar datos en session
        session['texto'] = texto
        # Solo actualizar numero_pedido si se proporciona uno nuevo
        if numero_pedido:
            session['numero_pedido'] = numero_pedido
        
        agencia = detectar_agencia(texto)
        numero = detectar_numero_seguimiento(texto)
        
        if agencia and numero:
            url_base = AGENCIES[agencia]['url']
            enlace = url_base.format(numero) if '{}' in url_base else f"{url_base}{numero}"
            session['enlace'] = enlace
            session['error'] = None
        else:
            session['error'] = 'No se pudo detectar el número de seguimiento o la agencia.'
            session['enlace'] = None
        
        # Redirigir a GET para evitar reenvío de formulario
        return redirect(url_for('index'))
    
    # GET request - obtener datos de session
    texto = session.get('texto', '')
    numero_pedido = session.get('numero_pedido', '')
    enlace = session.get('enlace')
    error = session.get('error')
    
    return render_template('index.html', enlace=enlace, error=error, texto=texto, numero_pedido=numero_pedido)

@app.route('/actualizar-pedido', methods=['POST'])
def actualizar_pedido():
    numero_pedido = request.form.get('numero-pedido', '')
    session['numero_pedido'] = numero_pedido
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 