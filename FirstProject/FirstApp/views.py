from django.shortcuts import render
from django.http import HttpResponse
def display(request):
    ss='''
        <center>
            <h2 style="color:Blue;">
                Hello User, Welcome to Django First-Project First-App
            </h2>
            <hr/>
            <img src="https://th.bing.com/th/id/OIP.ll1sZ-Vtq3O-994SItTlfQHaFj?pid=ImgDet&rs=1" />            
        </center>
        '''
    return HttpResponse(ss)

def show(request):
    print("welcome url is requested and show() is executed")
    ss=''' 
        <html>
            <head>
                <style>
                    h1{
                      color:blue;
                      width: 90%;
                    }
                    h2{
                      color:green;
                      width: 80%;
                    }
                    h3{
                      color:red;
                      width: 70%;
                    }
                    h1,h2,h3{
                      background-color: lightblue;
                      border: 2px solid brown;
                    }
                </style>
            </head>
            <body>
                 <center>
                    <h1>Hello user..!</h1>
                    <hr color="brown" width="80%"/>
                    <h2>welcome to Django-app</h2>
                    <hr color="brown" width="60%"/>
                    <h3>Have a nice day</h3>
                    <hr color="brown" width="40%"/>
            '''
    return HttpResponse(ss)
    
import time
def senddatetime(request):
    print("dtime url is requested and senddatetime() executed")
    ct=time.ctime()
    ss='''
        <html>
		    <head>
			    <title>Date-time Webpage</title>
			    <style>
				    h1{
					    color:Blue;
					    width:90%;
				    }
				    h2{
					    color:Green;
					    width:80%;
				    }
				    h3{
					    color:Red;
					    width:70%;
				    }
				    h1,h2,h3{
					    background-color:lightgreen;
					    border:2px Solid Brown;
				    }
			    </style>
		    </head>
		    <body>
			    <center>
				    <h1>Welcome to DJango-User..!!!</h1>
				    <hr color='brown' width='80%'/>
				    <h2>Server-Date & Time :: </h2>
				    <hr color='brown' width='70%'/>
				    <h3>''',ct,'''</h3>
				    <hr color='brown' width='60%'/>
			    </center>
		    </body>
	    </html>
	    '''
	
    
    return HttpResponse(ss)
    
def demo(request):
    print('Multiple-Request-URLs same response') 
    htmldata='''
            <center>
                <h1>Welcome Demo User!!!</h1>
                <hr/>
                <h2>This is Same-Output for diff-mulitple-Requests-URLs</h2>
                <hr/>
                <h3>have a great day</h3>
                <hr/>
            </center>
            '''
    return HttpResponse(htmldata)

def homepage(request):
    htmldata='''
            <center>
                <h1>welcome to DEFAULT homepage..!</h1>
                <hr/>
                <h2>Your request page is not found<h2>
                <hr/>
                <h3>Plz try other URL or Links...</h3>
                <hr/>
            </center>
            '''
    return HttpResponse(htmldata)            
    


                    
