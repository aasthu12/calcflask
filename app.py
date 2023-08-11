from flask import Flask,request,render_template


app=Flask(__name__)


@app.route('/')
def welcome():
    return("Welcome to Flask")

@app.route('/calc',methods=["GET"])
def math_operator():
    operator=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json['number2']

    if operator=='add':
        result=number1+number2
    elif operator=='substract':
        result=number1-number2
    elif operator=='multiply':
        result=number1*number2
    else:
        result=number1/number2
    return result
print(__name__)


if __name__=='__main__':
    app.run(debug=True)
