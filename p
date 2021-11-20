Program playground;
VARS
    int: i;
function int fact (int: j);
VARS int: i;
{ 
    if (j == 1) then {
        return(j);
    } else {
        return(j * fact(j - 1));
    }
}

function void otra();
VARS int: i;
{
    i = 2020;
    write(i);
}
main(){
    if(1 > 0) then {
        otra()
        i = fact(4);
    }
    write(i);
}