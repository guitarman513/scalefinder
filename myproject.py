from flask import Flask, render_template, url_for, flash, request, redirect
from werkzeug.utils import secure_filename
import pandas as pd 
import math

import os
from os.path import join, dirname, realpath


app = Flask(__name__)

# PWD = pd.read_csv('templates/data/pass.txt').columns[0]

HITS_PATH = join(dirname(realpath(__file__)), 'static/meta/')
HITS_TEMPLATE_PATH = join(dirname(realpath(__file__)), 'templates/data/hits.csv')

# ALLOWED_EXTENSIONS = {'txt', 'png', 'jpg', 'jpeg', 'gif'}
app.config['HITS_FOLDER'] = HITS_PATH
app.config['HITS_TEMPLATE_PATH'] = HITS_TEMPLATE_PATH

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS





# for logging in jinja
def debug(text):
  print(text)
  return ''


@app.route('/')
def home():
  # store hits on a monthly basis
  currentMonthHitsDir = app.config['HITS_FOLDER']+str(pd.datetime.now().year)+"_"+str(pd.datetime.now().month)+'/'
  currentMonthHitsFile = currentMonthHitsDir + "hits.csv"
  # make current month dir if doesn't already exist
  try:
    os.makedirs(currentMonthHitsDir)
  except FileExistsError as e:
    print(e,"Current Month directory already exists")
  # open current month's hits file if exists
  try:
    hits = pd.read_csv(currentMonthHitsFile,index_col=0)
  except FileNotFoundError as e:
    print(e,"Current Month hits directory DNE. Creating Now.")
    hitstemp = pd.read_csv(HITS_TEMPLATE_PATH,index_col=0)
    hitstemp.to_csv(currentMonthHitsFile)
    hits = pd.read_csv(currentMonthHitsFile,index_col=0)
  
  ip_addr = ''
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    ip_addr = request.environ['REMOTE_ADDR']
  else:
    ip_addr = request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy
  new_log = {'date': pd.datetime.now(), 'IP_ADDR': ip_addr}
  hits=hits.append(new_log, ignore_index=True)
  hits.to_csv(currentMonthHitsFile)
  mastheadText = ["Scale Finder","With Adjustable Stringed Instrument Fret Maps"]
  return render_template('html/guitar.html.jinja', mastheadImage='home-bg.jpg', debug=debug,mastText = mastheadText,str=str)


@app.route('/guitar/')
def guitar():
  mastheadText = ["Guitar","Triads and Neck Map"]
  return render_template('html/guitar.html.jinja', mastheadImage='guitars.jpeg', debug=debug,mastText = mastheadText,str=str)
@app.route('/guitar7/')
def guitar7():
  mastheadText = ["7-Stringed Guitar","Triads and Neck Map"]
  return render_template('html/guitar7.html.jinja', mastheadImage='guitars.jpeg', debug=debug,mastText = mastheadText,str=str)
@app.route('/guitar8/')
def guitar8():
  mastheadText = ["8-Stringed Guitar","Triads and Neck Map"]
  return render_template('html/guitar8.html.jinja', mastheadImage='guitars.jpeg', debug=debug,mastText = mastheadText,str=str)
@app.route('/guitar9/')
def guitar9():
  mastheadText = ["9-Stringed Guitar","Triads and Neck Map"]
  return render_template('html/guitar9.html.jinja', mastheadImage='guitars.jpeg', debug=debug,mastText = mastheadText,str=str)
@app.route('/guitar10/')
def guitar10():
  mastheadText = ["10-Stringed Guitar","Triads and Neck Map"]
  return render_template('html/guitar10.html.jinja', mastheadImage='guitars.jpeg', debug=debug,mastText = mastheadText,str=str)
@app.route('/guitar11/')
def guitar11():
  mastheadText = ["11-Stringed Guitar","Triads and Neck Map"]
  return render_template('html/guitar11.html.jinja', mastheadImage='guitars.jpeg', debug=debug,mastText = mastheadText,str=str)
@app.route('/guitar12/')
def guitar12():
  mastheadText = ["12-Stringed Guitar","Triads and Neck Map"]
  return render_template('html/guitar12.html.jinja', mastheadImage='guitars.jpeg', debug=debug,mastText = mastheadText,str=str)


@app.route('/bass')
def bass():
  mastheadText = ["Bass, Ukulele, and Other 4-Stringed Instruments","Triads and Neck Map"]
  return render_template('html/bass.html.jinja', mastheadImage='guitars.jpeg', debug=debug,mastText = mastheadText,str=str)

@app.route('/bass5')
def bass5():
  mastheadText = ["5-Stringed Bass","Triads and Neck Map"]
  return render_template('html/bass5.html.jinja', mastheadImage='guitars.jpeg', debug=debug,mastText = mastheadText,str=str)


@app.route('/banjo')
def banjo():
  mastheadText = ["Banjo","Triads and Neck Map"]
  return render_template('html/banjo.html.jinja', mastheadImage='banjuh.jpg', debug=debug,mastText = mastheadText,str=str)

@app.route('/all')
def all():
  mastheadText = ["All Instruments",""]
  return render_template('html/all.html.jinja', mastheadImage='allinst.jpeg', debug=debug,mastText = mastheadText,str=str)

@app.route('/learn')
def learn():
  mastheadText = ["Learn",""]
  return render_template('html/learn.html.jinja', mastheadImage='home-bg.jpg', debug=debug,mastText = mastheadText,str=str)



@app.route('/contact')
def contact():
  mastheadText = ["Contact Me",'My email is joe@joemulhern.net']
  return render_template('html/contact.html.jinja', mastheadImage='post-bg.jpg', debug=debug,mastText = mastheadText)


@app.errorhandler(404)
def page_not_found(e):
  mastheadText = ['Uh Oh',"The page you're looking for does not exist."]
  return render_template('html/notFound.html',mastText = mastheadText,mastheadImage = '404.png'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')
