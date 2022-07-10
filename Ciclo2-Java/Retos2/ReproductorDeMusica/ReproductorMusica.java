public class ReproductorMusica {
    
    //ATRIBUTOS
    
    
    //MÉTODOS
    public ReproductorMusica(String[] canciones) {
        //COMPLETE AQUÍ LA LÓGICA DEL CONSTRUCTOR SEGÚN EL ENUNCIADO
    }
    
    public void proximaCancion(){
        //COMPLETE AQUÍ LA LÓGICA DE ESTE MÉTODO SEGÚN EL ENUNCIADO
    }
    
    public void devolverCancion(){
        //COMPLETE AQUÍ LA LÓGICA DE ESTE MÉTODO SEGÚN EL ENUNCIADO
    }
    
    public void cambiarEstadoReproduccion(){
        //COMPLETE AQUÍ LA LÓGICA DE ESTE MÉTODO SEGÚN EL ENUNCIADO
    }
    
    //NO SE DEBE PREOCUPAR POR DESARROLLAR ESTE MÉTODO. ¡NO ELIMINARLO NI MODIFICARLO!
    public void agregarCancionesFavoritas(){
        for(int i = 0; i < cancionesFavoritas.length; i++)
            /*En caso de que encuentre que cancionReproduciendo está en el banco de cancionesFavoritas
            no seguimos buscando espacio libre para agregarla, y salimos del método*/
            if(cancionesFavoritas[i] == cancionReproduciendo)
                return;
            //Pero si no la encontró, y además encuentra un espacio donde añadirlo, lo hace
            else if(cancionesFavoritas[i] == -1){
                cancionesFavoritas[i] = cancionReproduciendo;
                return;
            }                
    }

    public String[] getCanciones() {
        //COMPLETE AQUÍ EL GETTER CORRESPONDIENTE
    }

    public void setCanciones(String[] canciones) {
        //COMPLETE AQUÍ EL SETTER CORRESPONDIENTE
    }

    public int[] getCancionesFavoritas() {
        //COMPLETE AQUÍ EL GETTER CORRESPONDIENTE
    }

    public void setCancionesFavoritas(int[] cancionesFavoritas) {
        //COMPLETE AQUÍ EL SETTER CORRESPONDIENTE
    }

    public boolean isPausado() {
        //COMPLETE AQUÍ EL GETTER CORRESPONDIENTE
    }

    public void setPausado(boolean pausado) {
        //COMPLETE AQUÍ EL SETTER CORRESPONDIENTE
    }

    public int getCancionReproduciendo() {
        //COMPLETE AQUÍ EL GETTER CORRESPONDIENTE
    }

    public void setCancionReproduciendo(int cancionReproduciendo) {
        //COMPLETE AQUÍ EL SETTER CORRESPONDIENTE
    }
    
}