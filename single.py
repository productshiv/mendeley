from mendeley import Mendeley
import yaml
import os
# Get the DOI to look up
import argparse
import openpyxl
from openpyxl import Workbook
'''10.1016/j.saa.2020.118426
10.1016/j.measurement.2020.107793
10.1016/j.jallcom.2020.154573
10.1088/1402-4896/ab978e
10.1016/j.physe.2020.114131
10.1002/cssc.202001302
10.1016/j.jallcom.2020.154038
10.1088/1361-6463/ab7cf9
'''

config_file = 'config.yml'
config = {}
if os.path.isfile(config_file): 
    with open('config.yml') as f:
        config = yaml.load(f)
else:
    config['clientId'] = os.environ.get('MENDELEY_CLIENT_ID')
    config['clientSecret'] = os.environ.get('MENDELEY_CLIENT_SECRET')
men = Mendeley(config['clientId'], config['clientSecret'])
session = men.start_client_credentials_flow().authenticate()

def autometa(doi):
    doc = session.catalog.by_identifier(doi=doi, view='stats')
    print ('"%s" has %s readers. \n' % (doc.title, doc.reader_count_by_academic_status))

    
autometa("10.1016/j.jlumin.2019.116996")
