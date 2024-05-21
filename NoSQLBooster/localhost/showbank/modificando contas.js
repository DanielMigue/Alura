db.runCommand({collMod:"contas",//atualiza ou edita
    validator:{
        $jsonSchema:{
            bsonType:"object",
            "additionalProperties": false,
            required:["_id","Numero_Conta","Tipo","CPF","Valor","Agencia"],
            properties:{
                _id:{
                    bsonType:"objectId",
                    description:"informe coretamente o endereço do cliente"
                },
                Numero_Conta:{
                    bsonType:"string",
                    description:"informe corretamente o número da conta."
                },
                Tipo:{
                    bsonType:"string",
                    enum:["Conta corrente","Conta poupança","Conta salário"],
                    description:"informe corretamente o tipo da conta."
                },
                CPF:{
                    bsonType:"string",
                    minLength:14,
                    maxLength:14,
                    description:"informe corretamente o CPF do cliente na conta."
                },
                Valor:{
                    bsonType:"double",
                    description:"informe corretamente o valor da conta"
                }
                Agencia:{
                    bsonType:"string",
                    description:"informe corretamente o número da agência"
                }
                
            }
        }
    },
    validationLevel:"moderate"
})