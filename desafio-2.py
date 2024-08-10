n,r,c=6,4,6 #aca se definen n(numero de personages),r(numero de filas) y c(numero de columnas)

def sanar(fila,col,vidaInicial, vidaActual,d, mapa): 
#//////////////////////// aca se verifica que los datos cumplan con las caracteristicas  //////////////////////  
 
    if (len(fila)==len(col)==len(vidaActual)==len(vidaInicial)==n)==False:#este if y lo que tiene dentro se encarga de verificar que el n conquerde con la cantidad de datos de los personages(fila,col,vidaInicial, vidaActual), pero si no concuerda y n es menor q la cantidad de datos solamente el if reducira la cantidad de datos que sigan
        if n<len(fila) and n<len(col) and n<len(vidaActual) and n<len(vidaInicial):
            fila=fila[0:n+1]
            col=col[0:n+1]
            vidaActual=vidaActual[0:n+1]
            vidaInicial=vidaInicial[0:n+1]
        else:
            return "el numero de jugadores deve ser igual n (ademas Fila,col,VidaIncial y Vida actual deven tener la mism cantidad de valores)"
        
        
    if r>1000 or r<1 or c>1000 or c<1 or n>1000 or n<1:#este if verifica que si n,r y c esten entre 1 y 1000
        return "n,r,c deven valer entre 1 y 1000" 
    
    if d>1000000 or d<1:#este if verifica que si d este entre 1 y 1000000
        return "d deve valer entre 1 y 1000000" 
    for F in fila:#este for e if verifican que fila este entre 0 y r-1
        if F>r-1 or F<0:
            return "fila deve valer entre 0 y r-1" 
        
    for C in col:#este for e if verifican que col este entre 0 y c-1
        if C>c-1 or C<0:
            return "col deve valer entre 0 y c-1" 
        
    for VA in vidaActual:#este for e if verifican que las vidas iniciales sean mayores o iguales a las actuales y tambien verifica que las vidas este entre 0 y 100
        if VA<0 or vidaInicial[vidaActual.index(VA)]<VA or vidaInicial[vidaActual.index(VA)]>100:
            return "La vida actal deve ser menor o igual a la inicial y deven estar entre el 1 y el 100"
        
    for y in mapa:#estos fors e ifs que r y c concuerden con el tamaño del mapa y que el mapa solo tenga . y x 
        if len(mapa)!=r or len(y)!=c:
            return "el mapa no tiene r filas y c columnas" 
        for x in y:
            if x!="x" and x!="X" and x!=".":
                print(x)
                return "solo se pueden colocar X y . en el mapa"
#////////////////////////////////////////////// 

#////////////////////// aca organizan la informacion de los personages y los ordenan para que se sepa cual nesecita mas vida////////////////////////          
    
    personages=[]
    while len(personages)<len(vidaInicial):#aca organizan la informacion de los personages
        personages.append([])
        personages[len(personages)-1].append(fila[len(personages)-1])
        personages[len(personages)-1].append(col[len(personages)-1])
        personages[len(personages)-1].append(vidaInicial[len(personages)-1])
        personages[len(personages)-1].append(vidaActual[len(personages)-1])
        personages[len(personages)-1].append(vidaInicial[len(personages)-1]-vidaActual[len(personages)-1])
    repeticiones=len(personages)
    nro=0
    while repeticiones!=1:#aca ordenan a los personages para que se sepa cual nesecita mas vida
        if  personages[nro][4]<personages[nro+1][4]:
            aux=personages[nro+1]
            personages[nro+1]=personages[nro]
            personages[nro]=aux
        nro+=1
        if nro==repeticiones-1:
            nro=0
            repeticiones-=1
#//////////////////////////////////////////////   

#///////////////////aca se definen todos los lugares en donde puede terminar Khris siendo todos marcados por una O para que se puedan distinguir///////////////////////////   
    
    inicio=[col[0],fila[0]]#aca se define la cordenada inicial de khris de una forma mas facil de escribir
    casillas=[[inicio]]#aca se crea una lista donde guardare todos los espacios donde se puede estar
    mapa[col[0]][fila[0]]="O"#aca marco con una O la pocicion inicial de Khris

    for p in range(d):
        casillas.append([])
                
        for casilla in casillas[p:len(casillas)-1]:
            for antes in casilla:
                if antes[0]-1>-1:#estos ifs es para ver si es pocible avanzar hacia la izquierda y si se puede lo registra
                    if mapa[antes[0]-1][antes[1]]==".":
                        casillas[-1].append([antes[0]-1,antes[1]])
                        mapa[antes[0]-1][antes[1]]="O"

                if antes[1]-1>-1:#estos ifs es para ver si es pocible avanzar hacia arriba y si se puede lo registra
                    if mapa[antes[0]][antes[1]-1]==".":
                        casillas[-1].append([antes[0],antes[1]-1])
                        mapa[antes[0]][antes[1]-1]="O"

                if antes[0]+1<len(mapa):#estos ifs es para ver si es pocible avanzar hacia la derecha y si se puede lo registra
                    if mapa[antes[0]+1][antes[1]]==".":
                        casillas[-1].append([antes[0]+1,antes[1]])
                        mapa[antes[0]+1][antes[1]]="O"

                if antes[1]+1<len(mapa[0]):#estos ifs es para ver si es pocible avanzar hacia abajo y si se puede lo registra
                    if mapa[antes[0]][antes[1]+1]==".":
                        casillas[-1].append([antes[0],antes[1]+1])
                        mapa[antes[0]][antes[1]+1]="O"
                        
    casillas=sum(casillas, [])#esto simplifica la matrix, por que antes estaba dividida por el numero de movimientos nesesarios para llegar a esa cordenada
    
    for personage in personages:#este for e if hace que todas las pociciones donde alla un personage sean eliminadas de el registro ya que se puede pasar por esas casillas pero no quedarce y verifica si un personage esta en la misma pocicion de obstaculo, si lo esta retorna error
        if [personage[0],personage[1]] in casillas and [personage[0],personage[1]]!=inicio:
            casillas.remove([personage[0],personage[1]])
            mapa[personage[0]][personage[1]]="."
        if mapa[personage[0]][personage[1]]=="X"or mapa[personage[0]][personage[1]]=="x":#este if verifica si un personage esta en la misma pocicion de obstaculo, si lo esta retorna error
            return "error, un personage no puede estar en la pocicion de un obstaculo"
    for x in mapa:#muestra el mapa
        print(x)
#//////////////////////////////////////////////

#//////////////////////////////////////////////

    for personage in personages:#estos fors e ifs se encargan de devolver la cantidad de vida curada 
        for casilla in casillas:
            if abs(casilla[0]-personage[0]) +abs(casilla[1]-personage[1])<=2 and abs(casilla[0]-personage[0]) +abs(casilla[1]-personage[1])>=0:
                if personage[4]>10:
                    return 10#aca devuelbe 10 directamente por que es lo maximo que puede curar
                else:
                    return 10-(10-personage[4])#aca devuelbe cuanto le curo para curar por completo al personage
#/////////////////////////////////////////////

resultado=sanar([0,3,0,2,0,3],[2,3,5,0,4,1],[13,40,40,50,40,6],[10,34,1,48,32,1],4,[[".",".","X","X",".","."],[".",".",".","X","X","X"],[".",".",".","X",".","."],[".",".",".",".",".","."]])

print(resultado)