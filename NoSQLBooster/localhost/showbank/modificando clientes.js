db.runCommand({collMod:"clientes", //atualiza ou edita
    validator:{
        $jsonSchema:{
            bsonType:"object",
            "additionalProperties": false,
            required:["_id","nome","cpf","status_civil","data_nascimento", "endereco","genero","profissao"],
            properties:{
                _id:{
                    bsonType:"objectId",
                    description:"informe coretamente o endereço do cliente"
                },
                nome:{
                    bsonType:"string",
                    maxLength:150,
                    description:"informe corretamente o nome do cliente."
                },
                cpf:{
                    bsonType:"string",
                    minLength:14,
                    maxLength:14,
                  description:"Informa corretamente o cpf do cliente"
                },
                status_civil:{
                    enum:["Solteiro(a)","Casado(a)","Separado(a)","Divorciado(a)","Viúvo(a)"],
                    description:"informe corretamente o status civil do cliente"
                },
                data_nascimento:{
                    bsonType:["string","null"],
                    description:"informe corretamente a data de nascimento do cliente"
                },
                endereco:{
                    bsonType:"string",
                    description:"informe coretamente o endereço do cliente"
                },
                genero:{
                    bsonType:"string",
                    description:"informe coretamente o gênero do cliente"
                },
                profissao:{
                    bsonType:"string",
                    description:"informe coretamente o profissão do cliente"
                }
            }
        }
    }
}
