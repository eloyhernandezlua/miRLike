Program MyRlike;
VARS
    int: i, j;


main(){
    j = 1;
    for i = 0 to 10 do {
        j = j + (j*i);
        write(j); 
    }
    write("Terminó el ciclo");
}