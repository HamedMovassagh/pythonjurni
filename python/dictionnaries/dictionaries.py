capitals={'usa':'whashangton DC',
           'india':'New dwhli',
           'chaina':'beijing',
           'russia':'Moscow' }


capitals.update({'germany':'berlin'})
capitals.update({'usa':'las vegas'})
capitals.pop('chaina')
capitals.clear()

#print(capitals['Moscow'])
#print(capitals.get('germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key,value in capitals.items():
    print(key,value)
