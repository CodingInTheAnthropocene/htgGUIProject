from datetime import datetime
from modules.dataSettings import *
from requests import get




def getCurrency(ID):
    r= get(f'https://catalogue.data.gov.bc.ca/api/3/action/package_show?id={ID}').json()["result"]["record_last_modified"]

    return datetime.strptime(str(r), '%Y-%m-%d').date()


