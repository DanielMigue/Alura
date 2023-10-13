// IMPORT serve para importar classes de outros pacotes
//ao lado tem que ter o domínio da empresa ao contrário
import br.com.alura.screenmatch.calculos.CalculadoraDeTempo;
import br.com.alura.screenmatch.calculos.FiltroRecomendacao;
import br.com.alura.screenmatch.modelos.Episodio;
import br.com.alura.screenmatch.modelos.Filme;
import br.com.alura.screenmatch.modelos.Serie;


public class Principal {
    public static void main(String[] args) {
        //O filme especifica, ele é um modelo. Então cria-se uma variável para podermos alterar o nome
        //e fazer manipuações que no caso é o "meuFilme". um objeto chamado br.com.alura.screenmatch.modelos.Filme que cria o objeto.
        Filme meuFilme = new Filme();//na esquerda é o nome da classe e na direita é o objeto que eu quero instanciar
        meuFilme.setNome("The Matrix");
        meuFilme.setAnoDelancamento(1999);
        meuFilme.setDuracaoEmMinutos(135);


        meuFilme.exibeFichaTecnica();
        meuFilme.avalia( 9);
        meuFilme.avalia(8);
        meuFilme.avalia(9);

        //System.out.println(meuFilme.somaDasAvaliacoes);
        System.out.println("Total de avaliações: " + meuFilme.getTotalDeAvaliacoes());
        //System.out.println("Média de avaliações do filme: " + meuFilme.pegaMedia());

        Serie lost = new Serie();
        lost.setNome("lost");
        lost.setAnoDelancamento(2000);
        lost.setDuracaoEmMinutos(50);
        lost.exibeFichaTecnica();
        lost.setTemporadas(10);
        lost.setEpisodiosPortemporada(10);
        lost.setMinutosPorEpisodio(50);
        System.out.println("Duração para maratonar Lost em minutos: " + lost.getDuracaoEmMinutos());

        CalculadoraDeTempo calculadora = new CalculadoraDeTempo();
        calculadora.inclui(meuFilme);
        System.out.println(calculadora.getTempoTotal());

        FiltroRecomendacao filtro = new FiltroRecomendacao();
        filtro.filtra(meuFilme);

        Episodio episodio = new Episodio();
        episodio.setNumero(1);
        episodio.setSerie(lost);
        episodio.setTotalVisualizacoes(300);
        filtro.filtra(episodio);
    }
}
