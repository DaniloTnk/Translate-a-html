# encoding: utf-8
from bs4 import BeautifulSoup
import re, csv

encode = 'utf-8'
doc = open('spec.html')
soup = BeautifulSoup(doc)
texts = soup.text.encode(encode)
texts = re.sub('({.*})|(  )*','',texts)
texts = re.sub("\n+","\n",texts)
texts = texts.splitlines()
texts = list(set(texts))
texts.sort()

csv_file = open('spec.csv','w+')
writer_csv = csv.writer(csv_file, delimiter=';', quoting=csv.QUOTE_ALL)
header = [u'Português', 'Espanhol', u'Qdt de Caracteres em Português']
header[0] = header[0].encode(encode,'replace')
header[2] = header[2].encode(encode,'replace')
writer_csv.writerow(header)
for iten in texts:
	line = [iten, "", str(len(iten))]
	line[0]= str(line[0])
	writer_csv.writerow(line)
doc.close()
csv_file.close()

