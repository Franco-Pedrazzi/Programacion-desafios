#include <iostream>
#include <chrono>
using namespace std;

char mapa [3][3]={{'S','.','.'}
                 ,{'#','#','#'}
                 ,{'.','.','G'}};
int fila=end(mapa)-begin(mapa);
int columna=end(mapa[0])-begin(mapa[0]);
int NroLlamadas=0;
int NroCaminosIncorrectos=0;
bool Retroceder=false;
int NroRetrocesos=0;

auto inicio = std::chrono::high_resolution_clock::now();

bool Find_Path(int x,int y){
    NroLlamadas++;
if (x<0 || y<0 || x==fila || y==columna){
    return false;
} 
if (mapa[x][y]=='G'){
    return true;
}
if (mapa[x][y]=='#' || mapa[x][y]=='+'){
    return false;
}
mapa[x][y]='+';
if (Find_Path(x-1,y) == true){
    return true;

}
if (Find_Path(x,y+1) == true){
        if(Retroceder){
        NroCaminosIncorrectos++;
        Retroceder=false;
    }
    return true;
    
}
if (Find_Path(x+1,y) == true){
        if(Retroceder){
        NroCaminosIncorrectos++;
        Retroceder=false;
    }
    return true;
}
if (Find_Path(x,y-1) == true){
        if(Retroceder){
        NroCaminosIncorrectos++;
        Retroceder=false;
    }
    return true;
}
mapa[x][y]='.';
NroRetrocesos++;
Retroceder=true;
return false;
}

int main(){
     for(int x=0;x<fila;x++){
            for(int y=0;y<columna;y++){
            if(mapa[x][y]=='S'){
            if(Find_Path(x,y)==false){
                cout <<"Error, no se encontro el camino"<< endl;
                return 0 ;
            }
            }
            }
    }
    cout <<"mapa: "<< endl;
    for(int x=0;x<fila;x++){
            for(int y=0;y<columna;y++){
            cout << mapa[x][y];
            }
        cout << endl;
    }
    
    cout <<"nro de llamadas de la funcion: " <<  NroLlamadas << endl;
    cout <<"nro caminos incorrectos: " <<  NroCaminosIncorrectos << endl;
    cout <<"nro de retrocesos : " <<  NroRetrocesos << endl;
    auto final = std::chrono::high_resolution_clock::now();
    auto tiempo = std::chrono::duration_cast<std::chrono::milliseconds>(final - inicio).count();

    cout << tiempo << " milisegundos" << std::endl;
    return 0 ;
}