public class TurnoVirtual {
    //ESTA CLASE NO TIENE MAIN
    
    //INSERTE LOS ATRIBUTOS
    
    //INSERTE EL MÉTODO CONSTRUCTOR
    
    //INSERTE LOS GETTERS Y SETTERS
    
    //INSERTE LOS DEMÁS MÉTODOS

    //NO SE DEBE PREOCUPAR POR DESARROLLAR ESTE MÉTODO. ¡NO ELIMINARLO NI MODIFICARLO!
    public void agregarTurnoPerdido() {
        for (int i = 0; i < turnosPerdidos.length; i++) {
            if (" ".equals(turnosPerdidos[i])) {
                turnosPerdidos[i] = turnos[turnoEnAtencion];
                break;
            }
        }
    }  
}
