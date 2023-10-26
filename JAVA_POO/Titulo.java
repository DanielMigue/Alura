package br.com.alura.screenmatch.modelos;
//SUPER CLASSE

public class Titulo {
    //Atributos
    private String nome;
    private int anoDelancamento;
    private boolean incluidoNoPlano;
    //private é um "modificador" de visibilidade, ele não deixa ler e nem escrever no atributo, então precisa-se fazer
    //um metódo com get
    //ajuda na segurança e encapsulamento do código
    private double somaDasAvaliacoes;
    private int totalDeAvaliacoes;
    private int duracaoEmMinutos;
    //Aqui se encontra o método com get
    // Quando há existência de funções de dentro da classe, começa a existencia dos métodos

    // MÉTODO GETTERS -  Método de leitura  que retorna o valor de um atributo
    public String getNome() {
        return nome;
    }

    public int getAnoDelancamento() {
        return anoDelancamento;
    }

    public boolean IsIncluidoNoPlano() {
        return incluidoNoPlano;
    }

    public int getDuracaoEmMinutos() {
        return duracaoEmMinutos;
    }

    public int getTotalDeAvaliacoes(){
        return totalDeAvaliacoes;
    }
    //MÉTODOS SETTERS - Método de modificação e atualização dos atributos

    //THIS - o this é usado para acessar o atributo da classe que está sendo atualizado pelo método set.
    public void setNome(String nome) {
        this.nome = nome;
    }


    public void setAnoDelancamento(int anoDelancamento) {
        this.anoDelancamento = anoDelancamento;
    }

    public void setIncluidoNoPlano(boolean incluidoNoPlano) {
        this.incluidoNoPlano = incluidoNoPlano;
    }

    public void setDuracaoEmMinutos(int duracaoEmMinutos) {
        this.duracaoEmMinutos = duracaoEmMinutos;
    }

    public void exibeFichaTecnica(){

        System.out.println("Nome do filme: " + nome);
        System.out.println("Ano de lançamento: " + anoDelancamento);
        System.out.println("Duração em minutos: " + duracaoEmMinutos);
    }
    public void avalia(double nota){
        somaDasAvaliacoes += nota;
        totalDeAvaliacoes++;
    }

    public double pegaMedia(){
        return somaDasAvaliacoes / totalDeAvaliacoes;
    }
}
