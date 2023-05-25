
public class Main
{
	public static void main(String[] args) {
	    Main t = new Main();		
       t.faca1("ababa");
       // t.faca2();
    }
    
    public void faca1(String w) {
        AFD a = new AFD();
        try {
               a.ler("./AFD.XML");
               System.out.println("AFD M = "+a);
               if (a.Aceita(w))
                   System.out.println("Aceitou "+w);
               System.out.println("Pe(q0,"+w+"):"+a.pe(a.getEstadoInicial(),w));
        } catch (Exception e){
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
