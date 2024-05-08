credenciais_clientes = {
    'alice123': {
        'username': 'alice123',
        'password' : 'alic3P@ssw0rd',
        'status' : 'actuve'},
    'bob456': {'username': 'bob456',
               'password': 'b0bP@ssword!',
               'status':'inactive'},
    'charlie789': {'username': 'charlie789',
                   'password': 'Ch@rlieP@ss9',
                   'status': 'active'}
}

#resposta letra D 
alerta = 'Enviar alerta!' if credenciais_clientes['bob456']['status'] == 'inictive' else 'Sem alerta'