from flask import Flask,request,json,jsonify
app=Flask(__name__)


@app.route('/')
def welcome():
    return("Welcome to Flask")

@app.route('/calc',methods=["GET"])
def math_operator():
    operator=request.json["operator"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    if operator=='add':
        result=int(number1)+int(number2)
    elif operator=='substract':
        result=int(number1)-int(number2)
    elif operator=='multiply':
        result=int(number1)*int(number2)
    else:
        result=int(number1)/int(number2)
    return jsonify(result)
print(__name__)


if __name__=='__main__':
    app.run(debug=True)
