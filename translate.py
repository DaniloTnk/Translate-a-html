# encoding: utf-8
import os, fnmatch, re

def translate(id_tuple):
	csv_id = id_tuple[0]
	csv_path = csv_files['paths'][csv_id]
	csv_name = csv_files['file_names'][csv_id]
	html_id = id_tuple[1]
	html_path = html_files['paths'][html_id]
	html_name = html_files['file_names'][html_id]
	with open(csv_path+"/"+csv_name,'r+') as csv_file:
		csv_vector = csv_file.readlines()
	csv_file.closed
	with open(html_path+"/"+html_name,'r+') as html_file:
		html_text = html_file.read()
		for lines in csv_vector:
			lines = lines.split(';')
			ptbr = lines[0]
			es = lines[1]
			ptbr = ptbr.decode('utf-8','replace')
			es = es.decode('utf-8','replace')
			html_text = html_text.replace(ptbr.encode('utf-8','replace'),es.encode('utf-8','replace'))
		html_file.seek(0)
		html_file.write(str(html_text))
		html_file.truncate()
		html_file.closed

def get_index(html_name):
	name_of_file = html_name.split('.')[0]
	try:
		csv_index = csv_files['file_names'].index(name_of_file+'.csv')
	except:
		csv_index = False
	html_index = html_files['file_names'].index(html_name)
	return(csv_index,html_index)

html_files = {
	'paths' : [],
	'file_names' : [],
}

csv_files = { 
	'paths' : [],
	'file_names' : [],
}

for root, dirnames, filenames in os.walk('path_to_HTML_files'):
	for filename in fnmatch.filter(filenames, '*.html'):
		html_files['paths'].append(root)
		html_files['file_names'].append(filename)

for root, dirnames, filenames in os.walk('path_to_CSV_files'):
	for filename in fnmatch.filter(filenames, '*.csv'):
		csv_files['paths'].append(root)
		csv_files['file_names'].append(filename)

for html_file in html_files['file_names']:
	translate(get_index(html_file))
	


