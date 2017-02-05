#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""./ngrok http -region=eu 5000"""

import os
import gpxpy
import gpxpy.gpx
import folium

from flask import Flask, send_file, request, redirect, url_for, render_template, abort, flash
from werkzeug.utils import secure_filename

__version__ = 0.1
__author__ = "Artur Wronowski"


UPLOAD_FOLDER = 'uploads'
MAP_FOLDER = 'maps'
ALLOWED_EXTENSIONS = set(['gpx'])

app = Flask(__name__)
app.secret_key = 'some_secret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def genmap(filename, _color='red', _weight='4'):
	""" generuje mape"""
	gpx_file = open(filename, 'r')
	gpx = gpxpy.parse(gpx_file)

	points = []
	if gpx.tracks != 1:
		flash('Brak tras')

	for track in gpx.tracks:
	    for segment in track.segments:        
	        for point in segment.points:
	            points.append(tuple([point.latitude, point.longitude]))

	ave_lat = sum(p[0] for p in points)/len(points)
	ave_lon = sum(p[1] for p in points)/len(points)

	map = folium.Map(location=[ave_lat, ave_lon], zoom_start=13)

	folium.PolyLine(points, color=_color, opacity=0.7, weight=_weight).add_to(map)

	map.save('maps/map.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """formatka upload pliku"""
	# sprawdzanie czy katalogi istnieją
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    if not os.path.exists(MAP_FOLDER):
        os.makedirs(MAP_FOLDER)

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # jeżeli user nie wybrał pliku
        if file.filename == '':
            flash('Nie wybrano pliku')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # save file in folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # generate map
            genmap(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # remove file
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('show_map'))

    return render_template('index.html')


@app.route('/maps/map.html')
def show_map():
	"""pokaż mapę"""
	return send_file('maps/map.html')


if __name__ == '__main__':
	app.run(debug=True, host= '0.0.0.0')