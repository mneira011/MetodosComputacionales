#include "stdlib.h"
#include "stdio.h"
#include <math.h>
#include <time.h>
#include <float.h>

FILE *fr;
char line[80];
double myvariable;
int i;
int j;

double x[42];
double y[42];

double minx;
double maxx;
double miny;
double maxy;

double posx;
double posy;
double rad;

int ITERACIONES = 100000;

void printTodo();
void cargarDatos();
void calcular();
double calcularDistancias(double px, double py);
double darRandom();
void calcularBoundaries();
int dentroDeBoundaries(double px, double py);
double calcRadio(double px,double py);
void calcular1();
void genData(char coso[]);

int main(int argc, char const *argv[]) {
  /* code */

  srand ( time ( NULL));

  cargarDatos("Canal_ionico.txt", "rt");
  calcular1();
  genData("Canal_ionico.dat");

  cargarDatos("Canal_ionico1.txt", "rt");
  calcular1();
  genData("Canal_ionico1.dat");


  // printf("%f, %f\n",posx, posy );
  // printf("%f\n",rad );




  return 0;
}


void genData(char coso[]){
  FILE *fp;

   fp = fopen(coso, "w");
  //  fprintf(fp, "This is testing for fprintf...\n");

   fprintf(fp,"%f\n",posx );
   fprintf(fp,"%f\n",posy );
   fprintf(fp,"%f\n",rad );



   fclose(fp);
}

void calcular1(){
  calcular();
  while(rad<0){
    calcular();
  }
}

void calcular(){
  calcularBoundaries();

  posx = (double)rand()/RAND_MAX*(maxx-minx)+minx;
  posy = (double)rand()/RAND_MAX*(maxy-miny)+miny;
  rad = calcRadio(posx,posy);


  int cont;

  double tpx = posx;
  double tpy = posy;

  //calculamos el centro del poro
  for(cont = 0; cont<ITERACIONES ; cont++){

    double ttpx = tpx + darRandom();
    double ttpy = tpy + darRandom();
    double alpha = calcRadio(ttpx,ttpy)/calcRadio(tpx,tpy);

    if(alpha>=1.0&& dentroDeBoundaries(ttpx,ttpy)){
      tpx = ttpx;
      tpy = ttpy;
      //mirar
      if(calcRadio(tpx,tpy)>rad){
        posx = tpx;
        posy = tpy;
        rad = calcRadio(tpx,tpy);
      }
    }
    else if(dentroDeBoundaries(ttpx,ttpy)){
      double beta = (double)rand()/RAND_MAX;
      if(beta<=alpha){
        tpx = ttpx;
        tpy = ttpy;
        //mirar
        if(calcRadio(tpx,tpy)>rad){
          posx = tpx;
          posy = tpy;
          rad = calcRadio(tpx,tpy);
        }
      }
    }
  }

}

double calcRadio(double px,double py){
  double tempRad = DBL_MAX;
  for(i = 0 ; i <42; i++){
    //calculamos el cuadrado de la distancia porque da lo mismo
    //y nos ahorramos tiempo de computo
    double dist= (x[i]-px)*(x[i]-px) + (y[i]-py)*(y[i]-py);
    if(dist<tempRad){
      tempRad = dist;
    }
  }
  //le quitamos el angstrom de la particula
  tempRad = sqrt(tempRad) -1;
  return tempRad;
}

int dentroDeBoundaries(double px, double py){
  int ans =1 ;
  if(px<minx || px>maxx){
    ans = 0;
  }
  if(py<miny || py>maxy){
    ans =0;
  }

  return ans;
}

double calcularDistancias(double px, double py){
  double ans = 0;
  for(i = 0 ; i <42; i++){
    //calculamos el cuadrado de la distancia porque da lo mismo
    //y nos ahorramos tiempo de computo
    ans += (x[i]-px)*(x[i]-px) + (y[i]-py)*(y[i]-py);
  }
}

void calcularBoundaries(){
  minx= + DBL_MAX;
  maxx=-DBL_MAX;
  miny=DBL_MAX;
  maxy=-DBL_MAX;

  for(i = 0 ;i<42;i++){
    double tempx = x[i];
    double tempy = y[i];
    if(tempx>maxx){
      maxx = tempx;
    }
    if(tempx<minx){
      minx=tempx;
    }
    if(tempy>maxy){
      maxy = tempy;
    }
    if(tempy<miny){
      miny = tempy;
    }
  }
}

void cargarDatos(char *ruta){
  fr = fopen (ruta, "rt");

  for(i = 0; i < 42; i++)
  {
    for (j = 0 ; j < 2; j++)
    {
      fscanf(fr,"%lf",&myvariable);

      if(j==0){
        x[i] = myvariable;
      }
      else{
        y[i] = myvariable;
      }
    }

  }
   fclose(fr);
}

double darRandom(){
  //sacado de https://stackoverflow.com/questions/33058848/generate-a-random-double-between-1-and-1
  double rand1 = (double)rand()/RAND_MAX*3.0-1.5;
  return rand1;
}


void printTodo(){
  int e ;
  printf("X:\n" );
  for(e=0;e<42;e++){
    printf("%f,",x[e] );
  }
  printf("\n" );

  printf("Y:\n" );
  for(e=0;e<42;e++){
    printf("%f,",y[e] );
  }
  printf("\n" );
}
