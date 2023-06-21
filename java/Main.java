
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main
{
	public static void main(String[] args) throws Exception {
	    Main t = new Main();		
       t.faca1("ababa");
       // t.faca2();
    }
    
    public void faca1(String w) throws Exception {
        List<Double> means = new ArrayList<>();
        try {
            AFD a = new AFD();
            for (int i = 0; i < 15; i++) {
                System.out.println("Iteracao: " + (i + 1));
                long start = System.currentTimeMillis();

                for (int j = 0; j < 100000; j++) {
                    a.ler("./AFD.XML");
                    // Aqui você pode adicionar a lógica correspondente em Java para processar o arquivo XML
                }

                long end = System.currentTimeMillis();
                double timer = (end - start) / 1000.0;
                means.add(timer);
            }

            System.out.println("Tempos decorrido: " + means);
    }
    catch(Exception e) {
                System.out.println(e);
            }
}

    public void faca2() {
        AFN a = new AFN();
        try {
               a.ler("./AFN01.XML");
               System.out.println("AFN M = "+a);
               System.out.println(("AFD M' = " + a.toAFD()).toString());
        } catch (Exception e){
               System.out.println(e);
        }     
    }
}
