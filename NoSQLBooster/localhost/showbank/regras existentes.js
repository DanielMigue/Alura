
//COMANDA PARA VERIFICAR AS REGRAS DE VALIDAÇÃO EXISTENTE
db.getCollectionInfos({name:"clientes"})
db.getCollectionInfos({name:"contas"})

//da pra verifica mais de uma coleção ao mesmo tempo
db.runCommand({listCollections:1,filter:{name:"contas"}})