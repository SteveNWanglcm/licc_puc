#ex03
dic={
    '2013':{'filme':{ 'Frozen', 'US$':1276480335}, 'filme2':{'US$':0}, 'filme3':{'US$': 0 }, 'filme4':{'US$':0}},
    '2012':{'filme':{ 'Marvel´s The Avengers', 'US$':1518812988},'filme2':{'US$':0}, 'filme3':{'US$': 0 }, 'filme4':{'US$':0}}
    '1997':{'filme':{ 'Titanic', 'US$':2187463944},'filme2':{'US$':0}, 'filme3':{'US$': 0 }, 'filme4':{'US$':0}},
    '2018':{'filme':{ 'Black Panther', 'US$':1346913161}, 'filme2': {'Avengers: Infinity War', 'US$':2048359754}, 'filme': {'Jurassic World: Fallen Kingdom', 'US$':1309484461}, 'filme4':{'US$':0}},
    '2015':{'filme':{ 'Avengers': 'Age of Ultron', 'US$':1405403694}, 'filme2':{'Star Wars: The Force Awakens', 'US$': 2068223624}, 'filme3':{'Furious 7', 'US$':1516045911}, 'filme4':{'Jurassic World', 'US$':1671713208}},
    '2009':{'filme':{ 'Avatar', 'US$':2787965087}, 'filme2':{'US$':0}, 'filme3':{'US$': 0 }, 'filme4':{'US$':0}},
    '2017':{'filme':{ 'Star Wars: The Last Jedi', 'US$':1332539889},  'filme2':{'Beauty and the Beast', 'US$':1263521126}, 'filme3':{'US$': 0 }, 'filme4':{'US$':0}},
    '2019':{'filme':{'Avengers: Endgame', 'US$':2750667499}, 'filme2':{'US$':0}, 'filme3':{'US$': 0 }, 'filme4':{'US$':0}}
}
#ex04

for i in dic:
    i = dic[0]
    valor_arrecadado = dic['filme']['US$'] + dic['filme2']['US$'] + dic['filme3']['US$'] + dic['filme4']['US$']
    print('valor arrecadado em ', i, ':', 'US$', valor_arrecadado );
