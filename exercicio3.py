
msg= 'How old are you?'
msg2= 'Have you not had a birthday this year yet?'
idade=input(msg)
aniversario=input(msg2)
aniversario=float(aniversario)
print(idade)
idade=float(idade)
print(idade)
ano=2018 - aniversario  #ao responder a msg2 0para sim e 1para não, utilizamos o ano atual menos a resposta da mensagem 2 para correção do bug. 
print(ano-idade)


