alert('Boas vindas ao jogo do número secreto');//Exibe mensagem como forma de instrução
let numeroMaximo = 1000;
let numeroSecreto = parseInt(Math.random() * numeroMaximo + 1);// um número inteiro pseudo aleatório
console.log(numeroSecreto);//Console.log imprime mensagens no console do ambiente e permite testar informações relevantes durante a execução de um programa

let chute;// O let significa um espaço na memória onde guardamos uma informação
//e o nome desse espaço é a váriavel numeroSecreto
let tentativas = 1;
//ENQUANTO=while. Enquanto chute nao for igual a uma determinada condição ele executa
while (chute != numeroSecreto) {
    chute = prompt(`Escolha um número entre 1 e ${numeroMaximo}`)// O prompt interagi com a pessoa permitindo inserir um valor
    //O chute é a váriavel na qual a pessoa digitará 

    //CONDIÇÃO
    //IF = Se
    if (numeroSecreto == chute) {
        break;
    }
    //Else = Se não
    else {
        if (chute > numeroSecreto) {
            alert(`O número secreto é menor que o ${chute}`);
        } else {
            alert(`O número secreto é maior que o ${chute}`);
        }
        tentativas++;//contador de tentativas para acompanhar e exibir a quantidade de vezes que o usuário tentou adivinhar
    }
}

let palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa';//operador ternário usado muito no MERCADO DE TRABALHO ele substitui o if e o else
//se for maior que 1 o número de tentativas a palavra tentativa se mantém no plural, se não, vai para o singular.
alert(`Isso ai! Você descobriu o número ${numeroSecreto} na quantidade de ${tentativas} ${palavraTentativa}.`);

//if (tentativas > 1) {
//    alert(`Isso ai! Você descobriu o número ${numeroSecreto} em ${tentativas}º tentativas.`);
//}
//else {
//    alert(`Isso ai! Você descobriu o número ${numeroSecreto} em ${tentativas}º tentativa.`);
//}
