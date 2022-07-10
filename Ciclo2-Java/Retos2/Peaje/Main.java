

public class Main{

    public static void showArray(String[] array){
        for(String element:array){
            System.out.print(element+" ");
        }
        System.out.println();
    }
    public static void showData(Peaje peaje){
        System.out.println("Coches en la fila de espera: ");
        showArray(peaje.getFilaCoches());
        System.out.println("Coches en la fila de espera despues de atender el primer coche: ");
        showArray(peaje.getCochesFlyPass());
        System.out.println("Estado del peaje: " + peaje.isEstadoPeaje());
        System.out.println("Coches en atencion: " + peaje.getCocheEnAtencion());
        System.out.println("Cantidad de coches anadidos: " + peaje.getCantidadCochesAtendidos());
    }
    public static void main(String[] args) {
        // array de placas de coches que van a pasar por el peaje de tamaño 14
        String[] filaCoches = {"A12345", "B12345", "C12345", "D12345", "E12345", "F12345", "G12345", "H12345", "I12345", "J12345", "K12345", "L12345", "M12345", "N12345"};
        Peaje taquillaPeaje = new Peaje(filaCoches);

        showData(taquillaPeaje);

        taquillaPeaje.proximoCoche();
        taquillaPeaje.proximoCoche();
        taquillaPeaje.proximoCoche();
        taquillaPeaje.proximoCoche();

        showData(taquillaPeaje);

        taquillaPeaje.agregarCocheFlyPass();
        taquillaPeaje.proximoCoche();
        taquillaPeaje.agregarCocheFlyPass();
        taquillaPeaje.proximoCoche();
        taquillaPeaje.agregarCocheFlyPass();

        showData(taquillaPeaje);

    }
}