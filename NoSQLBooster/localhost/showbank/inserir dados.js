//INSERE VALORES PESSOAIS DE UM CLIENTE
db.clientes.insertOne({"nome":"Allana Esther Lara Monteiro",
"cpf": "207.588.7003-96",
"data_nascimento": "15/03/1962",
"genero":"Feminino",
"profissao":"Servente de obras",
"endereco": "Rua Deuputado João Moura Santos, número 155, Matadouro, Teresina, PI, 64004-340",
"status_civil":"Divorciado(a)"
})


//MOSTRA OS DADOS DO CLIENTE
db.clientes.find() 

//MOSTRA OS DADOS DA CONTA DO CLINETE
db.contas.find()

//INSERE VALORES DA CONTA DE UM CLIENTE
db.contas.insert({
"Numero_Conta": "04938-1",
"Agência":"5575",
"Tipo":"Conta salário",
"CPF":"207.588.703-96",
"Valor":308
})

db.clientes.insert({
    "nome":"Cauê Luan da Paz",
    "cpf":"426.239.760-23",
    "data_nascimento":"16/02/1967",
    "genero":"Masculino",
    "profissao":"Vendedor em comércio atacadista",
    "endereco":"Rua Vinte e Quatro, número 121, Três Vendas, Pelotas, RS, 96071-380",
    "status_civil":"Casado(a)"
})
db.contas.insert({
    "Numero_Conta":"0265177-7",
    "Agência":"0944",
    "Tipo":"Conta salário",
    "CPF":"426.239.760-23",
    "Valor":"1411"
})

