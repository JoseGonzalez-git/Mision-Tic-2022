import java.io.Console;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Preferencial tiq_pref1 = new Preferencial("0123", "Juan Perez", "CL 01 CR 02 03");
        VIP tiq_vip1 = new VIP("5434", "María López", "CR 29 CL 28-27");
        tiq_pref1.participarSorteo();
        tiq_pref1.generarCredenciales();
        tiq_pref1.setDireccionResidencia("CL 04 CR 05-06");
        tiq_vip1.generarCredenciales();
        tiq_vip1.generarCredencialesPrevia();
        tiq_vip1.asignarPantalla(1);
        tiq_vip1.asignarPantalla(2);
        tiq_vip1.asignarPantalla(3);
        tiq_vip1.asignarPantalla(3);
        System.out.println("ID del tiquete:");
        System.out.println(tiq_pref1.getIdTiquete());
        System.out.println("Nombre del cliente:");
        System.out.println(tiq_pref1.getNombreCompleto());
        System.out.println("Dirección del cliente:");
        System.out.println(tiq_pref1.getDireccionResidencia());
        System.out.println("Credenciales del cliente:");
        System.out.println(tiq_pref1.getCredenciales());
        System.out.println("¿Participa en el sorteo?");
        System.out.println(tiq_pref1.isParticipaSorteo());
        System.out.println("ID del tiquete:");
        System.out.println(tiq_vip1.getIdTiquete());
        System.out.println("Nombre del cliente:");
        System.out.println(tiq_vip1.getNombreCompleto());
        System.out.println("Dirección del cliente:");
        System.out.println(tiq_vip1.getDireccionResidencia());
        System.out.println("Estado de las pantallas del cliente:");
        System.out.println(Arrays.toString(tiq_vip1.getPantallas()));
        System.out.println("Credenciales del cliente:");
        System.out.println(tiq_vip1.getCredenciales());
        System.out.println("Credenciales del cliente para la previa:");
        System.out.println(tiq_vip1.getCredencialesPrevia());
            }
}
