import json
import requests

accuweatherAPIKey = 'wpX3VvyAXJNxAK33VBQFZLGHhPqvY8V4'


def takeCoordenations():
    r = requests.get('http://www.geoplugin.net/json.gp?')

    if (r.status_code != 200):
        print('Não foi possivél obter a suas localização..')
        return None
    else:
        try:
            # Retorno a localização com JSON
            localizacao = json.loads(r.text)
            coodernadas = {}

            # Acessando a longitude e latitude da api de localização
            coodernadas['lat'] = localizacao['geoplugin_latitude']
            coodernadas['long'] = localizacao['geoplugin_longitude']
            return coodernadas
        except:
            return None


def takeCodeLocalizacion(lat, long):
    # Api de URL de localização na accuweater
    LocalizacionApiUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/" \
        + "search?apikey=" + accuweatherAPIKey \
        + "&q=" + lat + "%2C" + long + "&language=pt-br"

    # Fazendo uma nova requisição com accuweather
    r = requests.get(LocalizacionApiUrl)

    # Validando a URL LocalizacionApiUrl
    if (r.status_code != 200):
        print('Não foi possivél obter o clima atual.')
        return None
    else:
        try:
            LocationResponse = json.loads(r.text)

            infoLocal = {}

            # Pegando o nome do local:
            infoLocal['nomeLocal'] = LocationResponse['LocalizedName'] + ' , '\
                + LocationResponse['AdministrativeArea']['LocalizedName'] + ' . '\
                + LocationResponse['Country']['LocalizedName']
            # Pegando o código do local:
            infoLocal['codigoLocal'] = LocationResponse['Key']
            return infoLocal
        except:
            return None


def weatherNow(codigoLocal, nomeLocal):

    # Retornando o clima de uma localização:
    CurrentCondicionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" \
        + codigoLocal + "?apikey=" + accuweatherAPIKey \
        + "& language=pt-br"

    r = requests.get(CurrentCondicionsAPIUrl)
    # Validando a URL LocalizacionApiUrl
    if (r.status_code != 200):
        print('Não foi possivél obter a sua localização.')
        return None
    else:
        try:
            CurrentCondicionsResponse = json.loads(r.text)
            infoClima = {}
            infoClima['textoClima'] = CurrentCondicionsResponse[0]['WeatherText']
            infoClima['temperatura'] = CurrentCondicionsResponse[0]['Temperature']['Metric']['Value']
            infoClima['nomeLocal'] = nomeLocal
            return infoClima
        except:
            return None

# Begin the System


coodernadas = takeCoordenations()

try:
    local = takeCodeLocalizacion(coodernadas['lat'], coodernadas['long'])
    climaAtual = weatherNow(local['codigoLocal'], local['nomeLocal'])
    print('Clima atual em: ', climaAtual['nomeLocal'])
    print(climaAtual['textoClima'])
    print('Temperatura: ', str(climaAtual['temperatura']) + '\xb0' + 'C')
except:
    print('Erro ao processar a solicitação.')
