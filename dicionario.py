'''lista = []
lista.append('macaco')
print(lista[0])
dic = {'nome':'pedro', 'idade':25}
print(dic['nome'])
print(dic['idade'])
print(dic.keys())
print(dic.values()) 
print(dic.items())'''
listap = []
listap.append({'nome':'maria', 'idade':29})
listap.append({'nome':'pedro', 'idade':25})
listap.append({'nome':'carls', 'idade':25})
for dic in listap:
    print(f"{dic['nome'].capitalize()} tem {dic['idade']} anos")
