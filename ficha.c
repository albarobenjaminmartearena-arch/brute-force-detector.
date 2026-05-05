#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char nombre[50];
    char edad_txt[10];
    int edad;
    char carrera[50];

    printf("Ingrese nombre:");
    fgets(nombre, 50, stdin);
    nombre[strcspn(nombre, "\n")] = 0;

    printf("Ingrese edad:");
    fgets(edad_txt, 10, stdin);
    edad = atoi(edad_txt);

    printf("Ingrese carrera:");
    fgets(carrera, 50, stdin);
    carrera[strcspn(carrera, "\n")] = 0;

    printf("\n*** FICHA PERSONAL ***\n");
   printf("Nombre: %s\n", nombre);

printf("Edad: %d\n", edad);

printf("Carrera: %s\n", carrera);

printf("=================================================\n");

    return 0;
}