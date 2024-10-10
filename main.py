
# integrate HTML with flask
# HTTP verb GET And POST
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def Welcome():
    return render_template('index.html')



@app.route('/results',methods=["GET"])
def  results():
        physics=int(request.args.get("physics"))
        math=int(request.args.get("math"))
        chemistry=int(request.args.get("chemistry"))
        marks=int(request.args.get("score"))
        result_status=""
        if marks>56:
            result_status="PASS"
        else:
            result_status= "FAIL"
        return render_template("result.html",physics=physics, math=math, chemistry=chemistry,status=result_status)


@app.route('/submit',methods=["POST","GET"])
def submit():
    total_score=0
    if request.method=="POST":
        physics=int(request.form.get('physics'))
        math=int(request.form.get("math"))
        chemistry=int(request.form.get("chemistry"))
        total_score=(physics+math+chemistry)/4
    print(physics)
    print(total_score)
    return redirect(url_for('results',physics=physics, math=math, chemistry=chemistry,score=int(total_score)))
    




if __name__=="__main__":
    app.run(debug=True)

