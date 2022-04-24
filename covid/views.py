import requests
from django.shortcuts import render

# Create your views here.
def reports_display(request):
    try:
        req_obj           = requests.get('https://api.covid19api.com/summary',timeout=10)
        data              = req_obj.json()
        global_list       = [{k:v for k,v in data['Global'].items()}]
        current_date_time = data['Date'].split('T')[0] + ' ' + data['Date'].split('T')[1].split('.')[0]
        countries         = data['Countries']
        country_list      = []
        for c in countries:
            empty_dict = {}
            empty_dict['Country']        = str(c['Country'].replace('_',' '))
            empty_dict['CountryCode']    = str(c['CountryCode'].replace('_',' '))
            empty_dict['Slug']           = str(c['Slug'].replace('_',' '))
            empty_dict['NewConfirmed']   = str(c['NewConfirmed'])
            empty_dict['TotalConfirmed'] = str(c['TotalConfirmed'])
            empty_dict['NewDeaths']      = str(c['NewDeaths'])
            empty_dict['TotalDeaths']    = str(c['TotalDeaths'])
            empty_dict['NewRecovered']   = str(c['NewRecovered'])
            empty_dict['TotalRecovered'] = str(c['TotalRecovered'])
            empty_dict['Date']           = str(c['Date'].split('T')[0] + ' ' + c['Date'].split('T')[1].split('.')[0])
            country_list.append(empty_dict)
        return render(request, 'reports.html', {'global_list': global_list,'current_date': current_date_time,'country_list': country_list})
    except Exception as e :
        print(e)
        return render(request, 'reports.html')


def graphical_display(request):
    return render(request, 'graphical.html')