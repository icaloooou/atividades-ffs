import math
from flask import Flask, render_template, request
from unittest import TestCase, main

app = Flask(__name__)
app.config.from_object(__name__)

class Calculadora:
    def operation(self, x, y, operation):
        match operation:
            case "+":
                result = x + y 
            case "-":
                result = x - y
            case "*":
                result = x * y
            case "/":
                result = x / y
            case "Raiz Quadrada":
                result = math.sqrt(x)
            case "Logaritmo":
                result = math.log(x,y)
            case "Exponenciação":
                result = math.pow(x,y)
        return result
            
@app.route('/')
def calcu():
    return render_template('calcu.html')

@app.route('/resultado', methods=['POST'])
def show_result():
    valor_1 = float(request.form.get("var_1"))
    valor_2 = float(request.form.get("var_2"))
    operation = request.form.get("operation")
    calc = Calculadora()
    try:
        res = calc.operation(valor_1, valor_2, operation)
    except:
        res = "Error"
    finally:
            return render_template('resultado.html', res=res)

class TestesCalculadora(TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_soma(self):
        self.assertEqual(self.calc.operation(1, 1,"+"), 2)    
    
    def test_sub(self):
        self.assertEqual(self.calc.operation(1, 1,"-"), 0)

    def test_mul(self):
        self.assertEqual(self.calc.operation(2, 2,"*"), 4)
    
    def test_div(self):
        self.assertEqual(self.calc.operation(3, 3,"/"), 1)
  
    def test_div_byZero(self):
        self.assertRaises(ZeroDivisionError,self.calc.operation(3, 0, "/"))
   
    def test_sqr(self):
        self.assertEqual(self.calc.operation(144, 0, "Raiz Quadrada",), 12.0)

    def test_log(self):
        self.assertEqual(self.calc.operation(144, 2, "Logaritmo"), 7.169925001442313)
    
    def test_exp(self):
        self.assertEqual(self.calc.operation(12, 2, "Exponenciação"), 144.0)

if __name__ == '__main__':
    #app.run(debug=True)
    main()
