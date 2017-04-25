#include "stdlib.h"
#include "stdio.h"
#include <math.h>
//para compilar, corre el comando al final con -lm
//esta va a ser la placa
float *placa;

//funcion que inicializa la placa
void init();

//esta funcion nos va a imprimir la matriz en consola.
//es solo para la etapa de desarrollo
void imprimir();

int main(int argc, char const *argv[]) {
  printf("Iniciando la solucion de la placa...\n" );

  init();
  imprimir();
  printf("Solucion finalizada.\n");
  return 0;
}

void init(){
  placa =   malloc(100*100*sizeof(float));
  int i = 0 ;
  for(; i<100*100 ; i++){
    int x = i%100;
    int y = i/100;
    if(x>=20 && x<= 29 && y>=40 && y<=59){
      placa[i]=100.0;
    }
    else{
      placa[i] = 50.0;
    }
  }
}
void imprimir(){
  int i = 0 ;
  for(; i<100*100 ; i++){
    if((i+1)%100==0){
        printf("%f\n",placa[i] );
    }
    else
    printf("%f,",placa[i] );

  }
}
