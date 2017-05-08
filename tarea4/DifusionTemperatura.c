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

void genData(char coso[]);

void transInfo();

float darPromedio();

int main(int argc, char const *argv[]) {
  // printf("Iniciando la solucion de la placa...\n" );

  init();
  // // printf("terminoInit\n" );
  // periodicasCte();
  //
  // imprimir();
  // printf("Solucion finalizada.\n");
  fijasCte();
  init();
  fijasNOCte();
  init();
  periodicasCte();
  init();
  periodicasNOCte();
  init();
  abirtasCte();
  init();
  abirtasNOCte();
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
  FILE *arch;
  arch = fopen("promFijasCte.dat", "w");
  float t = 0;
  int imprimio100 = 0;
  genData("fijasCte0.dat");
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
    fprintf(arch,"%f\n",darPromedio() );
    if(t>100 && imprimio100 ==0){
      imprimio100 =1;
      genData("fijasCte100.dat");
    }
  }
  genData("fijasCte2500.dat");
  fclose(arch);
}
void fijasNOCte(){
  // printf("entro\n");
  FILE *arch;
  arch = fopen("promFijasNOCte.dat", "w");
  float t = 0;
  int imprimio100 = 0;
  genData("fijasNOCte0.dat");
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
    fprintf(arch,"%f\n",darPromedio() );
    if(t>100 && imprimio100 ==0){
      imprimio100 =1;
      genData("fijasNOCte100.dat");
    }
    // printf("%f\n", t);
  }
  genData("fijasNOCte2500.dat");
  fclose(arch);

}
void periodicasCte(){
  FILE *arch;
  arch = fopen("promPeriodicasCte.dat", "w");
  float t = 0;
  int imprimio100 = 0;
  genData("periodicasCte0.dat");
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
    fprintf(arch,"%f\n",darPromedio() );
    if(t>100 && imprimio100 ==0){
      imprimio100 =1;
      genData("periodicasCte100.dat");
    }
    // printf("%f\n", t);
  }
  genData("periodicasCte2500.dat");
  fclose(arch);
}
void periodicasNOCte(){
  FILE *arch;
  arch = fopen("promPeriodicasNOCte.dat", "w");
  float t = 0;
  int imprimio100 =0;
  genData("periodicasNOCte0.dat");
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
    fprintf(arch,"%f\n",darPromedio() );
    if(t>100 && imprimio100 ==0){
      imprimio100 =1;
      genData("periodicasNOCte100.dat");
    }

    // printf("%f\n", t);
  }
  genData("periodicasNOCte2500.dat");
  fclose(arch);
}

void abirtasNOCte(){
  FILE *arch;
  arch = fopen("promAbiertasNOCte.dat", "w");
  float t = 0;
  int imprimio100 =0;
  genData("abiertasNOCte0.dat");
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
    fprintf(arch,"%f\n",darPromedio() );
    // printf("%f\n", t);
    if(t>100 && imprimio100 ==0){
      imprimio100 =1;
      genData("abiertasNOCte100.dat");
    }
  }
    genData("abiertasNOCte2500.dat");
    fclose(arch);
}
void abirtasCte(){
  FILE *arch;
  arch = fopen("promAbiertasCte.dat", "w");
  float t = 0;
  int imprimio100 =0;
  genData("abiertasCte0.dat");
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
    fprintf(arch,"%f\n",darPromedio() );
    // printf("%f\n", t);
    if(t>100 && imprimio100 ==0){
      imprimio100 =1;
      genData("abiertasCte100.dat");
    }
  }
  genData("abiertasCte2500.dat");
  fclose(arch);
}


void transInfo(){
  int i =0;
  for(;i<100*100;i++){
    placa[i] = placanew[i];
  }
}
void genData(char coso[]){
  FILE *fp;

   fp = fopen(coso, "w");
  //  fprintf(fp, "This is testing for fprintf...\n");
   int i = 0 ;
   for(; i<100*100 ; i++){
     if((i+1)%100==0){
         fprintf(fp,"%f\n",placa[i] );
     }
     else
     fprintf(fp,"%f,",placa[i] );

   }
   fclose(fp);
}
float darPromedio(){
  int i =0;
  float promedio = 0;
  for(;i<100*100;i++){
    promedio += placa[i];
  }
  promedio /= (100*100);
  return promedio;
}
