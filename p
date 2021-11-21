Program playground;
VARS
    int: i;
    float: e;
function float calcula (float: y);
{
    write(y);
    return(y*y);
}

main(){
    e = calcula(calcula(3.0));
    write(e);
}