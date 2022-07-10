import java.util.Arrays;
import java.util.Random;

public class VIP extends Asistente{
    
    private boolean[] pantallas;
    private String credencialesPrevia;
    
    public VIP(String idTiquete, String nombreCompleto, String direccionResidencia ) {
        super(idTiquete,nombreCompleto, direccionResidencia );
        this.pantallas = new boolean[3];
        Arrays.fill(pantallas, false);
        this.credencialesPrevia = "";
    }

    public boolean[] getPantallas() {
        return pantallas;
    }

    public void setPantallas(boolean[] pantallas) {
        this.pantallas = pantallas;
    }

    public String getCredencialesPrevia() {
        return credencialesPrevia;
    }

    public void setCredencialesPrevia(String credencialesPrevia) {
        this.credencialesPrevia = credencialesPrevia;
    }

    public void generarCredencialesPrevia() {
        if(credencialesPrevia.isEmpty()){
            Random numero = new Random();
            int x = numero.nextInt(100000);
            String credencialPrevia = String.valueOf(x);
            credencialesPrevia = credencialPrevia;
        }
    }

    public void asignarPantalla(int pantalla){
        if(pantalla >= 1 && pantalla <= 3){
            if(pantallas[pantalla-1]){
                pantallas[pantalla-1] = false;
            }else if(!pantallas[pantalla-1]){
                pantallas[pantalla-1] = true;
            }
        }
    }

}
