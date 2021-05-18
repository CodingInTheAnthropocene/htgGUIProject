from datetime import datetime
from modules.dataSettings import *
from requests import get


def getCurrency(ID):
    return (get(f'https://catalogue.data.gov.bc.ca/api/3/action/package_show?id={ID}')).json()["result"]["record_last_modified"]

class dataCurrency:
    crownTenures = datetime.strptime(str(getCurrency(crownTenuresSettings.dataCatalogueId)), '%Y-%m-%d')


