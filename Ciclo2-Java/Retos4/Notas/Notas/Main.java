package Notas;

import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    
    public static void main(String[] args) {
        // TODO code application logic here
        ArrayList<Estudiante> grupo = new ArrayList<>();
        grupo.add(new Estudiante("Valeria Di", "10367876345", 1.8, 3, 10));         
        grupo.add(new Estudiante("Johan Doe", "1037645345", 3.4, 2, 7));            
        grupo.add(new Estudiante("Maurice Doe", "98765234", 4.5, 8, 13));           
        grupo.add(new Estudiante("Matthew Doe", "1036789453", 1.8, 8, 16));         
        grupo.add(new Estudiante("Agustina Doe", "10003456", 3.4, 7, 15));          
        grupo.add(new Estudiante("Agustina Doe", "10003456", 0.5, 3, 12));          
        grupo.add(new Estudiante("Milena Doe", "20003456", 0.4, 6, 7));             
        grupo.add(new Estudiante("Carla Di", "103789762", 2.4, 1, 15));             
        grupo.add(new Estudiante("Luz Di", "32675123", 2.0, 5, 12));
        Object[] reporte = Solucion.reportes(grupo);
        System.out.println(Arrays.toString(reporte));
    }

}
