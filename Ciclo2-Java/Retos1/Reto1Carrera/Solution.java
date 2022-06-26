public class Solution{
    //ESTA CLASE NO TIENE MAIN

    public static int [] reporte(int [] participantes){
        //EN ESTE ESPACIO PONER SU LÓGICA
        int [] resultado = new int [3];
        int totalParticipantes = participantes.length;
        int tiempoMasLargo = 0;
        for (int i = 0; i < totalParticipantes; i++) {
            if (participantes[i] > tiempoMasLargo) {
                tiempoMasLargo = participantes[i];
            }
        }
        int tiempoMasCorto = tiempoMasLargo;
        for (int i = 0; i < totalParticipantes; i++) {
            if (participantes[i] < tiempoMasCorto) {
                tiempoMasCorto = participantes[i];
            }
        }
        resultado[0] = totalParticipantes;
        resultado[1] = tiempoMasCorto;
        resultado[2] = tiempoMasLargo;
        return resultado;
    }
}