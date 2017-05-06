#include "stdlib.h"
#include "stdio.h"
#include <math.h>

float v = 0.1;
float dx = 1;
float dt = 0.49;
float alph = 0.49;
//para compilar, corre el comando al final con -lm
//esta va a ser la placa
float *placa;
float *placanew;

//funcion que inicializa la placa
void init();

//esta funcion nos va a imprimir la matriz en consola.
//es solo para la etapa de desarrollo
void imprimir();

void fijasCte();
void fijasNOCte();


void periodicasCte();
void periodicasNOCte();

void abirtasCte();
void abirtasNOCte();



void transInfo();

int main(int argc, char const *argv[]) {
  // printf("Iniciando la solucion de la placa...\n" );

  init();
  // printf("terminoInit\n" );
  periodicasCte();

  imprimir();
  // printf("Solucion finalizada.\n");
  return 0;
}

void init(){
  placa =   malloc(100*100*sizeof(float));
  placanew =   malloc(100*100*sizeof(float));
  int i = 0 ;
  for(; i<100*100 ; i++){
    int x = i%100;
    int y = i/100;
    if(x>=20 && x<= 39 && y>=45 && y<=54){
      placa[i]=100.0;
    }
    else{
      placa[i] = 50.0;
    }
  }
  placanew[i] = 0;
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
void fijasCte(){
  float t = 0;
  while(t<2500){
    int i =0;
    for(; i<100*100 ; i++){
      int x = i%100;
      int y = i/100;

      if(x>0 && x<99&&y>0 && y<99){
        if(x>=20 && x<= 39 && y>=45 && y<=54){
            placanew[y*100+x] = 100;
        }
        else{
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }

      }
      else{
        placanew[y*100+x] = 50;
      }

    }
    transInfo();
    t += dt;
    // printf("%f\n", t);
  }
}
void fijasNOCte(){
  // printf("entro\n");
  float t = 0;
  while(t<2500){
    int i =0;
    for(; i<100*100 ; i++){
      int x = i%100;
      int y = i/100;

      if(x>0 && x<99&&y>0 && y<99){
        placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
      }
      else{
        placanew[y*100+x] = 50;
      }

    }
    transInfo();
    t += dt;
    // printf("%f\n", t);
  }

}
void periodicasCte(){
  float t = 0;
  while(t<2500){
    int i =0;
    for(; i<100*100 ; i++){
      int x = i%100;
      int y = i/100;

      if(x>0 && x<99&&y>0 && y<99){
        if(x>=20 && x<= 39 && y>=45 && y<=54){
            placanew[y*100+x] = 100;
        }
        else{
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
      }
      //la periferia
      else{
        if(x==0 && y ==0){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(99)]+placa[(y+1)*100+(x)] + placa[(99)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(x==0 && y>0 && y< 99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(99)]+placa[(y+1)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(x==0 && y ==99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(99)]+placa[(0)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }//
        else if(y ==0 && x>0 && x<99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(99)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }//
        else if(y ==0 && x ==99){
          placanew[y*100+x] = v*alph*(placa[y*100+(0)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(99)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }//
        else if(y == 99 && x>0 && x<99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x-1)]+placa[(0)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }//
        else if(x ==99&& y>0 && y<99){
          placanew[y*100+x] = v*alph*(placa[y*100+(0)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }//
        else if(x ==99 && y==99){
          placanew[y*100+x] = v*alph*(placa[y*100+(0)]+placa[y*100+(x-1)]+placa[(0)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
      }

    }
    transInfo();
    t += dt;
    // printf("%f\n", t);
  }
}
void periodicasNOCte(){
  float t = 0;
  while(t<2500){
    int i =0;
    for(; i<100*100 ; i++){
      int x = i%100;
      int y = i/100;

      if(x>0 && x<99&&y>0 && y<99){
        placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
      }
      //la periferia
      else{
        if(x==0 && y ==0){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(99)]+placa[(y+1)*100+(x)] + placa[(99)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(x==0 && y>0 && y< 99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(99)]+placa[(y+1)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(x==0 && y ==99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(99)]+placa[(0)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }//
        else if(y ==0 && x>0 && x<99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(99)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }//
        else if(y ==0 && x ==99){
          placanew[y*100+x] = v*alph*(placa[y*100+(0)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(99)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }//
        else if(y == 99 && x>0 && x<99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x-1)]+placa[(0)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }//
        else if(x ==99&& y>0 && y<99){
          placanew[y*100+x] = v*alph*(placa[y*100+(0)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }//
        else if(x ==99 && y==99){
          placanew[y*100+x] = v*alph*(placa[y*100+(0)]+placa[y*100+(x-1)]+placa[(0)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
      }

    }
    transInfo();
    t += dt;
    // printf("%f\n", t);
  }
}

void abirtasNOCte(){
  float t = 0;
  while(t<2500){
    int i =0;
    for(; i<100*100 ; i++){
      int x = i%100;
      int y = i/100;

      if(x>0 && x<99&&y>0 && y<99){
        placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
      }
      //la periferia
      else{
        if(x==0 && y ==0){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x)]+placa[(y+1)*100+(x)] + placa[(y)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(x==0 && y>0 && y< 99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x)]+placa[(y+1)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(x==0 && y ==99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x)]+placa[(y)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(y ==0 && x>0 && x<99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(y)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(y ==0 && x ==99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(y)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(y == 99 && x>0 && x<99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x-1)]+placa[(y)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(x ==99&& y>0 && y<99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(x ==99 && y==99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x)]+placa[y*100+(x-1)]+placa[(y)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
      }

    }
    transInfo();
    t += dt;
    // printf("%f\n", t);
  }
}
void abirtasCte(){
  float t = 0;
  while(t<2500){
    int i =0;
    for(; i<100*100 ; i++){
      int x = i%100;
      int y = i/100;

      if(x>0 && x<99&&y>0 && y<99){
        if(x>=20 && x<= 39 && y>=45 && y<=54){
            placanew[y*100+x] = 100;
        }
        else{
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }

      }
      //la periferia
      else{
        if(x==0 && y ==0){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x)]+placa[(y+1)*100+(x)] + placa[(y)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(x==0 && y>0 && y< 99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x)]+placa[(y+1)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(x==0 && y ==99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x)]+placa[(y)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(y ==0 && x>0 && x<99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(y)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(y ==0 && x ==99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(y)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(y == 99 && x>0 && x<99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x+1)]+placa[y*100+(x-1)]+placa[(y)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(x ==99&& y>0 && y<99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x)]+placa[y*100+(x-1)]+placa[(y+1)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
        else if(x ==99 && y==99){
          placanew[y*100+x] = v*alph*(placa[y*100+(x)]+placa[y*100+(x-1)]+placa[(y)*100+(x)] + placa[(y-1)*100+(x)]) + (1-4*alph*v)*placa[y*100+(x)];
        }
      }

    }
    transInfo();
    t += dt;
    // printf("%f\n", t);
  }
}


void transInfo(){
  int i =0;
  for(;i<100*100;i++){
    placa[i] = placanew[i];
  }
}
