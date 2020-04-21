from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


engine = create_engine("sqlite:///titanic.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to the table
Passenger = Base.classes.passenger



