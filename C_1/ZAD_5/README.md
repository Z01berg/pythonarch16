# W Pythonie i Javie mowa jest o różnych terminach, ponieważ są to różne języki programowania z różnymi implementacjami.

- Python jest interpretowany, co oznacza, że kod źródłowy jest przetwarzany przez interpreter Pythona linia po linii w czasie rzeczywistym. Interpreter wykonuje kod źródłowy bezpośrednio, bez konieczności kompilacji do kodu maszynowego. Dlatego w Pythonie mówimy o interpreterze.

	- n
	 x = 5
	 y = 10
	 if x < y:
   	 	print("x jest mniejsze od y")
   	 else:
   	 	print("x jest większe lub równe y")
  
   
 	
- Java jest kompilowana do kodu bajtowego, który następnie jest wykonywany przez maszynę wirtualną Javy (JVM). Kod bajtowy jest językiem pośrednim, który może być uruchomiony na dowolnej platformie, która ma zainstalowaną JVM. Maszyna wirtualna Javy tłumaczy kod bajtowy na kod maszynowy w czasie rzeczywistym podczas wykonywania aplikacji. Dlatego w Javie mówimy o maszynie wirtualnej.

	- public class Example {
    	public static void main(String[] args) {
      		 int x = 5;
        	 int y = 10;
       		 if (x < y) {
             	System.out.println("x jest mniejsze od y");
        	 } else {
            	System.out.println("x jest większe lub równe y");
        	 }
   	   	  }
	   }
