
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACOR ALLA AND APAR BOOL CCOR CHAR CLLA COMA CPAR CTEC CTEF CTEI DIF DIV DO DOSPNTS ELSE FALSE FLOAT FOR FUNCTION ID IF IGUAL IGUALIGUAL INT MAIN MAS MAYI MAYQ MENI MENOS MENQ NOT OR POR PROGRAM PTCOMA READ RETURN STR STRING THEN TO TRUE VARS VOID WHILE WRITEprogram : PROGRAM agregarTablaFunciones varss funcs MAIN APAR CPAR ALLA poptomain estatutos CLLAagregarTablaFunciones : ID PTCOMApoptomain : varss : VARS vars\n             | empty\n    vars : tipo DOSPNTS insertVar varsppp varspp vars\n            | empty\n    insertVar : IDvarsppp : initDim CTEI setDim\n               | empty\n    setDim : CCORinitDim : ACORvarspp : PTCOMA\n              | COMA insertVar varsppp varspp\n    funcs : FUNCTION funcsp insertFunc funcspp\n             | empty\n    insertFunc : IDfuncspp : APAR params CPAR updateParamTable PTCOMA varss ALLA addsize estatutos CLLA endfunction funcsupdateParamTable : endfunction : addsize : funcsp : VOID\n              | tipo\n    estatutos : asig estatutop\n                 | return estatutop\n                 | lectura estatutop\n                 | escritura estatutop\n                 | cond estatutop\n                 | while estatutop\n                 | for estatutop\n                 | exp estatutop\n    estatutop : estatutos\n                 | empty\n    tipo : INT\n            | FLOAT\n            | CHAR\n    params : tipo DOSPNTS insertParams ididx paramsp\n              | empty\n    insertParams : ID\n    paramsp : COMA params\n               | empty\n    asig : varAs ididx igualAs asigpp PTCOMAvarAs : IDigualAs : IGUALasigp : exp asigppp\n             | empty\n    asigppp : COMA asigp\n               | empty\n    asigpp : expididx : corArr exp ver CCOR\n             | empty\n    corArr : ACORver : return : RETURN APAR exp CPAR PTCOMAlectura : READ APAR readId ididx lecturapp CPAR PTCOMAreadId : ID\n    lecturapp : COMA readId ididx lecturapp\n                 | empty\n    escritura : WRITE APAR escriturap escriturapp CPAR PTCOMAescriturap : pushEsc\n                  | exp\n    pushEsc : STRING\n               | CTEC\n    escriturapp : COMA escriturap escriturapp\n                   | empty\n    cond : IF APAR exp checkCond THEN ALLA estatutos CLLA condppcondpp : checkElse ALLA estatutos CLLA\n              | empty\n    checkElse : ELSE\n    checkCond : CPAR\n    while : saveWhile APAR exp checkWhileCond DO ALLA estatutos CLLAsaveWhile : WHILE\n    checkWhileCond : CPAR\n    for : FOR varFor ididx IGUAL exp initFor exp beforeDo ALLA estatutos CLLAvarFor : ID\n    initFor : TO\n    beforeDo : DO\n    exp : texp exppexpp : OR exp\n            | empty\n    texp : gexp texpptexpp : andCheck texp\n             | empty\n     andCheck : AND\n    gexp : mexp gexppgexpp : addPO mexp\n             | empty\n    addPO : MAYQ\n             | MENQ\n             | MAYI\n             | MENI\n             | IGUALIGUAL\n             | DIF\n             | NOT\n    mexp : termino mexppmexpp : operSR mexp\n            | empty\n    operSR : MENOS\n              | MAS\n    termino : factor terminopterminop : oper termino\n                | empty\n    oper : DIV\n            | POR\n    meteFondo : APARsacaFondo : CPARfactor : meteFondo exp sacaFondo\n              | ctes\n    factorp : APAR createEra factorParams cparParams\n               | ididx\n    factorParams : exp valParams factorpp\n                    | empty\n    cparParams : CPARcreateEra : valParams : factorpp : COMA exp valParams factorpp\n                | empty\n    ctes : CTEC\n            | CTEI\n            | CTEF\n            | ID validateExistance factorp\n    validateExistance : empty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,83,],[0,-1,]),'ID':([2,15,16,17,19,20,21,22,35,41,43,45,50,52,53,54,55,56,57,58,59,66,67,68,70,71,72,73,74,75,76,77,78,95,96,97,98,99,100,101,102,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,134,138,139,152,153,154,155,156,157,158,159,160,161,172,178,179,180,182,183,184,186,196,199,201,202,203,204,205,206,209,215,219,220,225,227,229,232,236,237,],[4,-34,-35,-36,25,-22,-23,27,-3,27,68,81,-105,68,68,68,68,68,68,68,68,104,-123,-122,-123,-123,-123,-123,134,-108,-118,-119,-120,134,-51,-52,134,143,134,134,134,-78,134,-80,-123,-81,134,-83,-84,-85,134,-87,-88,-89,-90,-91,-92,-93,-94,-95,134,-97,-98,-99,-100,134,-102,-103,-104,-122,134,-44,-79,-121,-114,-110,-82,-86,-96,-101,-107,-106,134,134,134,-21,-42,-50,-54,143,68,-59,68,68,134,-76,-109,-113,-55,134,-123,-71,-66,-68,68,68,-74,-67,]),'VARS':([3,8,135,],[6,-2,6,]),'FUNCTION':([3,5,6,7,8,12,14,39,40,46,137,217,224,],[-123,10,-123,-5,-2,-4,-7,-123,-13,-6,-14,-20,10,]),'MAIN':([3,5,6,7,8,9,11,12,14,29,39,40,46,137,217,224,231,],[-123,-123,-123,-5,-2,18,-16,-4,-7,-15,-123,-13,-6,-14,-20,-123,-18,]),'PTCOMA':([4,26,27,31,33,44,47,48,49,67,70,71,72,73,75,76,77,78,79,82,96,105,107,108,109,111,113,115,123,125,128,130,134,152,153,155,156,157,158,159,160,161,166,167,169,183,188,197,205,206,],[8,-123,-8,40,-10,-19,-123,-9,-11,-123,-123,-123,-123,-123,-108,-118,-119,-120,135,40,-51,-78,-80,-123,-81,-83,-85,-87,-95,-97,-100,-102,-122,-79,-121,-110,-82,-86,-96,-101,-107,-106,182,-49,184,-50,199,209,-109,-113,]),'INT':([6,10,30,39,40,137,164,],[15,15,15,15,-13,-14,15,]),'FLOAT':([6,10,30,39,40,137,164,],[16,16,16,16,-13,-14,16,]),'CHAR':([6,10,30,39,40,137,164,],[17,17,17,17,-13,-14,17,]),'ALLA':([6,7,12,14,28,39,40,46,135,137,162,190,191,221,222,226,228,],[-123,-5,-4,-7,35,-123,-13,-6,-123,-14,180,201,202,229,-77,232,-69,]),'VOID':([10,],[20,]),'DOSPNTS':([13,15,16,17,37,],[22,-34,-35,-36,45,]),'APAR':([18,24,25,35,43,50,52,53,54,55,56,57,58,59,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,78,95,96,97,98,100,101,102,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,134,138,139,152,153,154,155,156,157,158,159,160,161,172,178,179,180,182,183,184,196,199,201,202,203,204,205,206,209,215,219,220,225,227,229,232,236,237,],[23,30,-17,-3,50,-105,50,50,50,50,50,50,50,50,98,99,100,101,102,-123,-122,-72,-123,-123,-123,-123,50,-108,-118,-119,-120,50,-51,-52,50,50,50,50,-78,50,-80,154,-81,50,-83,-84,-85,50,-87,-88,-89,-90,-91,-92,-93,-94,-95,50,-97,-98,-99,-100,50,-102,-103,-104,-122,50,-44,-79,-121,-114,-110,-82,-86,-96,-101,-107,-106,50,50,50,-21,-42,-50,-54,50,-59,50,50,50,-76,-109,-113,-55,50,-123,-71,-66,-68,50,50,-74,-67,]),'CPAR':([23,30,36,38,67,70,71,72,73,75,76,77,78,80,81,96,105,107,108,109,111,113,115,123,125,128,130,133,134,136,141,142,143,144,145,146,147,148,149,150,152,153,154,155,156,157,158,159,160,161,163,164,165,170,171,173,179,181,183,185,187,189,193,194,195,198,200,205,206,207,210,214,216,218,223,230,234,],[28,-123,44,-38,-123,-123,-123,-123,-123,-108,-118,-119,-120,-123,-39,-51,-78,-80,-123,-81,-83,-85,-87,-95,-97,-100,-102,161,-122,-123,169,-123,-56,-123,-60,-61,-62,-63,175,177,-79,-121,-114,-110,-82,-86,-96,-101,-107,-106,-37,-123,-41,-123,188,-65,-123,-40,-50,197,-58,-123,206,-115,-112,-123,-64,-109,-113,-123,-123,-111,-117,-57,-115,-123,-116,]),'ACOR':([26,27,47,60,68,80,81,103,104,108,134,142,143,198,],[34,-8,34,97,-43,97,-39,97,-75,97,-122,97,-56,97,]),'COMA':([26,27,31,33,47,48,49,67,70,71,72,73,75,76,77,78,80,81,82,96,105,107,108,109,111,113,115,123,125,128,130,134,136,142,143,144,145,146,147,148,152,153,155,156,157,158,159,160,161,170,183,189,194,198,205,206,207,210,223,230,],[-123,-8,41,-10,-123,-9,-11,-123,-123,-123,-123,-123,-108,-118,-119,-120,-123,-39,41,-51,-78,-80,-123,-81,-83,-85,-87,-95,-97,-100,-102,-122,164,-123,-56,172,-60,-61,-62,-63,-79,-121,-110,-82,-86,-96,-101,-107,-106,186,-50,172,-115,-123,-109,-113,215,186,-115,215,]),'CTEI':([32,34,35,43,50,52,53,54,55,56,57,58,59,67,68,70,71,72,73,74,75,76,77,78,95,96,97,98,100,101,102,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,134,138,139,152,153,154,155,156,157,158,159,160,161,172,178,179,180,182,183,184,196,199,201,202,203,204,205,206,209,215,219,220,225,227,229,232,236,237,],[42,-12,-3,77,-105,77,77,77,77,77,77,77,77,-123,-122,-123,-123,-123,-123,77,-108,-118,-119,-120,77,-51,-52,77,77,77,77,-78,77,-80,-123,-81,77,-83,-84,-85,77,-87,-88,-89,-90,-91,-92,-93,-94,-95,77,-97,-98,-99,-100,77,-102,-103,-104,-122,77,-44,-79,-121,-114,-110,-82,-86,-96,-101,-107,-106,77,77,77,-21,-42,-50,-54,77,-59,77,77,77,-76,-109,-113,-55,77,-123,-71,-66,-68,77,77,-74,-67,]),'RETURN':([35,43,52,53,54,55,56,57,58,59,67,68,70,71,72,73,75,76,77,78,96,105,107,108,109,111,113,115,123,125,128,130,134,152,153,155,156,157,158,159,160,161,180,182,183,184,196,199,201,202,205,206,209,219,220,225,227,229,232,236,237,],[-3,61,61,61,61,61,61,61,61,61,-123,-122,-123,-123,-123,-123,-108,-118,-119,-120,-51,-78,-80,-123,-81,-83,-85,-87,-95,-97,-100,-102,-122,-79,-121,-110,-82,-86,-96,-101,-107,-106,-21,-42,-50,-54,61,-59,61,61,-109,-113,-55,-123,-71,-66,-68,61,61,-74,-67,]),'READ':([35,43,52,53,54,55,56,57,58,59,67,68,70,71,72,73,75,76,77,78,96,105,107,108,109,111,113,115,123,125,128,130,134,152,153,155,156,157,158,159,160,161,180,182,183,184,196,199,201,202,205,206,209,219,220,225,227,229,232,236,237,],[-3,62,62,62,62,62,62,62,62,62,-123,-122,-123,-123,-123,-123,-108,-118,-119,-120,-51,-78,-80,-123,-81,-83,-85,-87,-95,-97,-100,-102,-122,-79,-121,-110,-82,-86,-96,-101,-107,-106,-21,-42,-50,-54,62,-59,62,62,-109,-113,-55,-123,-71,-66,-68,62,62,-74,-67,]),'WRITE':([35,43,52,53,54,55,56,57,58,59,67,68,70,71,72,73,75,76,77,78,96,105,107,108,109,111,113,115,123,125,128,130,134,152,153,155,156,157,158,159,160,161,180,182,183,184,196,199,201,202,205,206,209,219,220,225,227,229,232,236,237,],[-3,63,63,63,63,63,63,63,63,63,-123,-122,-123,-123,-123,-123,-108,-118,-119,-120,-51,-78,-80,-123,-81,-83,-85,-87,-95,-97,-100,-102,-122,-79,-121,-110,-82,-86,-96,-101,-107,-106,-21,-42,-50,-54,63,-59,63,63,-109,-113,-55,-123,-71,-66,-68,63,63,-74,-67,]),'IF':([35,43,52,53,54,55,56,57,58,59,67,68,70,71,72,73,75,76,77,78,96,105,107,108,109,111,113,115,123,125,128,130,134,152,153,155,156,157,158,159,160,161,180,182,183,184,196,199,201,202,205,206,209,219,220,225,227,229,232,236,237,],[-3,64,64,64,64,64,64,64,64,64,-123,-122,-123,-123,-123,-123,-108,-118,-119,-120,-51,-78,-80,-123,-81,-83,-85,-87,-95,-97,-100,-102,-122,-79,-121,-110,-82,-86,-96,-101,-107,-106,-21,-42,-50,-54,64,-59,64,64,-109,-113,-55,-123,-71,-66,-68,64,64,-74,-67,]),'FOR':([35,43,52,53,54,55,56,57,58,59,67,68,70,71,72,73,75,76,77,78,96,105,107,108,109,111,113,115,123,125,128,130,134,152,153,155,156,157,158,159,160,161,180,182,183,184,196,199,201,202,205,206,209,219,220,225,227,229,232,236,237,],[-3,66,66,66,66,66,66,66,66,66,-123,-122,-123,-123,-123,-123,-108,-118,-119,-120,-51,-78,-80,-123,-81,-83,-85,-87,-95,-97,-100,-102,-122,-79,-121,-110,-82,-86,-96,-101,-107,-106,-21,-42,-50,-54,66,-59,66,66,-109,-113,-55,-123,-71,-66,-68,66,66,-74,-67,]),'WHILE':([35,43,52,53,54,55,56,57,58,59,67,68,70,71,72,73,75,76,77,78,96,105,107,108,109,111,113,115,123,125,128,130,134,152,153,155,156,157,158,159,160,161,180,182,183,184,196,199,201,202,205,206,209,219,220,225,227,229,232,236,237,],[-3,69,69,69,69,69,69,69,69,69,-123,-122,-123,-123,-123,-123,-108,-118,-119,-120,-51,-78,-80,-123,-81,-83,-85,-87,-95,-97,-100,-102,-122,-79,-121,-110,-82,-86,-96,-101,-107,-106,-21,-42,-50,-54,69,-59,69,69,-109,-113,-55,-123,-71,-66,-68,69,69,-74,-67,]),'CTEC':([35,43,50,52,53,54,55,56,57,58,59,67,68,70,71,72,73,74,75,76,77,78,95,96,97,98,100,101,102,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,134,138,139,152,153,154,155,156,157,158,159,160,161,172,178,179,180,182,183,184,196,199,201,202,203,204,205,206,209,215,219,220,225,227,229,232,236,237,],[-3,76,-105,76,76,76,76,76,76,76,76,-123,-122,-123,-123,-123,-123,76,-108,-118,-119,-120,76,-51,-52,76,148,76,76,-78,76,-80,-123,-81,76,-83,-84,-85,76,-87,-88,-89,-90,-91,-92,-93,-94,-95,76,-97,-98,-99,-100,76,-102,-103,-104,-122,76,-44,-79,-121,-114,-110,-82,-86,-96,-101,-107,-106,148,76,76,-21,-42,-50,-54,76,-59,76,76,76,-76,-109,-113,-55,76,-123,-71,-66,-68,76,76,-74,-67,]),'CTEF':([35,43,50,52,53,54,55,56,57,58,59,67,68,70,71,72,73,74,75,76,77,78,95,96,97,98,100,101,102,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,134,138,139,152,153,154,155,156,157,158,159,160,161,172,178,179,180,182,183,184,196,199,201,202,203,204,205,206,209,215,219,220,225,227,229,232,236,237,],[-3,78,-105,78,78,78,78,78,78,78,78,-123,-122,-123,-123,-123,-123,78,-108,-118,-119,-120,78,-51,-52,78,78,78,78,-78,78,-80,-123,-81,78,-83,-84,-85,78,-87,-88,-89,-90,-91,-92,-93,-94,-95,78,-97,-98,-99,-100,78,-102,-103,-104,-122,78,-44,-79,-121,-114,-110,-82,-86,-96,-101,-107,-106,78,78,78,-21,-42,-50,-54,78,-59,78,78,78,-76,-109,-113,-55,78,-123,-71,-66,-68,78,78,-74,-67,]),'CCOR':([42,67,70,71,72,73,75,76,77,78,96,105,107,108,109,111,113,115,123,125,128,130,134,140,152,153,155,156,157,158,159,160,161,168,183,205,206,],[49,-123,-123,-123,-123,-123,-108,-118,-119,-120,-51,-78,-80,-123,-81,-83,-85,-87,-95,-97,-100,-102,-122,-53,-79,-121,-110,-82,-86,-96,-101,-107,-106,183,-50,-109,-113,]),'CLLA':([51,52,53,54,55,56,57,58,59,67,68,70,71,72,73,75,76,77,78,84,85,86,87,88,89,90,91,92,93,96,105,107,108,109,111,113,115,123,125,128,130,134,152,153,155,156,157,158,159,160,161,182,183,184,199,205,206,208,209,211,212,219,220,225,227,233,235,236,237,],[83,-123,-123,-123,-123,-123,-123,-123,-123,-123,-122,-123,-123,-123,-123,-108,-118,-119,-120,-24,-32,-33,-25,-26,-27,-28,-29,-30,-31,-51,-78,-80,-123,-81,-83,-85,-87,-95,-97,-100,-102,-122,-79,-121,-110,-82,-86,-96,-101,-107,-106,-42,-50,-54,-59,-109,-113,217,-55,219,220,-123,-71,-66,-68,236,237,-74,-67,]),'IGUAL':([60,68,94,96,103,104,151,183,],[-123,-43,139,-51,-123,-75,178,-50,]),'OR':([67,68,70,71,72,73,75,76,77,78,96,108,109,111,113,115,123,125,128,130,134,148,153,155,156,157,158,159,160,161,183,205,206,],[106,-122,-123,-123,-123,-123,-108,-118,-119,-120,-51,-123,-81,-83,-85,-87,-95,-97,-100,-102,-122,-118,-121,-110,-82,-86,-96,-101,-107,-106,-50,-109,-113,]),'TO':([67,70,71,72,73,75,76,77,78,96,105,107,108,109,111,113,115,123,125,128,130,134,152,153,155,156,157,158,159,160,161,183,192,205,206,],[-123,-123,-123,-123,-123,-108,-118,-119,-120,-51,-78,-80,-123,-81,-83,-85,-87,-95,-97,-100,-102,-122,-79,-121,-110,-82,-86,-96,-101,-107,-106,-50,204,-109,-113,]),'DO':([67,70,71,72,73,75,76,77,78,96,105,107,108,109,111,113,115,123,125,128,130,134,152,153,155,156,157,158,159,160,161,176,177,183,205,206,213,],[-123,-123,-123,-123,-123,-108,-118,-119,-120,-51,-78,-80,-123,-81,-83,-85,-87,-95,-97,-100,-102,-122,-79,-121,-110,-82,-86,-96,-101,-107,-106,191,-73,-50,-109,-113,222,]),'DIV':([68,73,75,76,77,78,96,108,134,148,153,155,160,161,183,205,206,],[-122,131,-108,-118,-119,-120,-51,-123,-122,-118,-121,-110,-107,-106,-50,-109,-113,]),'POR':([68,73,75,76,77,78,96,108,134,148,153,155,160,161,183,205,206,],[-122,132,-108,-118,-119,-120,-51,-123,-122,-118,-121,-110,-107,-106,-50,-109,-113,]),'MENOS':([68,72,73,75,76,77,78,96,108,128,130,134,148,153,155,159,160,161,183,205,206,],[-122,126,-123,-108,-118,-119,-120,-51,-123,-100,-102,-122,-118,-121,-110,-101,-107,-106,-50,-109,-113,]),'MAS':([68,72,73,75,76,77,78,96,108,128,130,134,148,153,155,159,160,161,183,205,206,],[-122,127,-123,-108,-118,-119,-120,-51,-123,-100,-102,-122,-118,-121,-110,-101,-107,-106,-50,-109,-113,]),'MAYQ':([68,71,72,73,75,76,77,78,96,108,123,125,128,130,134,148,153,155,158,159,160,161,183,205,206,],[-122,116,-123,-123,-108,-118,-119,-120,-51,-123,-95,-97,-100,-102,-122,-118,-121,-110,-96,-101,-107,-106,-50,-109,-113,]),'MENQ':([68,71,72,73,75,76,77,78,96,108,123,125,128,130,134,148,153,155,158,159,160,161,183,205,206,],[-122,117,-123,-123,-108,-118,-119,-120,-51,-123,-95,-97,-100,-102,-122,-118,-121,-110,-96,-101,-107,-106,-50,-109,-113,]),'MAYI':([68,71,72,73,75,76,77,78,96,108,123,125,128,130,134,148,153,155,158,159,160,161,183,205,206,],[-122,118,-123,-123,-108,-118,-119,-120,-51,-123,-95,-97,-100,-102,-122,-118,-121,-110,-96,-101,-107,-106,-50,-109,-113,]),'MENI':([68,71,72,73,75,76,77,78,96,108,123,125,128,130,134,148,153,155,158,159,160,161,183,205,206,],[-122,119,-123,-123,-108,-118,-119,-120,-51,-123,-95,-97,-100,-102,-122,-118,-121,-110,-96,-101,-107,-106,-50,-109,-113,]),'IGUALIGUAL':([68,71,72,73,75,76,77,78,96,108,123,125,128,130,134,148,153,155,158,159,160,161,183,205,206,],[-122,120,-123,-123,-108,-118,-119,-120,-51,-123,-95,-97,-100,-102,-122,-118,-121,-110,-96,-101,-107,-106,-50,-109,-113,]),'DIF':([68,71,72,73,75,76,77,78,96,108,123,125,128,130,134,148,153,155,158,159,160,161,183,205,206,],[-122,121,-123,-123,-108,-118,-119,-120,-51,-123,-95,-97,-100,-102,-122,-118,-121,-110,-96,-101,-107,-106,-50,-109,-113,]),'NOT':([68,71,72,73,75,76,77,78,96,108,123,125,128,130,134,148,153,155,158,159,160,161,183,205,206,],[-122,122,-123,-123,-108,-118,-119,-120,-51,-123,-95,-97,-100,-102,-122,-118,-121,-110,-96,-101,-107,-106,-50,-109,-113,]),'AND':([68,70,71,72,73,75,76,77,78,96,108,113,115,123,125,128,130,134,148,153,155,157,158,159,160,161,183,205,206,],[-122,112,-123,-123,-123,-108,-118,-119,-120,-51,-123,-85,-87,-95,-97,-100,-102,-122,-118,-121,-110,-86,-96,-101,-107,-106,-50,-109,-113,]),'STRING':([100,172,],[147,147,]),'THEN':([174,175,],[190,-70,]),'ELSE':([219,],[228,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'agregarTablaFunciones':([2,],[3,]),'varss':([3,135,],[5,162,]),'empty':([3,5,6,26,30,39,47,52,53,54,55,56,57,58,59,60,67,70,71,72,73,80,103,108,135,136,142,144,164,170,179,189,198,207,210,219,224,230,],[7,11,14,33,38,14,33,86,86,86,86,86,86,86,86,96,107,111,115,125,130,96,96,96,7,165,96,173,38,187,195,173,96,216,187,227,11,216,]),'funcs':([5,224,],[9,231,]),'vars':([6,39,],[12,46,]),'tipo':([6,10,30,39,164,],[13,21,37,13,37,]),'funcsp':([10,],[19,]),'insertFunc':([19,],[24,]),'insertVar':([22,41,],[26,47,]),'funcspp':([24,],[29,]),'varsppp':([26,47,],[31,82,]),'initDim':([26,47,],[32,32,]),'params':([30,164,],[36,181,]),'varspp':([31,82,],[39,137,]),'poptomain':([35,],[43,]),'setDim':([42,],[48,]),'estatutos':([43,52,53,54,55,56,57,58,59,196,201,202,229,232,],[51,85,85,85,85,85,85,85,85,208,211,212,233,235,]),'asig':([43,52,53,54,55,56,57,58,59,196,201,202,229,232,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'return':([43,52,53,54,55,56,57,58,59,196,201,202,229,232,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'lectura':([43,52,53,54,55,56,57,58,59,196,201,202,229,232,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'escritura':([43,52,53,54,55,56,57,58,59,196,201,202,229,232,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'cond':([43,52,53,54,55,56,57,58,59,196,201,202,229,232,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'while':([43,52,53,54,55,56,57,58,59,196,201,202,229,232,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'for':([43,52,53,54,55,56,57,58,59,196,201,202,229,232,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'exp':([43,52,53,54,55,56,57,58,59,74,95,98,100,101,102,106,138,172,178,179,196,201,202,203,215,229,232,],[59,59,59,59,59,59,59,59,59,133,140,141,146,149,150,152,167,146,192,194,59,59,59,213,223,59,59,]),'varAs':([43,52,53,54,55,56,57,58,59,196,201,202,229,232,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'saveWhile':([43,52,53,54,55,56,57,58,59,196,201,202,229,232,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'texp':([43,52,53,54,55,56,57,58,59,74,95,98,100,101,102,106,110,138,172,178,179,196,201,202,203,215,229,232,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,156,67,67,67,67,67,67,67,67,67,67,67,]),'gexp':([43,52,53,54,55,56,57,58,59,74,95,98,100,101,102,106,110,138,172,178,179,196,201,202,203,215,229,232,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'mexp':([43,52,53,54,55,56,57,58,59,74,95,98,100,101,102,106,110,114,124,138,172,178,179,196,201,202,203,215,229,232,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,157,158,71,71,71,71,71,71,71,71,71,71,71,]),'termino':([43,52,53,54,55,56,57,58,59,74,95,98,100,101,102,106,110,114,124,129,138,172,178,179,196,201,202,203,215,229,232,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,159,72,72,72,72,72,72,72,72,72,72,72,]),'factor':([43,52,53,54,55,56,57,58,59,74,95,98,100,101,102,106,110,114,124,129,138,172,178,179,196,201,202,203,215,229,232,],[73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,]),'meteFondo':([43,52,53,54,55,56,57,58,59,74,95,98,100,101,102,106,110,114,124,129,138,172,178,179,196,201,202,203,215,229,232,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'ctes':([43,52,53,54,55,56,57,58,59,74,95,98,100,101,102,106,110,114,124,129,138,172,178,179,196,201,202,203,215,229,232,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'updateParamTable':([44,],[79,]),'insertParams':([45,],[80,]),'estatutop':([52,53,54,55,56,57,58,59,],[84,87,88,89,90,91,92,93,]),'ididx':([60,80,103,108,142,198,],[94,136,151,155,170,210,]),'corArr':([60,80,103,108,142,198,],[95,95,95,95,95,95,]),'varFor':([66,],[103,]),'expp':([67,],[105,]),'validateExistance':([68,134,],[108,108,]),'texpp':([70,],[109,]),'andCheck':([70,],[110,]),'gexpp':([71,],[113,]),'addPO':([71,],[114,]),'mexpp':([72,],[123,]),'operSR':([72,],[124,]),'terminop':([73,],[128,]),'oper':([73,],[129,]),'igualAs':([94,],[138,]),'readId':([99,186,],[142,198,]),'escriturap':([100,172,],[144,189,]),'pushEsc':([100,172,],[145,145,]),'factorp':([108,],[153,]),'sacaFondo':([133,],[160,]),'paramsp':([136,],[163,]),'asigpp':([138,],[166,]),'ver':([140,],[168,]),'escriturapp':([144,189,],[171,200,]),'checkCond':([149,],[174,]),'checkWhileCond':([150,],[176,]),'createEra':([154,],[179,]),'lecturapp':([170,210,],[185,218,]),'factorParams':([179,],[193,]),'addsize':([180,],[196,]),'initFor':([192,],[203,]),'cparParams':([193,],[205,]),'valParams':([194,223,],[207,230,]),'factorpp':([207,230,],[214,234,]),'beforeDo':([213,],[221,]),'endfunction':([217,],[224,]),'condpp':([219,],[225,]),'checkElse':([219,],[226,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM agregarTablaFunciones varss funcs MAIN APAR CPAR ALLA poptomain estatutos CLLA','program',11,'p_program','lex.py',709),
  ('agregarTablaFunciones -> ID PTCOMA','agregarTablaFunciones',2,'p_agregarTablaFunciones','lex.py',734),
  ('poptomain -> <empty>','poptomain',0,'p_poptomain','lex.py',752),
  ('varss -> VARS vars','varss',2,'p_varss','lex.py',766),
  ('varss -> empty','varss',1,'p_varss','lex.py',767),
  ('vars -> tipo DOSPNTS insertVar varsppp varspp vars','vars',6,'p_vars','lex.py',772),
  ('vars -> empty','vars',1,'p_vars','lex.py',773),
  ('insertVar -> ID','insertVar',1,'p_insertVar','lex.py',777),
  ('varsppp -> initDim CTEI setDim','varsppp',3,'p_varsppp','lex.py',787),
  ('varsppp -> empty','varsppp',1,'p_varsppp','lex.py',788),
  ('setDim -> CCOR','setDim',1,'p_setDim','lex.py',792),
  ('initDim -> ACOR','initDim',1,'p_initDim','lex.py',808),
  ('varspp -> PTCOMA','varspp',1,'p_varspp','lex.py',824),
  ('varspp -> COMA insertVar varsppp varspp','varspp',4,'p_varspp','lex.py',825),
  ('funcs -> FUNCTION funcsp insertFunc funcspp','funcs',4,'p_funcs','lex.py',832),
  ('funcs -> empty','funcs',1,'p_funcs','lex.py',833),
  ('insertFunc -> ID','insertFunc',1,'p_insertFunc','lex.py',837),
  ('funcspp -> APAR params CPAR updateParamTable PTCOMA varss ALLA addsize estatutos CLLA endfunction funcs','funcspp',12,'p_funcspp','lex.py',853),
  ('updateParamTable -> <empty>','updateParamTable',0,'p_updateParamTable','lex.py',859),
  ('endfunction -> <empty>','endfunction',0,'p_endfunciton','lex.py',866),
  ('addsize -> <empty>','addsize',0,'p_addsize','lex.py',880),
  ('funcsp -> VOID','funcsp',1,'p_funcsp','lex.py',912),
  ('funcsp -> tipo','funcsp',1,'p_funcsp','lex.py',913),
  ('estatutos -> asig estatutop','estatutos',2,'p_estatutos','lex.py',926),
  ('estatutos -> return estatutop','estatutos',2,'p_estatutos','lex.py',927),
  ('estatutos -> lectura estatutop','estatutos',2,'p_estatutos','lex.py',928),
  ('estatutos -> escritura estatutop','estatutos',2,'p_estatutos','lex.py',929),
  ('estatutos -> cond estatutop','estatutos',2,'p_estatutos','lex.py',930),
  ('estatutos -> while estatutop','estatutos',2,'p_estatutos','lex.py',931),
  ('estatutos -> for estatutop','estatutos',2,'p_estatutos','lex.py',932),
  ('estatutos -> exp estatutop','estatutos',2,'p_estatutos','lex.py',933),
  ('estatutop -> estatutos','estatutop',1,'p_estatutop','lex.py',940),
  ('estatutop -> empty','estatutop',1,'p_estatutop','lex.py',941),
  ('tipo -> INT','tipo',1,'p_tipo','lex.py',948),
  ('tipo -> FLOAT','tipo',1,'p_tipo','lex.py',949),
  ('tipo -> CHAR','tipo',1,'p_tipo','lex.py',950),
  ('params -> tipo DOSPNTS insertParams ididx paramsp','params',5,'p_params','lex.py',961),
  ('params -> empty','params',1,'p_params','lex.py',962),
  ('insertParams -> ID','insertParams',1,'p_insertParams','lex.py',966),
  ('paramsp -> COMA params','paramsp',2,'p_paramsp','lex.py',980),
  ('paramsp -> empty','paramsp',1,'p_paramsp','lex.py',981),
  ('asig -> varAs ididx igualAs asigpp PTCOMA','asig',5,'p_asig','lex.py',988),
  ('varAs -> ID','varAs',1,'p_varAs','lex.py',1003),
  ('igualAs -> IGUAL','igualAs',1,'p_igualAs','lex.py',1012),
  ('asigp -> exp asigppp','asigp',2,'p_asigp','lex.py',1028),
  ('asigp -> empty','asigp',1,'p_asigp','lex.py',1029),
  ('asigppp -> COMA asigp','asigppp',2,'p_asigppp','lex.py',1037),
  ('asigppp -> empty','asigppp',1,'p_asigppp','lex.py',1038),
  ('asigpp -> exp','asigpp',1,'p_asigpp','lex.py',1044),
  ('ididx -> corArr exp ver CCOR','ididx',4,'p_ididx','lex.py',1051),
  ('ididx -> empty','ididx',1,'p_ididx','lex.py',1052),
  ('corArr -> ACOR','corArr',1,'p_corArr','lex.py',1084),
  ('ver -> <empty>','ver',0,'p_ver','lex.py',1099),
  ('return -> RETURN APAR exp CPAR PTCOMA','return',5,'p_return','lex.py',1141),
  ('lectura -> READ APAR readId ididx lecturapp CPAR PTCOMA','lectura',7,'p_lectura','lex.py',1156),
  ('readId -> ID','readId',1,'p_readId','lex.py',1160),
  ('lecturapp -> COMA readId ididx lecturapp','lecturapp',4,'p_lecturapp','lex.py',1168),
  ('lecturapp -> empty','lecturapp',1,'p_lecturapp','lex.py',1169),
  ('escritura -> WRITE APAR escriturap escriturapp CPAR PTCOMA','escritura',6,'p_escritura','lex.py',1176),
  ('escriturap -> pushEsc','escriturap',1,'p_escriturap','lex.py',1181),
  ('escriturap -> exp','escriturap',1,'p_escriturap','lex.py',1182),
  ('pushEsc -> STRING','pushEsc',1,'p_pushEsc','lex.py',1193),
  ('pushEsc -> CTEC','pushEsc',1,'p_pushEsc','lex.py',1194),
  ('escriturapp -> COMA escriturap escriturapp','escriturapp',3,'p_escriturapp','lex.py',1202),
  ('escriturapp -> empty','escriturapp',1,'p_escriturapp','lex.py',1203),
  ('cond -> IF APAR exp checkCond THEN ALLA estatutos CLLA condpp','cond',9,'p_cond','lex.py',1209),
  ('condpp -> checkElse ALLA estatutos CLLA','condpp',4,'p_condpp','lex.py',1222),
  ('condpp -> empty','condpp',1,'p_condpp','lex.py',1223),
  ('checkElse -> ELSE','checkElse',1,'p_checkElse','lex.py',1229),
  ('checkCond -> CPAR','checkCond',1,'p_checkCond','lex.py',1245),
  ('while -> saveWhile APAR exp checkWhileCond DO ALLA estatutos CLLA','while',8,'p_while','lex.py',1263),
  ('saveWhile -> WHILE','saveWhile',1,'p_saveWhile','lex.py',1278),
  ('checkWhileCond -> CPAR','checkWhileCond',1,'p_checkWhileCond','lex.py',1285),
  ('for -> FOR varFor ididx IGUAL exp initFor exp beforeDo ALLA estatutos CLLA','for',11,'p_for','lex.py',1306),
  ('varFor -> ID','varFor',1,'p_varFor','lex.py',1333),
  ('initFor -> TO','initFor',1,'p_initFor','lex.py',1348),
  ('beforeDo -> DO','beforeDo',1,'p_beforeDo','lex.py',1364),
  ('exp -> texp expp','exp',2,'p_exp','lex.py',1390),
  ('expp -> OR exp','expp',2,'p_expp','lex.py',1394),
  ('expp -> empty','expp',1,'p_expp','lex.py',1395),
  ('texp -> gexp texpp','texp',2,'p_texp','lex.py',1399),
  ('texpp -> andCheck texp','texpp',2,'p_texpp','lex.py',1403),
  ('texpp -> empty','texpp',1,'p_texpp','lex.py',1404),
  ('andCheck -> AND','andCheck',1,'p_andCheck','lex.py',1407),
  ('gexp -> mexp gexpp','gexp',2,'p_gexp','lex.py',1413),
  ('gexpp -> addPO mexp','gexpp',2,'p_gexpp','lex.py',1436),
  ('gexpp -> empty','gexpp',1,'p_gexpp','lex.py',1437),
  ('addPO -> MAYQ','addPO',1,'p_addPO','lex.py',1440),
  ('addPO -> MENQ','addPO',1,'p_addPO','lex.py',1441),
  ('addPO -> MAYI','addPO',1,'p_addPO','lex.py',1442),
  ('addPO -> MENI','addPO',1,'p_addPO','lex.py',1443),
  ('addPO -> IGUALIGUAL','addPO',1,'p_addPO','lex.py',1444),
  ('addPO -> DIF','addPO',1,'p_addPO','lex.py',1445),
  ('addPO -> NOT','addPO',1,'p_addPO','lex.py',1446),
  ('mexp -> termino mexpp','mexp',2,'p_mexp','lex.py',1452),
  ('mexpp -> operSR mexp','mexpp',2,'p_mexpp','lex.py',1478),
  ('mexpp -> empty','mexpp',1,'p_mexpp','lex.py',1479),
  ('operSR -> MENOS','operSR',1,'p_operSR','lex.py',1484),
  ('operSR -> MAS','operSR',1,'p_operSR','lex.py',1485),
  ('termino -> factor terminop','termino',2,'p_termino','lex.py',1493),
  ('terminop -> oper termino','terminop',2,'p_terminop','lex.py',1518),
  ('terminop -> empty','terminop',1,'p_terminop','lex.py',1519),
  ('oper -> DIV','oper',1,'p_oper','lex.py',1524),
  ('oper -> POR','oper',1,'p_oper','lex.py',1525),
  ('meteFondo -> APAR','meteFondo',1,'p_meteFondo','lex.py',1533),
  ('sacaFondo -> CPAR','sacaFondo',1,'p_sacaFondo','lex.py',1539),
  ('factor -> meteFondo exp sacaFondo','factor',3,'p_factor','lex.py',1545),
  ('factor -> ctes','factor',1,'p_factor','lex.py',1546),
  ('factorp -> APAR createEra factorParams cparParams','factorp',4,'p_factorp','lex.py',1586),
  ('factorp -> ididx','factorp',1,'p_factorp','lex.py',1587),
  ('factorParams -> exp valParams factorpp','factorParams',3,'p_factorParams','lex.py',1591),
  ('factorParams -> empty','factorParams',1,'p_factorParams','lex.py',1592),
  ('cparParams -> CPAR','cparParams',1,'p_cparParams','lex.py',1596),
  ('createEra -> <empty>','createEra',0,'p_createEra','lex.py',1618),
  ('valParams -> <empty>','valParams',0,'p_valParams','lex.py',1633),
  ('factorpp -> COMA exp valParams factorpp','factorpp',4,'p_factorpp','lex.py',1666),
  ('factorpp -> empty','factorpp',1,'p_factorpp','lex.py',1667),
  ('ctes -> CTEC','ctes',1,'p_ctes','lex.py',1676),
  ('ctes -> CTEI','ctes',1,'p_ctes','lex.py',1677),
  ('ctes -> CTEF','ctes',1,'p_ctes','lex.py',1678),
  ('ctes -> ID validateExistance factorp','ctes',3,'p_ctes','lex.py',1679),
  ('validateExistance -> <empty>','validateExistance',0,'p_validateExistance','lex.py',1688),
  ('empty -> <empty>','empty',0,'p_empty','lex.py',1700),
]
