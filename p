Program playground;
VARS
    int: i[3];
    int: j;
main(){
    for j = 0 to 3 do {
        i[j] = j; 
    }

    write(i[0]);
    write(i[1]);
    write(i[2]);

}