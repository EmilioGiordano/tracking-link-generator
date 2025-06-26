from flask import Flask, render_template, request
import re
from agencies import AGENCIES

app = Flask(__name__)

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
    enlace = None
    error = None
    texto = ''
    if request.method == 'POST':
        texto = request.form.get('mensaje', '')
        agencia = detectar_agencia(texto)
        numero = detectar_numero_seguimiento(texto)
        if agencia and numero:
            url_base = AGENCIES[agencia]['url']
            enlace = url_base.format(numero) if '{}' in url_base else f"{url_base}{numero}"
        else:
            error = 'No se pudo detectar el número de seguimiento o la agencia.'
    return render_template('index.html', enlace=enlace, error=error, texto=texto)

 