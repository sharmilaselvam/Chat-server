from flask import Flask,request,render_template,redirect,url_for,make_response
from random import random
ser=Flask(__name__)

database={"totmes":0}
logedin={}
login_details={'sharmila' :{'password':'sharmi'}}  //to  add user {'name1':{'password':'pass'},'name2':{"password":"pass2"}}


@ser.route('/')
def home():
    return render_template("index.html")



@ser.route('/login',methods=['GET','POST'])
def login():
    if(request.method=='GET'):
        return render_template("login.html",pserror="")
    elif(request.method=='POST'):
        uname=request.form['uname']
        psw=request.form['pass']
        if((uname in login_details) and (psw==login_details[uname]['password'])):
            rm=str(int(random()*(10**16)))
            logedin[request.form["uname"]]=rm
            res=redirect(url_for("chat"))    
            res.set_cookie("uname", uname)
            res.set_cookie("rm",rm)
            return res
        else:
            return render_template("login.html",pserror="Invalid username or password.")

@ser.route('/chat',methods=['GET','POST'])
def chat():
    if(request.method=='GET'):
        uname=request.cookies.get("uname")
        rm=request.cookies.get('rm')
        if(uname in logedin and logedin[uname]==rm):
            return render_template("chat.html",msg=database,user=uname,r=database["totmes"],count=database['totmes'])
        else:
            return render_template('login.html',pserror='you are already loged out....')
    elif(request.method=='POST'):
        uname=request.cookies.get("uname")
        rm=request.cookies.get('rm')
        if(uname in logedin and logedin[uname]==rm):    
            if(request.form['subm']=='s'):
                mes=request.form['mes']
                pos=int(database['totmes'])
                database[pos]=dict(uname=uname,mes=mes)
                database["totmes"]=pos+1
                res=make_response(mes)
                res.headers['count']=database['totmes']
                return res
            else:
                count=int(request.form['count'])
                if(database['totmes']+1>count):
                    ret=""
                    for i in range(count,database['totmes']):
                        if(uname!=database[i]['uname']):
                            ret+='<div class="chat"><p class="amsg"><span class="a">'+database[i]['uname']+'</span><span class="msg">'+database[i]['mes']+'</span></p></div>'
                        else:
                            ret+='<div class="chat"><p class="bmsg"><span class="b">Me</span><span class="msg">'+database[i]['mes']+'</span></p></div>'
                    res=make_response(ret)
                    res.headers['count']=database['totmes']
                    return res
                else:  
                    return ""
        else:
            return make_response(render_template('login.html',pserror='you are already loged out....'),404)
    else:
            return render_template('login.html',pserror='you are already loged out....')
        
        
    
@ser.route('/register',methods=['GET','POST'])
def register():
    if(request.method=='GET'):
        return render_template("register.html")
    elif(request.method=='POST'):
        fsname=request.form['firstname']
        lsname=request.form['lastname']
        password=request.form['pass1']
        repassword=request.form['pass2']
        dept=str(request.form['dept'])
        batch=int(request.form['batch'])
        userr=dperr=bterr=pserr1=pserr2=''
        err=False
        if(len(fsname)<1 or len(lsname)<1):
            userr='this.innerHTML="^ User name is empty";this.style.display="block";'
            err=True
        if(dept.lower() not in ['cse','it','eee','ece','mech','bme','cvil']):
            dperr='this.innerHTML="^ Department field is invalid";this.style.display="block";'
            err=True
        if not (batch<2020 and batch>=2016):
            bterr='this.innerHTML="^ Batch field is invalid";this.style.display="block";'
            err=True
        if(len(password)==0):
            pserr1='this.innerHTML="^ Password is empty";this.style.display="block";'
            err=True
        if(len(repassword)==0):
            pserr2='this.innerHTML="^ Password is empty";this.style.display="block";'
            err=True
        if(password!=repassword):
            pserr2='this.innerHTML="^ Password is empty";this.style.display="block";'
            err=True
        if(err is False):
            login_details[fsname]={'password':password,'dept':dept,'batch':batch}
            return redirect(url_for("login"))
        else:
            return render_template('register.html',userr=userr,dperr=dperr,bterr=bterr,pserr1=pserr1,pserr2=pserr2)
                     
    else:
        return render_template('register.html')

@ser.route('/logout')
def logout():
    uname=request.cookies.get("uname")
    del logedin[uname]
    return redirect(url_for('login'))


if (__name__=='__main__'):
    ser.run("0.0.0.0",8080,True)
