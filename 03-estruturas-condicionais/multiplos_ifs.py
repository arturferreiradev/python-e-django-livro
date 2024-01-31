a = 1
mensagem = 'Nenhuma condição foi executada ainda'

if a==2: 
    mensagem = 'Entrei no primeiro suíte - a vale 2'
elif a==3:
    mensagem = 'Entrei no segundo suíte - a vale 3'
elif a==4:
    mensagem = 'Entrei no terceiro suíte - a vale 4'
else:
    mensagem = 'Entrei no suíte do else - a vale 1'

print(mensagem)

# Obs as cláusulas if, elif e else não devem ser identadas, apenas os suítes devem sofrer identamento.