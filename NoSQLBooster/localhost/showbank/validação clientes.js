use showbank

//Clientes
Nome: texto
cpf: texto
data de nascimento:texto
genero:texto
profissao:texto
endereco:texto
status civil:texto

//Contas
numero da conta: texto
agencia: texto
tipo: texto
cpf: texto
valor: double

db.createCollection("clientes", {
    validator:{
        $jsonSchema:{
            bsonType:"object",
            required:["nome","cpf","status_civil","data_nascimento","genero","endereco"],
            properties:{
                nome:{
                    bsonType:"string",
                    description:"informe corretamente o nome do cliente."
                },
                cpf:{
                    bsonType:"string",
                  description:"Informa corretamente o cpf do cliente"
                },
                status_civil:{
                    enum:["Solteiro(a)","Casado(a)","Separado(a)","Divorciado(a)","Viúvo(a)"],
                    description:"informe corretamente o status civil do cliente"
                },
                data_nascimento:{
                    bsonType:"string",
                    description:"informe corretamente a data de nascimento do cliente"
                },
                endereco:{
                    bsonType:"string",
                    description:"informe coretamente o endereço do cliente"
                }
            }
        }
    }
})