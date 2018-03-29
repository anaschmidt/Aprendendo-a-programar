
nomes =['ana','matheus', 'eduardo', 'vitoria', 'pedro']
print(nomes[3])
print(nomes[1])
# função de lista nome da lista.index  um objeto tem propriedade e métodos(função de um objeto que vai fazer alguma coisa)
print(nomes.index('matheus'))
#: cópia da lista operação de corte 
sublista_nomes = nomes[1:4]
print(sublista_nomes)
sublista_nomes2 = nomes[3:]
print(sublista_nomes2)
print(sublista_nomes + sublista_nomes2)
novos = ['brasil', 'bruna']
nomes = novos+nomes
print(nomes)
#nome da lista.append(valor)
nomes.append('cristiano')
print(nomes)

