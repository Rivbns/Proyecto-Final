# Import
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')

# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button1 = request.form.get('button1')
    button2 = request.form.get('button2')
    button3 = request.form.get('button3')
    
    if button1:
        return redirect('https://github.com/Rivbns/bot-matematico')
    elif button2:
        return redirect('https://discord.gg/Hxrmd4Aa')
    elif button3:
        return redirect('https://discord.com/oauth2/authorize?client_id=1317614643375505509')
    else:
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
