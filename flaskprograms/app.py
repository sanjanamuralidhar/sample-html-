from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/')
def index1():
    return render_template('home.html')
@app.route('/about/')
def index2():
    return render_template('about.html')
@app.route('/contactus/')
def index3():
    return render_template('contactus.html')
@app.route('/send',methods=['GET','POST'])
def index4():
    if (request.method=='POST'):
        getName=request.form['name']
        
        getEmail=request.form['email']
        
        getPhone=request.form['phone']
    
        getSubject=request.form['subject']
        
        getMessage=request.form['message']
        return render_template('result.html',newName=getName) 



if(__name__=='__main__'):
    app.run(debug=True)