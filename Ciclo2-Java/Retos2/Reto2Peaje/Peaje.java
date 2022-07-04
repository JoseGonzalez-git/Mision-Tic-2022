package Reto2Peaje;

public class Peaje {

    private String[] filaCoches;
    private String[] cochesFlyPass;
    private boolean estadoPeaje;
    private int cantidadCochesAnadidos;
    private int cocheEnAtencion;


    public Peaje(String[] filaCoches) {
        this.filaCoches = filaCoches;
        this.cochesFlyPass = new String[filaCoches.length];
        this.estadoPeaje = true;
        this.cantidadCochesAnadidos = 1;
        this.cocheEnAtencion = 0;
    }
    
    public void proximoCoche(){
        if(cantidadCochesAnadidos > 0){
            cocheEnAtencion++;
            if(cocheEnAtencion == cantidadCochesAnadidos){
                cocheEnAtencion = 0;
            }
        }
    }
    
    
    public void agregarCocheFlyPass(){
        String cocheABuscar = filaCoches[cocheEnAtencion];
        for(String coche:cochesFlyPass){
            if(coche.equals(cocheABuscar)){
                break;
            }
            if(" ".equals(coche)){
                coche = cocheABuscar;
            }
        }
    }
    
    public void cambiarEstadoPeaje(){
        estadoPeaje = !estadoPeaje;
    }
    
    public String[] getFilaCoches() {
        return filaCoches;
    }

    public void setFilaCoches(String[] filaCoches) {
        this.filaCoches = filaCoches;
    }

    public String[] getCochesFlyPass() {
        return cochesFlyPass;
    }

    public void setCochesFlyPass(String[] cochesFlyPass) {
        this.cochesFlyPass = cochesFlyPass;
    }

    public boolean isEstadoPeaje() {
        return estadoPeaje;
    }

    public void setEstadoPeaje(boolean estadoPeaje) {
        this.estadoPeaje = estadoPeaje;
    }

    public int getCantidadCochesAnadidos() {
        return cantidadCochesAnadidos;
    }
}
