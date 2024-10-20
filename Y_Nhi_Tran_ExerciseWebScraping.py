# Y Nhi Tran
# Exercise Web Scraping

from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import defaultdict

# Open the website
# Get URL
html = urlopen("https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions_per_capita")
# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Initialize a defaultdict
dict = defaultdict()
# Find the table in the site
table = soup.find('table', class_='wikitable sortable')

# Collect data
for row in table.find_all('tr')[1:]:
    # Find all info of td - table data in the site
    column = row.find_all('td')
    # Collect data and format them (country - strip(), number data - replace \xa0 and \n)
    if column:
        country = column[0].text.strip()
        year1 = column[1].text.replace('\xa0', '')
        year2 = column[14].text.replace('\n', '')
        # Store data in the default dict
        dict[country] = (year1, year2)

# Print collected data
print("Production-based emissions: annual carbon dioxide emissions in metric tons per capita in 1980 and 2018")
print("{:>46} {:>9} {:>10}".format("COUNTRY NAME", "1980", "2018"))
for k, v in dict.items():
    y1, y2 = v
    print(f'{k:>46}' + "{:>10} {:>10}".format(y1, y2))
# Print the dict
print(dict)

# OUTPUT
# Production-based emissions: annual carbon dioxide emissions in metric tons per capita in 1980 and 2018
#                                   COUNTRY NAME      1980       2018
#                                    Afghanistan       0.1        0.3
#                                        Albania       1.9        1.6
#                                        Algeria       3.4        3.9
#                                 American Samoa        ..         ..
#                                        Andorra        ..        6.0
#                                         Angola       0.6        1.0
#                            Antigua and Barbuda       1.9        6.2
#                                      Argentina       3.9        4.7
#                                        Armenia        ..        2.0
#                                          Aruba        ..        9.3
#                                      Australia      15.0       16.8
#                                        Austria       6.9        8.2
#                                     Azerbaijan        ..        3.5
#                                        Bahamas      37.9        7.7
#                                        Bahrain      21.9       21.8
#                                     Bangladesh       0.1        0.6
#                                       Barbados       2.7       11.6
#                                        Belarus        ..        6.8
#                                        Belgium      13.7        9.2
#                                         Belize       1.3        1.2
#                                          Benin       0.1        0.7
#                                        Bermuda       8.0        7.2
#                                         Bhutan       0.1        1.9
#                                        Bolivia       0.8        2.0
#                         Bosnia and Herzegovina        ..        7.8
#                                       Botswana       1.0        3.2
#                                         Brazil       1.5        2.4
#                         British Virgin Islands       2.7        4.8
#                                         Brunei      35.5       16.0
#                                       Bulgaria       8.7        6.3
#                                   Burkina Faso       0.1        0.2
#                                        Burundi       0.0        0.0
#                                     Cape Verde       0.4        1.9
#                                       Cambodia       0.0        0.7
#                                       Cameroon       0.5        0.6
#                                         Canada      18.0       16.1
#                                 Cayman Islands      10.0        8.1
#                       Central African Republic       0.0        0.1
#                                           Chad       0.0        0.0
#                                          Chile       2.2        5.0
#                                          China       1.5        8.0
#                                       Colombia       1.6        1.8
#                                        Comoros       0.2        0.3
#               Democratic Republic of the Congo       0.1        0.0
#                          Republic of the Congo       0.2        1.3
#                                   Cook Islands        ..        2.4
#                                     Costa Rica       1.0        1.8
#                                    Ivory Coast       0.8        0.6
#                                        Croatia        ..        4.7
#                                           Cuba       3.2        2.4
#                                        Curaçao        ..       52.1
#                                         Cyprus       4.7        6.3
#                                 Czech Republic        ..       10.4
#                                        Denmark      11.8        5.8
#                                       Djibouti       1.0        1.1
#                                       Dominica       0.5        1.7
#                             Dominican Republic       1.1        2.3
#                                        Ecuador       1.7        2.6
#                                          Egypt       1.0        2.5
#                                    El Salvador       0.5        1.2
#                              Equatorial Guinea       0.2        2.5
#                                        Eritrea        ..        0.2
#                                        Estonia        ..       18.6
#                                       Eswatini       0.8        0.9
#                                       Ethiopia       0.1        0.2
#                               Falkland Islands        ..       13.6
#                                  Faroe Islands        ..        0.0
#                                           Fiji       1.3        1.4
#                                        Finland      12.2        8.8
#                                         France       9.1        5.0
#                                  French Guiana        ..        2.6
#                               French Polynesia       1.9        2.0
#                                          Gabon       9.1        3.2
#                                         Gambia       0.3        0.3
#                                        Georgia        ..        2.8
#                                        Germany        ..        9.1
#                                          Ghana       0.2        0.7
#                                      Gibraltar       2.9       19.6
#                                         Greece       5.3        6.5
#                                      Greenland      11.2        9.4
#                                        Grenada       0.5        2.7
#                                     Guadeloupe        ..        5.2
#                                           Guam        ..        0.1
#                                      Guatemala       0.6        1.2
#                                         Guinea       0.2        0.2
#                                  Guinea-Bissau       0.2        0.2
#                                         Guyana       2.3        2.5
#                                          Haiti       0.1        0.3
#                                       Honduras       0.6        1.1
#                                      Hong Kong       3.3        6.1
#                                        Hungary       8.1        5.4
#                                        Iceland       8.2       12.1
#                                          India       0.5        1.9
#                                      Indonesia       0.6        2.1
#                                           Iran       3.1        8.9
#                                           Iraq       3.3        4.8
#                                        Ireland       7.7        7.7
#                                    Isle of Man        ..         ..
#                                         Israel       5.5        7.9
#                                          Italy       6.9        5.8
#                                        Jamaica       3.9        2.7
#                                          Japan       8.1        9.4
#                                         Jordan       2.0        2.6
#                                     Kazakhstan        ..       16.8
#                                          Kenya       0.4        0.4
#                                       Kiribati       0.5        0.3
#                                    North Korea        ..        1.2
#                                    South Korea       3.5       13.6
#                                         Kosovo        ..         ..
#                                         Kuwait      18.0       23.9
#                                     Kyrgyzstan        ..        1.7
#                                           Laos       0.1        0.5
#                                         Latvia        ..        4.1
#                                        Lebanon       2.4        4.2
#                                        Lesotho        ..        0.3
#                                        Liberia       1.1        0.3
#                                          Libya       8.4        8.7
#                                  Liechtenstein        ..         ..
#                                      Lithuania        ..        5.0
#                                     Luxembourg      30.3       16.9
#                                          Macau       2.2        2.0
#                                North Macedonia        ..        3.9
#                                     Madagascar       0.2        0.2
#                                         Malawi       0.1        0.1
#                                       Malaysia       2.0        8.0
#                                       Maldives       0.3        2.0
#                                           Mali       0.1        0.1
#                                          Malta       3.2        3.5
#                               Marshall Islands        ..         ..
#                                     Martinique        ..        6.4
#                                     Mauritania       0.4        0.7
#                                      Mauritius       0.6        3.5
#                                         Mexico       3.9        3.8
#                 Federated States of Micronesia        ..         ..
#                                        Moldova        ..        2.1
#                                         Monaco        ..        5.0
#                                       Mongolia       4.1        6.3
#                                     Montenegro        ..        6.3
#                                        Morocco       0.8        1.9
#                                     Mozambique       0.3        0.3
#                                        Myanmar       0.2        0.6
#                                        Namibia        ..        1.7
#                                          Nauru      16.7         ..
#                                          Nepal       0.0        0.3
#                                    Netherlands      12.5        9.5
#                                  New Caledonia      14.3       26.2
#                                    New Zealand       5.6        7.7
#                                      Nicaragua       0.6        1.0
#                                          Niger       0.1        0.1
#                                        Nigeria       0.9        0.6
#                                         Norway       9.3        9.4
#                                           Oman       5.2       17.6
#                                       Pakistan       0.4        1.0
#                                          Palau      12.9       58.0
#                                         Panama       1.6        2.8
#                               Papua New Guinea       0.6        0.5
#                                       Paraguay       0.5        1.1
#                                           Peru       1.4        1.8
#                                    Philippines       0.8        1.4
#                                         Poland      13.1        8.8
#                                       Portugal       2.8        5.1
#                                    Puerto Rico        ..        0.9
#                                          Qatar      58.5       38.2
#                                        Réunion        ..        3.4
#                                        Romania       8.8        4.1
#                                         Russia        ..       12.1
#                                         Rwanda       0.1        0.1
#                                          Samoa       0.6        0.7
#                                     San Marino        ..        5.8
#                          São Tomé and Príncipe       0.4        0.7
#                                   Saudi Arabia      17.4       18.6
#                                        Senegal       0.6        0.7
#                                         Serbia        ..        6.3
#                                     Seychelles       1.5       10.3
#                                   Sierra Leone       0.2        0.2
#                                      Singapore      13.0        9.7
#                                   Sint Maarten        ..         ..
#                                       Slovakia        ..        7.0
#                                       Slovenia        ..        7.5
#                                Solomon Islands       0.4        0.2
#                                        Somalia       0.1        0.1
#                                   South Africa       7.7        8.3
#                                    South Sudan        ..        0.4
#                                          Spain       5.7        6.0
#                                      Sri Lanka       0.2        1.1
#   Saint Helena, Ascension and Tristan da Cunha        ..        4.4
#                          Saint Kitts and Nevis       1.2        4.4
#                                    Saint Lucia       1.0        2.1
#                      Saint Pierre and Miquelon        ..       12.5
#               Saint Vincent and the Grenadines       0.4        1.7
#                                          Sudan       0.2        0.4
#                                       Suriname       6.5        4.0
#                                         Sweden       8.6        4.5
#                                    Switzerland       6.4        4.8
#                                          Syria       2.3        1.6
#                                         Taiwan        ..       12.0
#                                     Tajikistan        ..        0.7
#                                       Tanzania       0.1        0.2
#                                       Thailand       0.8        4.1
#                                    Timor-Leste        ..        0.2
#                                           Togo       0.3        0.4
#                                          Tonga       0.4        1.1
#                            Trinidad and Tobago      15.6       26.2
#                                        Tunisia       1.5        2.8
#                                         Turkey       1.7        5.1
#                                   Turkmenistan        ..       14.4
#                       Turks and Caicos Islands        ..        4.7
#                                         Tuvalu        ..         ..
#                                         Uganda       0.0        0.1
#                                        Ukraine        ..        4.5
#                           United Arab Emirates      35.4       22.4
#                                 United Kingdom      10.3        5.6
#                                  United States      20.8       16.1
#                                        Uruguay       2.0        2.0
#                                     Uzbekistan        ..        3.1
#                                        Vanuatu       0.5        0.3
#                                      Venezuela       5.9        3.7
#                                        Vietnam       0.3        2.8
#                   United States Virgin Islands        ..         ..
#                             West Bank and Gaza        ..         ..
#                                          Yemen       0.4        0.4
#                                         Zambia       0.6        0.3
#                                       Zimbabwe       1.3        0.8
# defaultdict(None, {'Afghanistan': ('0.1', '0.3'), 'Albania': ('1.9', '1.6'), 'Algeria': ('3.4', '3.9'), 'American Samoa': ('..', '..'), 'Andorra': ('..', '6.0'), 'Angola': ('0.6', '1.0'), 'Antigua and Barbuda': ('1.9', '6.2'), 'Argentina': ('3.9', '4.7'), 'Armenia': ('..', '2.0'), 'Aruba': ('..', '9.3'), 'Australia': ('15.0', '16.8'), 'Austria': ('6.9', '8.2'), 'Azerbaijan': ('..', '3.5'), 'Bahamas': ('37.9', '7.7'), 'Bahrain': ('21.9', '21.8'), 'Bangladesh': ('0.1', '0.6'), 'Barbados': ('2.7', '11.6'), 'Belarus': ('..', '6.8'), 'Belgium': ('13.7', '9.2'), 'Belize': ('1.3', '1.2'), 'Benin': ('0.1', '0.7'), 'Bermuda': ('8.0', '7.2'), 'Bhutan': ('0.1', '1.9'), 'Bolivia': ('0.8', '2.0'), 'Bosnia and Herzegovina': ('..', '7.8'), 'Botswana': ('1.0', '3.2'), 'Brazil': ('1.5', '2.4'), 'British Virgin Islands': ('2.7', '4.8'), 'Brunei': ('35.5', '16.0'), 'Bulgaria': ('8.7', '6.3'), 'Burkina Faso': ('0.1', '0.2'), 'Burundi': ('0.0', '0.0'), 'Cape Verde': ('0.4', '1.9'), 'Cambodia': ('0.0', '0.7'), 'Cameroon': ('0.5', '0.6'), 'Canada': ('18.0', '16.1'), 'Cayman Islands': ('10.0', '8.1'), 'Central African Republic': ('0.0', '0.1'), 'Chad': ('0.0', '0.0'), 'Chile': ('2.2', '5.0'), 'China': ('1.5', '8.0'), 'Colombia': ('1.6', '1.8'), 'Comoros': ('0.2', '0.3'), 'Democratic Republic of the Congo': ('0.1', '0.0'), 'Republic of the Congo': ('0.2', '1.3'), 'Cook Islands': ('..', '2.4'), 'Costa Rica': ('1.0', '1.8'), 'Ivory Coast': ('0.8', '0.6'), 'Croatia': ('..', '4.7'), 'Cuba': ('3.2', '2.4'), 'Curaçao': ('..', '52.1'), 'Cyprus': ('4.7', '6.3'), 'Czech Republic': ('..', '10.4'), 'Denmark': ('11.8', '5.8'), 'Djibouti': ('1.0', '1.1'), 'Dominica': ('0.5', '1.7'), 'Dominican Republic': ('1.1', '2.3'), 'Ecuador': ('1.7', '2.6'), 'Egypt': ('1.0', '2.5'), 'El Salvador': ('0.5', '1.2'), 'Equatorial Guinea': ('0.2', '2.5'), 'Eritrea': ('..', '0.2'), 'Estonia': ('..', '18.6'), 'Eswatini': ('0.8', '0.9'), 'Ethiopia': ('0.1', '0.2'), 'Falkland Islands': ('..', '13.6'), 'Faroe Islands': ('..', '0.0'), 'Fiji': ('1.3', '1.4'), 'Finland': ('12.2', '8.8'), 'France': ('9.1', '5.0'), 'French Guiana': ('..', '2.6'), 'French Polynesia': ('1.9', '2.0'), 'Gabon': ('9.1', '3.2'), 'Gambia': ('0.3', '0.3'), 'Georgia': ('..', '2.8'), 'Germany': ('..', '9.1'), 'Ghana': ('0.2', '0.7'), 'Gibraltar': ('2.9', '19.6'), 'Greece': ('5.3', '6.5'), 'Greenland': ('11.2', '9.4'), 'Grenada': ('0.5', '2.7'), 'Guadeloupe': ('..', '5.2'), 'Guam': ('..', '0.1'), 'Guatemala': ('0.6', '1.2'), 'Guinea': ('0.2', '0.2'), 'Guinea-Bissau': ('0.2', '0.2'), 'Guyana': ('2.3', '2.5'), 'Haiti': ('0.1', '0.3'), 'Honduras': ('0.6', '1.1'), 'Hong Kong': ('3.3', '6.1'), 'Hungary': ('8.1', '5.4'), 'Iceland': ('8.2', '12.1'), 'India': ('0.5', '1.9'), 'Indonesia': ('0.6', '2.1'), 'Iran': ('3.1', '8.9'), 'Iraq': ('3.3', '4.8'), 'Ireland': ('7.7', '7.7'), 'Isle of Man': ('..', '..'), 'Israel': ('5.5', '7.9'), 'Italy': ('6.9', '5.8'), 'Jamaica': ('3.9', '2.7'), 'Japan': ('8.1', '9.4'), 'Jordan': ('2.0', '2.6'), 'Kazakhstan': ('..', '16.8'), 'Kenya': ('0.4', '0.4'), 'Kiribati': ('0.5', '0.3'), 'North Korea': ('..', '1.2'), 'South Korea': ('3.5', '13.6'), 'Kosovo': ('..', '..'), 'Kuwait': ('18.0', '23.9'), 'Kyrgyzstan': ('..', '1.7'), 'Laos': ('0.1', '0.5'), 'Latvia': ('..', '4.1'), 'Lebanon': ('2.4', '4.2'), 'Lesotho': ('..', '0.3'), 'Liberia': ('1.1', '0.3'), 'Libya': ('8.4', '8.7'), 'Liechtenstein': ('..', '..'), 'Lithuania': ('..', '5.0'), 'Luxembourg': ('30.3', '16.9'), 'Macau': ('2.2', '2.0'), 'North Macedonia': ('..', '3.9'), 'Madagascar': ('0.2', '0.2'), 'Malawi': ('0.1', '0.1'), 'Malaysia': ('2.0', '8.0'), 'Maldives': ('0.3', '2.0'), 'Mali': ('0.1', '0.1'), 'Malta': ('3.2', '3.5'), 'Marshall Islands': ('..', '..'), 'Martinique': ('..', '6.4'), 'Mauritania': ('0.4', '0.7'), 'Mauritius': ('0.6', '3.5'), 'Mexico': ('3.9', '3.8'), 'Federated States of Micronesia': ('..', '..'), 'Moldova': ('..', '2.1'), 'Monaco': ('..', '5.0'), 'Mongolia': ('4.1', '6.3'), 'Montenegro': ('..', '6.3'), 'Morocco': ('0.8', '1.9'), 'Mozambique': ('0.3', '0.3'), 'Myanmar': ('0.2', '0.6'), 'Namibia': ('..', '1.7'), 'Nauru': ('16.7', '..'), 'Nepal': ('0.0', '0.3'), 'Netherlands': ('12.5', '9.5'), 'New Caledonia': ('14.3', '26.2'), 'New Zealand': ('5.6', '7.7'), 'Nicaragua': ('0.6', '1.0'), 'Niger': ('0.1', '0.1'), 'Nigeria': ('0.9', '0.6'), 'Norway': ('9.3', '9.4'), 'Oman': ('5.2', '17.6'), 'Pakistan': ('0.4', '1.0'), 'Palau': ('12.9', '58.0'), 'Panama': ('1.6', '2.8'), 'Papua New Guinea': ('0.6', '0.5'), 'Paraguay': ('0.5', '1.1'), 'Peru': ('1.4', '1.8'), 'Philippines': ('0.8', '1.4'), 'Poland': ('13.1', '8.8'), 'Portugal': ('2.8', '5.1'), 'Puerto Rico': ('..', '0.9'), 'Qatar': ('58.5', '38.2'), 'Réunion': ('..', '3.4'), 'Romania': ('8.8', '4.1'), 'Russia': ('..', '12.1'), 'Rwanda': ('0.1', '0.1'), 'Samoa': ('0.6', '0.7'), 'San Marino': ('..', '5.8'), 'São Tomé and Príncipe': ('0.4', '0.7'), 'Saudi Arabia': ('17.4', '18.6'), 'Senegal': ('0.6', '0.7'), 'Serbia': ('..', '6.3'), 'Seychelles': ('1.5', '10.3'), 'Sierra Leone': ('0.2', '0.2'), 'Singapore': ('13.0', '9.7'), 'Sint Maarten': ('..', '..'), 'Slovakia': ('..', '7.0'), 'Slovenia': ('..', '7.5'), 'Solomon Islands': ('0.4', '0.2'), 'Somalia': ('0.1', '0.1'), 'South Africa': ('7.7', '8.3'), 'South Sudan': ('..', '0.4'), 'Spain': ('5.7', '6.0'), 'Sri Lanka': ('0.2', '1.1'), 'Saint Helena, Ascension and Tristan da Cunha': ('..', '4.4'), 'Saint Kitts and Nevis': ('1.2', '4.4'), 'Saint Lucia': ('1.0', '2.1'), 'Saint Pierre and Miquelon': ('..', '12.5'), 'Saint Vincent and the Grenadines': ('0.4', '1.7'), 'Sudan': ('0.2', '0.4'), 'Suriname': ('6.5', '4.0'), 'Sweden': ('8.6', '4.5'), 'Switzerland': ('6.4', '4.8'), 'Syria': ('2.3', '1.6'), 'Taiwan': ('..', '12.0'), 'Tajikistan': ('..', '0.7'), 'Tanzania': ('0.1', '0.2'), 'Thailand': ('0.8', '4.1'), 'Timor-Leste': ('..', '0.2'), 'Togo': ('0.3', '0.4'), 'Tonga': ('0.4', '1.1'), 'Trinidad and Tobago': ('15.6', '26.2'), 'Tunisia': ('1.5', '2.8'), 'Turkey': ('1.7', '5.1'), 'Turkmenistan': ('..', '14.4'), 'Turks and Caicos Islands': ('..', '4.7'), 'Tuvalu': ('..', '..'), 'Uganda': ('0.0', '0.1'), 'Ukraine': ('..', '4.5'), 'United Arab Emirates': ('35.4', '22.4'), 'United Kingdom': ('10.3', '5.6'), 'United States': ('20.8', '16.1'), 'Uruguay': ('2.0', '2.0'), 'Uzbekistan': ('..', '3.1'), 'Vanuatu': ('0.5', '0.3'), 'Venezuela': ('5.9', '3.7'), 'Vietnam': ('0.3', '2.8'), 'United States Virgin Islands': ('..', '..'), 'West Bank and Gaza': ('..', '..'), 'Yemen': ('0.4', '0.4'), 'Zambia': ('0.6', '0.3'), 'Zimbabwe': ('1.3', '0.8')}
