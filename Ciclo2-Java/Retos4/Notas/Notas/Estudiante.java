package Notas;
public class Estudiante {
    //ATRIBUTOS
    private String nombreCompleto;
    private String documentoIdentidad;
    private double nota;
    private int grado;
    private int edad;

    //CONSTRUCTOR
    public Estudiante(String nombreCompleto, String documentoIdentidad, double nota, int grado, int edad) {
        this.nombreCompleto = nombreCompleto;
        this.documentoIdentidad = documentoIdentidad;
        this.nota = nota;
        this.grado = grado;
        this.edad = edad;
    }
    
    //GETTERS Y SETTERS
    public String getNombreCompleto() {
        return nombreCompleto;
    }

    public void setNombreCompleto(String nombreCompleto) {
        this.nombreCompleto = nombreCompleto;
    }

    public String getDocumentoIdentidad() {
        return documentoIdentidad;
    }

    public void setDocumentoIdentidad(String documentoIdentidad) {
        this.documentoIdentidad = documentoIdentidad;
    }

    public double getNota() {
        return nota;
    }

    public void setNota(double nota) {
        this.nota = nota;
    }    

    public int getGrado() {
        return grado;
    }

    public void setGrado(int grado) {
        this.grado = grado;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }
}
