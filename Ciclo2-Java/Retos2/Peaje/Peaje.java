
public class Peaje {

    private String[] filaCoches;
    private String[] cochesFlyPass;
    private boolean estadoPeaje;
    private int cantidadCochesAtendidos;
    private int cocheEnAtencion;


    public Peaje(String[] filaCoches) {
        this.filaCoches = filaCoches;
        this.cochesFlyPass = new String[filaCoches.length];
        llenarCochesFlyPass(getCochesFlyPass().length);
        this.estadoPeaje = true;
        this.cantidadCochesAtendidos = 1;
        this.cocheEnAtencion = 0;
    }
    
    public void proximoCoche(){
        if(isEstadoPeaje()){
            if(cantidadCochesAtendidos < filaCoches.length){
                cantidadCochesAtendidos++;
                cocheEnAtencion++;
            }else{
                cocheEnAtencion = 0;
                estadoPeaje = false;
            }
        }
    }
    
    public void agregarCocheFlyPass(){
        String cocheABuscar = filaCoches[cocheEnAtencion];
        int posicionCoche = buscarCoche(cocheABuscar);
        if(posicionCoche != -1){
            cochesFlyPass[posicionCoche] = cocheABuscar;
            filaCoches[posicionCoche] = "";
        }
    }
    
    private int buscarCoche(String cocheABuscar) {
        int posicionCoche = -1;
        for(int i = 0; i < filaCoches.length; i++){
            if(filaCoches[i].equals(cocheABuscar)){
                posicionCoche = i;
                break;
            }
        }
        return posicionCoche;
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

    public int getCantidadCochesAtendidos() {
        return cantidadCochesAtendidos;
    }

    public void setCantidadCochesAtendidos(int cantidadCochesAtendidos) {
        this.cantidadCochesAtendidos = cantidadCochesAtendidos;
    }

    public int getCocheEnAtencion() {
        return cocheEnAtencion;
    }

    public void setCocheEnAtencion(int cocheEnAtencion) {
        this.cocheEnAtencion = cocheEnAtencion;
    }

    public void llenarCochesFlyPass(int tam){
        for(int i = 0; i < tam; i++){
            cochesFlyPass[i] = " ";
        }
    }
}
