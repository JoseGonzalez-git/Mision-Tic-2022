public class Preferencial extends Asistente {
    
    private boolean participaSorteo; 

    public Preferencial(String idTiquete,String nombreCompleto, String direccionResidencia) {
        super(idTiquete,nombreCompleto, direccionResidencia);
        this.participaSorteo = false;
    }

    public boolean isParticipaSorteo() {
        return participaSorteo;
    }
    
    public void setParticipaSorteo(boolean participaSorteo) {
        this.participaSorteo = participaSorteo;
    }

    public void participarSorteo(){
        if(!isParticipaSorteo()){
            setParticipaSorteo(true);
        }else if(isParticipaSorteo()){
            setParticipaSorteo(false);
        }
    }
}
