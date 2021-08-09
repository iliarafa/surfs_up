#importing dependancies

import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#set up the database
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect database
Base = automap_base()
Base.prepare(engine, reflect=True)

# save references
Measurement = Base.classes.measurement
Station = Base.classes.station

# link to database
session = Session(engine)

# setting up flask
import app
app = Flask(__name__)
@app.route("/")


def welcome():
    return(
    '''
    Welcome to the Climate Analysis API! n/
    Available Routes: n/
    /api/v1.0/precipitation n/
    /api/v1.0/stations n/
    /api/v1.0/tobs n/
    /api/v1.0/temp/start/end
    ''')

