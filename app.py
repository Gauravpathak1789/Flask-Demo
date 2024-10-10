from flask import Flask,redirect,url_for
#  what we had learnt -- building url dynamically and rendering templates.
app=Flask(__name__) #this is app variable


@app.route('/')
def Welcome():
    return "welcome to my website"

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the marks is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is "+str(score)

@app.route('/result/<int:marks>')
def  result(marks):
    result=""
    if marks>70:
        result="success"
    else:
        result= "fail"
    return redirect(url_for(result,score=marks))



if __name__=="__main__":
    app.run(debug=True)

