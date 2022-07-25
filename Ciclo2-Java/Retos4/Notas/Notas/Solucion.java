package Notas;

import java.util.ArrayList;

public class Solucion {
    // ESTA CLASE NO TIENE MAIN

    public static Object[] reportes(ArrayList<Estudiante> grupo) {
        // EN ESTE ESPACIO PONER SU LÓGICA
        int tamano = grupo.size();
        double promedio = 0;

        for (int i = 0; i < tamano; i++) {
            promedio += grupo.get(i).getNota();
        }

        promedio = promedio / tamano;

        //Sort arrayList por nota
        for (int i = 0; i < tamano; i++) {
            for (int j = 0; j < tamano - 1; j++) {
                if (grupo.get(j).getNota() > grupo.get(j + 1).getNota()) {
                    Estudiante aux = grupo.get(j);
                    grupo.set(j, grupo.get(j + 1));
                    grupo.set(j + 1, aux);
                }
            }
        }
        //nota mas alta
        double  notaMayor = grupo.get(tamano - 1).getNota();
        //nota mas baja
        double notaMenor = grupo.get(0).getNota();

        // estudiante con nota menor
        String estudianteMenor = "";
        for (int i = 0; i < tamano; i++) {
            if (grupo.get(i).getNota() == notaMenor) {
                estudianteMenor = grupo.get(i).getNombreCompleto();
            }
        }
        // estudiante con nota mayor
        String estudianteMayor = "";
        for (int i = 0; i < tamano; i++) {
            if (grupo.get(i).getNota() == notaMayor) {
                estudianteMayor = grupo.get(i).getNombreCompleto();
            }
        }

        // reporte
        Object[] reporte = new Object[5];
        reporte[0] = promedio;
        reporte[1] = estudianteMenor;
        reporte[2] = notaMenor;
        reporte[3] = estudianteMayor;
        reporte[4] = notaMayor;

        return reporte;
    }
}