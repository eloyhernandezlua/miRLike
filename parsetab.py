
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACOR ALLA AND APAR BOOL CCOR CHAR CLLA COMA CPAR CTEC CTEF CTEI DIF DIV DO DOSPNTS ELSE FALSE FLOAT FOR FUNCTION ID IF IGUAL IGUALIGUAL INT MAIN MAS MAYI MAYQ MENI MENOS MENQ NOT OR POR PROGRAM PTCOMA READ RETURN STR STRING THEN TO TRUE VARS VOID WHILE WRITEprogram : PROGRAM agregarTablaFunciones varss funcs MAIN APAR CPAR ALLA poptomain estatutos CLLAagregarTablaFunciones : ID PTCOMApoptomain : varss : VARS vars\n             | empty\n    vars : tipo DOSPNTS insertVar varsppp varspp vars\n            | empty\n    insertVar : IDvarsppp : initDim CTEI setDim\n               | empty\n    setDim : CCORinitDim : ACORvarspp : PTCOMA\n              | COMA insertVar varsppp varspp\n    funcs : FUNCTION funcsp insertFunc funcspp\n             | empty\n    insertFunc : IDfuncspp : APAR params CPAR updateParamTable PTCOMA varss ALLA addsize estatutos CLLA endfunction funcsupdateParamTable : endfunction : addsize : funcsp : VOID\n              | tipo\n    estatutos : asig estatutop\n                 | return estatutop\n                 | lectura estatutop\n                 | escritura estatutop\n                 | cond estatutop\n                 | while estatutop\n                 | for estatutop\n                 | exp estatutop\n    estatutop : estatutos\n                 | empty\n    tipo : INT\n            | FLOAT\n            | CHAR\n    params : tipo DOSPNTS insertParams ididx paramsp\n              | empty\n    insertParams : ID\n    paramsp : COMA params\n               | empty\n    asig : varAs ididx igualAs asigpp PTCOMAvarAs : IDigualAs : IGUALasigp : exp asigppp\n             | empty\n    asigppp : COMA asigp\n               | empty\n    asigpp : expididx : corArr exp CCOR\n             | empty\n    corArr : ACORreturn : RETURN APAR exp CPAR PTCOMAlectura : READ APAR readId ididx lecturapp CPAR PTCOMAreadId : ID\n    lecturapp : COMA readId ididx lecturapp\n                 | empty\n    escritura : WRITE APAR escriturap escriturapp CPAR PTCOMAescriturap : pushEsc\n                  | exp\n    pushEsc : STRING\n               | CTEC\n    escriturapp : COMA escriturap\n                   | empty\n    cond : IF APAR exp checkCond THEN ALLA estatutos CLLA condppcondpp : checkElse ALLA estatutos CLLA\n              | empty\n    checkElse : ELSE\n    checkCond : CPAR\n    while : saveWhile APAR exp checkWhileCond DO ALLA estatutos CLLAsaveWhile : WHILE\n    checkWhileCond : CPAR\n    for : FOR varFor ididx IGUAL exp initFor exp beforeDo ALLA estatutos CLLAvarFor : ID\n    initFor : TO\n    beforeDo : DO\n    exp : texp exppexpp : OR exp\n            | empty\n    texp : gexp texpptexpp : andCheck texp\n             | empty\n     andCheck : AND\n    gexp : mexp gexppgexpp : addPO mexp\n             | empty\n    addPO : MAYQ\n             | MENQ\n             | MAYI\n             | MENI\n             | IGUAL IGUAL\n             | DIF\n    mexp : termino mexppmexpp : operSR mexp\n            | empty\n    operSR : MENOS\n              | MAS\n    termino : factor terminopterminop : oper termino\n                | empty\n    oper : DIV\n            | POR\n    factor : APAR exp CPAR\n              | ctes\n    factorp : APAR createEra exp valParams factorpp cparParams\n               | ACOR exp CCOR\n               | empty\n    cparParams : CPARcreateEra : valParams : factorpp : COMA exp valParams factorpp\n                | empty\n    ctes : CTEC\n            | CTEI\n            | CTEF\n            | ID validateExistance factorp\n    validateExistance : empty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,84,],[0,-1,]),'ID':([2,15,16,17,19,20,21,22,35,41,43,45,50,52,53,54,55,56,57,58,59,66,67,68,70,71,72,73,74,75,76,77,83,96,98,99,100,101,102,103,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,136,137,138,151,152,153,154,155,156,157,158,159,160,171,177,178,180,182,183,185,193,194,197,198,199,200,201,204,210,214,215,218,219,222,224,226,229,233,234,],[4,-34,-35,-36,25,-22,-23,27,-3,27,68,80,83,68,68,68,68,68,68,68,68,105,-118,-117,-118,-118,-118,-118,-104,-113,-114,-115,-117,83,-52,83,142,83,83,83,-77,83,-79,-118,-80,83,-82,-83,-84,83,-86,-87,-88,-89,-90,-92,-93,83,-95,-96,-97,-98,83,-100,-101,-102,-103,83,-44,-78,-116,-109,83,-107,-81,-85,-91,-94,-99,83,83,83,-21,-42,-53,142,-106,68,-58,68,68,83,-75,-54,83,-118,-70,-105,-108,-65,-67,68,68,-73,-66,]),'VARS':([3,8,133,],[6,-2,6,]),'FUNCTION':([3,5,6,7,8,12,14,39,40,46,135,212,221,],[-118,10,-118,-5,-2,-4,-7,-118,-13,-6,-14,-20,10,]),'MAIN':([3,5,6,7,8,9,11,12,14,29,39,40,46,135,212,221,228,],[-118,-118,-118,-5,-2,18,-16,-4,-7,-15,-118,-13,-6,-14,-20,-118,-18,]),'PTCOMA':([4,26,27,31,33,44,47,48,49,67,70,71,72,73,74,75,76,77,78,81,83,106,108,109,110,112,114,116,123,125,128,130,136,151,152,155,156,157,159,160,165,166,168,187,193,195,218,219,],[8,-118,-8,40,-10,-19,-118,-9,-11,-118,-118,-118,-118,-118,-104,-113,-114,-115,133,40,-117,-77,-79,-118,-80,-82,-84,-86,-93,-95,-98,-100,-103,-78,-116,-107,-81,-85,-94,-99,182,-49,183,197,-106,204,-105,-108,]),'INT':([6,10,30,39,40,135,163,],[15,15,15,15,-13,-14,15,]),'FLOAT':([6,10,30,39,40,135,163,],[16,16,16,16,-13,-14,16,]),'CHAR':([6,10,30,39,40,135,163,],[17,17,17,17,-13,-14,17,]),'ALLA':([6,7,12,14,28,39,40,46,133,135,161,189,190,216,217,223,225,],[-118,-5,-4,-7,35,-118,-13,-6,-118,-14,180,198,199,226,-76,229,-68,]),'VOID':([10,],[20,]),'DOSPNTS':([13,15,16,17,37,],[22,-34,-35,-36,45,]),'APAR':([18,24,25,35,43,50,52,53,54,55,56,57,58,59,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,77,83,96,98,99,101,102,103,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,136,137,138,151,152,153,154,155,156,157,158,159,160,171,177,178,180,182,183,193,194,197,198,199,200,201,204,210,214,215,218,219,222,224,226,229,233,234,],[23,30,-17,-3,50,50,50,50,50,50,50,50,50,50,99,100,101,102,103,-118,-117,-71,-118,-118,-118,-118,-104,-113,-114,-115,-117,50,-52,50,50,50,50,-77,50,-79,153,-80,50,-82,-83,-84,50,-86,-87,-88,-89,-90,-92,-93,50,-95,-96,-97,-98,50,-100,-101,-102,-103,50,-44,-78,-116,-109,50,-107,-81,-85,-91,-94,-99,50,50,50,-21,-42,-53,-106,50,-58,50,50,50,-75,-54,50,-118,-70,-105,-108,-65,-67,50,50,-73,-66,]),'CPAR':([23,30,36,38,67,70,71,72,73,74,75,76,77,79,80,82,83,97,106,108,109,110,112,114,116,123,125,128,130,134,136,140,141,142,143,144,145,146,147,148,149,151,152,155,156,157,159,160,162,163,164,167,169,170,172,181,184,186,188,192,193,196,202,205,209,211,213,218,219,220,227,231,],[28,-118,44,-38,-118,-118,-118,-118,-118,-104,-113,-114,-115,-118,-39,136,-117,-51,-77,-79,-118,-80,-82,-84,-86,-93,-95,-98,-100,-118,-103,168,-118,-55,-118,-59,-60,-61,-62,174,176,-78,-116,-107,-81,-85,-94,-99,-37,-118,-41,-50,-118,187,-64,-40,195,-57,-63,-110,-106,-118,-118,-118,219,-112,-56,-105,-108,-110,-118,-111,]),'ACOR':([26,27,47,60,68,79,80,83,104,105,109,141,142,196,],[34,-8,34,98,-43,98,-39,-117,98,-74,154,98,-55,98,]),'COMA':([26,27,31,33,47,48,49,67,70,71,72,73,74,75,76,77,79,80,81,83,97,106,108,109,110,112,114,116,123,125,128,130,134,136,141,142,143,144,145,146,147,151,152,155,156,157,159,160,167,169,192,193,196,202,205,218,219,220,227,],[-118,-8,41,-10,-118,-9,-11,-118,-118,-118,-118,-118,-104,-113,-114,-115,-118,-39,41,-117,-51,-77,-79,-118,-80,-82,-84,-86,-93,-95,-98,-100,163,-103,-118,-55,171,-59,-60,-61,-62,-78,-116,-107,-81,-85,-94,-99,-50,185,-110,-106,-118,210,185,-105,-108,-110,210,]),'CTEI':([32,34,35,43,50,52,53,54,55,56,57,58,59,67,68,70,71,72,73,74,75,76,77,83,96,98,99,101,102,103,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,136,137,138,151,152,153,154,155,156,157,158,159,160,171,177,178,180,182,183,193,194,197,198,199,200,201,204,210,214,215,218,219,222,224,226,229,233,234,],[42,-12,-3,76,76,76,76,76,76,76,76,76,76,-118,-117,-118,-118,-118,-118,-104,-113,-114,-115,-117,76,-52,76,76,76,76,-77,76,-79,-118,-80,76,-82,-83,-84,76,-86,-87,-88,-89,-90,-92,-93,76,-95,-96,-97,-98,76,-100,-101,-102,-103,76,-44,-78,-116,-109,76,-107,-81,-85,-91,-94,-99,76,76,76,-21,-42,-53,-106,76,-58,76,76,76,-75,-54,76,-118,-70,-105,-108,-65,-67,76,76,-73,-66,]),'RETURN':([35,43,52,53,54,55,56,57,58,59,67,68,70,71,72,73,74,75,76,77,83,106,108,109,110,112,114,116,123,125,128,130,136,151,152,155,156,157,159,160,180,182,183,193,194,197,198,199,204,214,215,218,219,222,224,226,229,233,234,],[-3,61,61,61,61,61,61,61,61,61,-118,-117,-118,-118,-118,-118,-104,-113,-114,-115,-117,-77,-79,-118,-80,-82,-84,-86,-93,-95,-98,-100,-103,-78,-116,-107,-81,-85,-94,-99,-21,-42,-53,-106,61,-58,61,61,-54,-118,-70,-105,-108,-65,-67,61,61,-73,-66,]),'READ':([35,43,52,53,54,55,56,57,58,59,67,68,70,71,72,73,74,75,76,77,83,106,108,109,110,112,114,116,123,125,128,130,136,151,152,155,156,157,159,160,180,182,183,193,194,197,198,199,204,214,215,218,219,222,224,226,229,233,234,],[-3,62,62,62,62,62,62,62,62,62,-118,-117,-118,-118,-118,-118,-104,-113,-114,-115,-117,-77,-79,-118,-80,-82,-84,-86,-93,-95,-98,-100,-103,-78,-116,-107,-81,-85,-94,-99,-21,-42,-53,-106,62,-58,62,62,-54,-118,-70,-105,-108,-65,-67,62,62,-73,-66,]),'WRITE':([35,43,52,53,54,55,56,57,58,59,67,68,70,71,72,73,74,75,76,77,83,106,108,109,110,112,114,116,123,125,128,130,136,151,152,155,156,157,159,160,180,182,183,193,194,197,198,199,204,214,215,218,219,222,224,226,229,233,234,],[-3,63,63,63,63,63,63,63,63,63,-118,-117,-118,-118,-118,-118,-104,-113,-114,-115,-117,-77,-79,-118,-80,-82,-84,-86,-93,-95,-98,-100,-103,-78,-116,-107,-81,-85,-94,-99,-21,-42,-53,-106,63,-58,63,63,-54,-118,-70,-105,-108,-65,-67,63,63,-73,-66,]),'IF':([35,43,52,53,54,55,56,57,58,59,67,68,70,71,72,73,74,75,76,77,83,106,108,109,110,112,114,116,123,125,128,130,136,151,152,155,156,157,159,160,180,182,183,193,194,197,198,199,204,214,215,218,219,222,224,226,229,233,234,],[-3,64,64,64,64,64,64,64,64,64,-118,-117,-118,-118,-118,-118,-104,-113,-114,-115,-117,-77,-79,-118,-80,-82,-84,-86,-93,-95,-98,-100,-103,-78,-116,-107,-81,-85,-94,-99,-21,-42,-53,-106,64,-58,64,64,-54,-118,-70,-105,-108,-65,-67,64,64,-73,-66,]),'FOR':([35,43,52,53,54,55,56,57,58,59,67,68,70,71,72,73,74,75,76,77,83,106,108,109,110,112,114,116,123,125,128,130,136,151,152,155,156,157,159,160,180,182,183,193,194,197,198,199,204,214,215,218,219,222,224,226,229,233,234,],[-3,66,66,66,66,66,66,66,66,66,-118,-117,-118,-118,-118,-118,-104,-113,-114,-115,-117,-77,-79,-118,-80,-82,-84,-86,-93,-95,-98,-100,-103,-78,-116,-107,-81,-85,-94,-99,-21,-42,-53,-106,66,-58,66,66,-54,-118,-70,-105,-108,-65,-67,66,66,-73,-66,]),'WHILE':([35,43,52,53,54,55,56,57,58,59,67,68,70,71,72,73,74,75,76,77,83,106,108,109,110,112,114,116,123,125,128,130,136,151,152,155,156,157,159,160,180,182,183,193,194,197,198,199,204,214,215,218,219,222,224,226,229,233,234,],[-3,69,69,69,69,69,69,69,69,69,-118,-117,-118,-118,-118,-118,-104,-113,-114,-115,-117,-77,-79,-118,-80,-82,-84,-86,-93,-95,-98,-100,-103,-78,-116,-107,-81,-85,-94,-99,-21,-42,-53,-106,69,-58,69,69,-54,-118,-70,-105,-108,-65,-67,69,69,-73,-66,]),'CTEC':([35,43,50,52,53,54,55,56,57,58,59,67,68,70,71,72,73,74,75,76,77,83,96,98,99,101,102,103,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,136,137,138,151,152,153,154,155,156,157,158,159,160,171,177,178,180,182,183,193,194,197,198,199,200,201,204,210,214,215,218,219,222,224,226,229,233,234,],[-3,75,75,75,75,75,75,75,75,75,75,-118,-117,-118,-118,-118,-118,-104,-113,-114,-115,-117,75,-52,75,147,75,75,-77,75,-79,-118,-80,75,-82,-83,-84,75,-86,-87,-88,-89,-90,-92,-93,75,-95,-96,-97,-98,75,-100,-101,-102,-103,75,-44,-78,-116,-109,75,-107,-81,-85,-91,-94,-99,147,75,75,-21,-42,-53,-106,75,-58,75,75,75,-75,-54,75,-118,-70,-105,-108,-65,-67,75,75,-73,-66,]),'CTEF':([35,43,50,52,53,54,55,56,57,58,59,67,68,70,71,72,73,74,75,76,77,83,96,98,99,101,102,103,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,136,137,138,151,152,153,154,155,156,157,158,159,160,171,177,178,180,182,183,193,194,197,198,199,200,201,204,210,214,215,218,219,222,224,226,229,233,234,],[-3,77,77,77,77,77,77,77,77,77,77,-118,-117,-118,-118,-118,-118,-104,-113,-114,-115,-117,77,-52,77,77,77,77,-77,77,-79,-118,-80,77,-82,-83,-84,77,-86,-87,-88,-89,-90,-92,-93,77,-95,-96,-97,-98,77,-100,-101,-102,-103,77,-44,-78,-116,-109,77,-107,-81,-85,-91,-94,-99,77,77,77,-21,-42,-53,-106,77,-58,77,77,77,-75,-54,77,-118,-70,-105,-108,-65,-67,77,77,-73,-66,]),'CCOR':([42,67,70,71,72,73,74,75,76,77,83,106,108,109,110,112,114,116,123,125,128,130,136,139,151,152,155,156,157,159,160,179,193,218,219,],[49,-118,-118,-118,-118,-118,-104,-113,-114,-115,-117,-77,-79,-118,-80,-82,-84,-86,-93,-95,-98,-100,-103,167,-78,-116,-107,-81,-85,-94,-99,193,-106,-105,-108,]),'CLLA':([51,52,53,54,55,56,57,58,59,67,68,70,71,72,73,74,75,76,77,83,85,86,87,88,89,90,91,92,93,94,106,108,109,110,112,114,116,123,125,128,130,136,151,152,155,156,157,159,160,182,183,193,197,203,204,206,207,214,215,218,219,222,224,230,232,233,234,],[84,-118,-118,-118,-118,-118,-118,-118,-118,-118,-117,-118,-118,-118,-118,-104,-113,-114,-115,-117,-24,-32,-33,-25,-26,-27,-28,-29,-30,-31,-77,-79,-118,-80,-82,-84,-86,-93,-95,-98,-100,-103,-78,-116,-107,-81,-85,-94,-99,-42,-53,-106,-58,212,-54,214,215,-118,-70,-105,-108,-65,-67,233,234,-73,-66,]),'IGUAL':([60,68,71,72,73,74,75,76,77,83,95,97,104,105,109,121,123,125,128,130,136,147,150,152,155,159,160,167,193,218,219,],[-118,-43,121,-118,-118,-104,-113,-114,-115,-117,138,-51,-118,-74,-118,158,-93,-95,-98,-100,-103,-113,177,-116,-107,-94,-99,-50,-106,-105,-108,]),'OR':([67,68,70,71,72,73,74,75,76,77,83,109,110,112,114,116,123,125,128,130,136,147,152,155,156,157,159,160,193,218,219,],[107,-117,-118,-118,-118,-118,-104,-113,-114,-115,-117,-118,-80,-82,-84,-86,-93,-95,-98,-100,-103,-113,-116,-107,-81,-85,-94,-99,-106,-105,-108,]),'TO':([67,70,71,72,73,74,75,76,77,83,106,108,109,110,112,114,116,123,125,128,130,136,151,152,155,156,157,159,160,191,193,218,219,],[-118,-118,-118,-118,-118,-104,-113,-114,-115,-117,-77,-79,-118,-80,-82,-84,-86,-93,-95,-98,-100,-103,-78,-116,-107,-81,-85,-94,-99,201,-106,-105,-108,]),'DO':([67,70,71,72,73,74,75,76,77,83,106,108,109,110,112,114,116,123,125,128,130,136,151,152,155,156,157,159,160,175,176,193,208,218,219,],[-118,-118,-118,-118,-118,-104,-113,-114,-115,-117,-77,-79,-118,-80,-82,-84,-86,-93,-95,-98,-100,-103,-78,-116,-107,-81,-85,-94,-99,190,-72,-106,217,-105,-108,]),'DIV':([68,73,74,75,76,77,83,109,136,147,152,155,193,218,219,],[-117,131,-104,-113,-114,-115,-117,-118,-103,-113,-116,-107,-106,-105,-108,]),'POR':([68,73,74,75,76,77,83,109,136,147,152,155,193,218,219,],[-117,132,-104,-113,-114,-115,-117,-118,-103,-113,-116,-107,-106,-105,-108,]),'MENOS':([68,72,73,74,75,76,77,83,109,128,130,136,147,152,155,160,193,218,219,],[-117,126,-118,-104,-113,-114,-115,-117,-118,-98,-100,-103,-113,-116,-107,-99,-106,-105,-108,]),'MAS':([68,72,73,74,75,76,77,83,109,128,130,136,147,152,155,160,193,218,219,],[-117,127,-118,-104,-113,-114,-115,-117,-118,-98,-100,-103,-113,-116,-107,-99,-106,-105,-108,]),'MAYQ':([68,71,72,73,74,75,76,77,83,109,123,125,128,130,136,147,152,155,159,160,193,218,219,],[-117,117,-118,-118,-104,-113,-114,-115,-117,-118,-93,-95,-98,-100,-103,-113,-116,-107,-94,-99,-106,-105,-108,]),'MENQ':([68,71,72,73,74,75,76,77,83,109,123,125,128,130,136,147,152,155,159,160,193,218,219,],[-117,118,-118,-118,-104,-113,-114,-115,-117,-118,-93,-95,-98,-100,-103,-113,-116,-107,-94,-99,-106,-105,-108,]),'MAYI':([68,71,72,73,74,75,76,77,83,109,123,125,128,130,136,147,152,155,159,160,193,218,219,],[-117,119,-118,-118,-104,-113,-114,-115,-117,-118,-93,-95,-98,-100,-103,-113,-116,-107,-94,-99,-106,-105,-108,]),'MENI':([68,71,72,73,74,75,76,77,83,109,123,125,128,130,136,147,152,155,159,160,193,218,219,],[-117,120,-118,-118,-104,-113,-114,-115,-117,-118,-93,-95,-98,-100,-103,-113,-116,-107,-94,-99,-106,-105,-108,]),'DIF':([68,71,72,73,74,75,76,77,83,109,123,125,128,130,136,147,152,155,159,160,193,218,219,],[-117,122,-118,-118,-104,-113,-114,-115,-117,-118,-93,-95,-98,-100,-103,-113,-116,-107,-94,-99,-106,-105,-108,]),'AND':([68,70,71,72,73,74,75,76,77,83,109,114,116,123,125,128,130,136,147,152,155,157,159,160,193,218,219,],[-117,113,-118,-118,-118,-104,-113,-114,-115,-117,-118,-84,-86,-93,-95,-98,-100,-103,-113,-116,-107,-85,-94,-99,-106,-105,-108,]),'STRING':([101,171,],[146,146,]),'THEN':([173,174,],[189,-69,]),'ELSE':([214,],[225,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'agregarTablaFunciones':([2,],[3,]),'varss':([3,133,],[5,161,]),'empty':([3,5,6,26,30,39,47,52,53,54,55,56,57,58,59,60,67,70,71,72,73,79,104,109,133,134,141,143,163,169,196,202,205,214,221,227,],[7,11,14,33,38,14,33,87,87,87,87,87,87,87,87,97,108,112,116,125,130,97,97,155,7,164,97,172,38,186,97,211,186,224,11,211,]),'funcs':([5,221,],[9,228,]),'vars':([6,39,],[12,46,]),'tipo':([6,10,30,39,163,],[13,21,37,13,37,]),'funcsp':([10,],[19,]),'insertFunc':([19,],[24,]),'insertVar':([22,41,],[26,47,]),'funcspp':([24,],[29,]),'varsppp':([26,47,],[31,81,]),'initDim':([26,47,],[32,32,]),'params':([30,163,],[36,181,]),'varspp':([31,81,],[39,135,]),'poptomain':([35,],[43,]),'setDim':([42,],[48,]),'estatutos':([43,52,53,54,55,56,57,58,59,194,198,199,226,229,],[51,86,86,86,86,86,86,86,86,203,206,207,230,232,]),'asig':([43,52,53,54,55,56,57,58,59,194,198,199,226,229,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'return':([43,52,53,54,55,56,57,58,59,194,198,199,226,229,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'lectura':([43,52,53,54,55,56,57,58,59,194,198,199,226,229,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'escritura':([43,52,53,54,55,56,57,58,59,194,198,199,226,229,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'cond':([43,52,53,54,55,56,57,58,59,194,198,199,226,229,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'while':([43,52,53,54,55,56,57,58,59,194,198,199,226,229,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'for':([43,52,53,54,55,56,57,58,59,194,198,199,226,229,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'exp':([43,50,52,53,54,55,56,57,58,59,96,99,101,102,103,107,137,154,171,177,178,194,198,199,200,210,226,229,],[59,82,59,59,59,59,59,59,59,59,139,140,145,148,149,151,166,179,145,191,192,59,59,59,208,220,59,59,]),'varAs':([43,52,53,54,55,56,57,58,59,194,198,199,226,229,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'saveWhile':([43,52,53,54,55,56,57,58,59,194,198,199,226,229,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'texp':([43,50,52,53,54,55,56,57,58,59,96,99,101,102,103,107,111,137,154,171,177,178,194,198,199,200,210,226,229,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,156,67,67,67,67,67,67,67,67,67,67,67,67,]),'gexp':([43,50,52,53,54,55,56,57,58,59,96,99,101,102,103,107,111,137,154,171,177,178,194,198,199,200,210,226,229,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'mexp':([43,50,52,53,54,55,56,57,58,59,96,99,101,102,103,107,111,115,124,137,154,171,177,178,194,198,199,200,210,226,229,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,157,159,71,71,71,71,71,71,71,71,71,71,71,71,]),'termino':([43,50,52,53,54,55,56,57,58,59,96,99,101,102,103,107,111,115,124,129,137,154,171,177,178,194,198,199,200,210,226,229,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,160,72,72,72,72,72,72,72,72,72,72,72,72,]),'factor':([43,50,52,53,54,55,56,57,58,59,96,99,101,102,103,107,111,115,124,129,137,154,171,177,178,194,198,199,200,210,226,229,],[73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,]),'ctes':([43,50,52,53,54,55,56,57,58,59,96,99,101,102,103,107,111,115,124,129,137,154,171,177,178,194,198,199,200,210,226,229,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'updateParamTable':([44,],[78,]),'insertParams':([45,],[79,]),'estatutop':([52,53,54,55,56,57,58,59,],[85,88,89,90,91,92,93,94,]),'ididx':([60,79,104,141,196,],[95,134,150,169,205,]),'corArr':([60,79,104,141,196,],[96,96,96,96,96,]),'varFor':([66,],[104,]),'expp':([67,],[106,]),'validateExistance':([68,83,],[109,109,]),'texpp':([70,],[110,]),'andCheck':([70,],[111,]),'gexpp':([71,],[114,]),'addPO':([71,],[115,]),'mexpp':([72,],[123,]),'operSR':([72,],[124,]),'terminop':([73,],[128,]),'oper':([73,],[129,]),'igualAs':([95,],[137,]),'readId':([100,185,],[141,196,]),'escriturap':([101,171,],[143,188,]),'pushEsc':([101,171,],[144,144,]),'factorp':([109,],[152,]),'paramsp':([134,],[162,]),'asigpp':([137,],[165,]),'escriturapp':([143,],[170,]),'checkCond':([148,],[173,]),'checkWhileCond':([149,],[175,]),'createEra':([153,],[178,]),'lecturapp':([169,205,],[184,213,]),'addsize':([180,],[194,]),'initFor':([191,],[200,]),'valParams':([192,220,],[202,227,]),'factorpp':([202,227,],[209,231,]),'beforeDo':([208,],[216,]),'cparParams':([209,],[218,]),'endfunction':([212,],[221,]),'condpp':([214,],[222,]),'checkElse':([214,],[223,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM agregarTablaFunciones varss funcs MAIN APAR CPAR ALLA poptomain estatutos CLLA','program',11,'p_program','lex.py',653),
  ('agregarTablaFunciones -> ID PTCOMA','agregarTablaFunciones',2,'p_agregarTablaFunciones','lex.py',657),
  ('poptomain -> <empty>','poptomain',0,'p_poptomain','lex.py',670),
  ('varss -> VARS vars','varss',2,'p_varss','lex.py',684),
  ('varss -> empty','varss',1,'p_varss','lex.py',685),
  ('vars -> tipo DOSPNTS insertVar varsppp varspp vars','vars',6,'p_vars','lex.py',690),
  ('vars -> empty','vars',1,'p_vars','lex.py',691),
  ('insertVar -> ID','insertVar',1,'p_insertVar','lex.py',695),
  ('varsppp -> initDim CTEI setDim','varsppp',3,'p_varsppp','lex.py',705),
  ('varsppp -> empty','varsppp',1,'p_varsppp','lex.py',706),
  ('setDim -> CCOR','setDim',1,'p_setDim','lex.py',710),
  ('initDim -> ACOR','initDim',1,'p_initDim','lex.py',720),
  ('varspp -> PTCOMA','varspp',1,'p_varspp','lex.py',736),
  ('varspp -> COMA insertVar varsppp varspp','varspp',4,'p_varspp','lex.py',737),
  ('funcs -> FUNCTION funcsp insertFunc funcspp','funcs',4,'p_funcs','lex.py',744),
  ('funcs -> empty','funcs',1,'p_funcs','lex.py',745),
  ('insertFunc -> ID','insertFunc',1,'p_insertFunc','lex.py',749),
  ('funcspp -> APAR params CPAR updateParamTable PTCOMA varss ALLA addsize estatutos CLLA endfunction funcs','funcspp',12,'p_funcspp','lex.py',762),
  ('updateParamTable -> <empty>','updateParamTable',0,'p_updateParamTable','lex.py',768),
  ('endfunction -> <empty>','endfunction',0,'p_endfunciton','lex.py',775),
  ('addsize -> <empty>','addsize',0,'p_addsize','lex.py',788),
  ('funcsp -> VOID','funcsp',1,'p_funcsp','lex.py',806),
  ('funcsp -> tipo','funcsp',1,'p_funcsp','lex.py',807),
  ('estatutos -> asig estatutop','estatutos',2,'p_estatutos','lex.py',820),
  ('estatutos -> return estatutop','estatutos',2,'p_estatutos','lex.py',821),
  ('estatutos -> lectura estatutop','estatutos',2,'p_estatutos','lex.py',822),
  ('estatutos -> escritura estatutop','estatutos',2,'p_estatutos','lex.py',823),
  ('estatutos -> cond estatutop','estatutos',2,'p_estatutos','lex.py',824),
  ('estatutos -> while estatutop','estatutos',2,'p_estatutos','lex.py',825),
  ('estatutos -> for estatutop','estatutos',2,'p_estatutos','lex.py',826),
  ('estatutos -> exp estatutop','estatutos',2,'p_estatutos','lex.py',827),
  ('estatutop -> estatutos','estatutop',1,'p_estatutop','lex.py',834),
  ('estatutop -> empty','estatutop',1,'p_estatutop','lex.py',835),
  ('tipo -> INT','tipo',1,'p_tipo','lex.py',842),
  ('tipo -> FLOAT','tipo',1,'p_tipo','lex.py',843),
  ('tipo -> CHAR','tipo',1,'p_tipo','lex.py',844),
  ('params -> tipo DOSPNTS insertParams ididx paramsp','params',5,'p_params','lex.py',855),
  ('params -> empty','params',1,'p_params','lex.py',856),
  ('insertParams -> ID','insertParams',1,'p_insertParams','lex.py',860),
  ('paramsp -> COMA params','paramsp',2,'p_paramsp','lex.py',874),
  ('paramsp -> empty','paramsp',1,'p_paramsp','lex.py',875),
  ('asig -> varAs ididx igualAs asigpp PTCOMA','asig',5,'p_asig','lex.py',882),
  ('varAs -> ID','varAs',1,'p_varAs','lex.py',897),
  ('igualAs -> IGUAL','igualAs',1,'p_igualAs','lex.py',906),
  ('asigp -> exp asigppp','asigp',2,'p_asigp','lex.py',922),
  ('asigp -> empty','asigp',1,'p_asigp','lex.py',923),
  ('asigppp -> COMA asigp','asigppp',2,'p_asigppp','lex.py',931),
  ('asigppp -> empty','asigppp',1,'p_asigppp','lex.py',932),
  ('asigpp -> exp','asigpp',1,'p_asigpp','lex.py',938),
  ('ididx -> corArr exp CCOR','ididx',3,'p_ididx','lex.py',945),
  ('ididx -> empty','ididx',1,'p_ididx','lex.py',946),
  ('corArr -> ACOR','corArr',1,'p_corArr','lex.py',950),
  ('return -> RETURN APAR exp CPAR PTCOMA','return',5,'p_return','lex.py',991),
  ('lectura -> READ APAR readId ididx lecturapp CPAR PTCOMA','lectura',7,'p_lectura','lex.py',1006),
  ('readId -> ID','readId',1,'p_readId','lex.py',1010),
  ('lecturapp -> COMA readId ididx lecturapp','lecturapp',4,'p_lecturapp','lex.py',1018),
  ('lecturapp -> empty','lecturapp',1,'p_lecturapp','lex.py',1019),
  ('escritura -> WRITE APAR escriturap escriturapp CPAR PTCOMA','escritura',6,'p_escritura','lex.py',1026),
  ('escriturap -> pushEsc','escriturap',1,'p_escriturap','lex.py',1031),
  ('escriturap -> exp','escriturap',1,'p_escriturap','lex.py',1032),
  ('pushEsc -> STRING','pushEsc',1,'p_pushEsc','lex.py',1043),
  ('pushEsc -> CTEC','pushEsc',1,'p_pushEsc','lex.py',1044),
  ('escriturapp -> COMA escriturap','escriturapp',2,'p_escriturapp','lex.py',1052),
  ('escriturapp -> empty','escriturapp',1,'p_escriturapp','lex.py',1053),
  ('cond -> IF APAR exp checkCond THEN ALLA estatutos CLLA condpp','cond',9,'p_cond','lex.py',1059),
  ('condpp -> checkElse ALLA estatutos CLLA','condpp',4,'p_condpp','lex.py',1072),
  ('condpp -> empty','condpp',1,'p_condpp','lex.py',1073),
  ('checkElse -> ELSE','checkElse',1,'p_checkElse','lex.py',1079),
  ('checkCond -> CPAR','checkCond',1,'p_checkCond','lex.py',1095),
  ('while -> saveWhile APAR exp checkWhileCond DO ALLA estatutos CLLA','while',8,'p_while','lex.py',1113),
  ('saveWhile -> WHILE','saveWhile',1,'p_saveWhile','lex.py',1128),
  ('checkWhileCond -> CPAR','checkWhileCond',1,'p_checkWhileCond','lex.py',1135),
  ('for -> FOR varFor ididx IGUAL exp initFor exp beforeDo ALLA estatutos CLLA','for',11,'p_for','lex.py',1156),
  ('varFor -> ID','varFor',1,'p_varFor','lex.py',1182),
  ('initFor -> TO','initFor',1,'p_initFor','lex.py',1197),
  ('beforeDo -> DO','beforeDo',1,'p_beforeDo','lex.py',1213),
  ('exp -> texp expp','exp',2,'p_exp','lex.py',1239),
  ('expp -> OR exp','expp',2,'p_expp','lex.py',1243),
  ('expp -> empty','expp',1,'p_expp','lex.py',1244),
  ('texp -> gexp texpp','texp',2,'p_texp','lex.py',1248),
  ('texpp -> andCheck texp','texpp',2,'p_texpp','lex.py',1252),
  ('texpp -> empty','texpp',1,'p_texpp','lex.py',1253),
  ('andCheck -> AND','andCheck',1,'p_andCheck','lex.py',1256),
  ('gexp -> mexp gexpp','gexp',2,'p_gexp','lex.py',1262),
  ('gexpp -> addPO mexp','gexpp',2,'p_gexpp','lex.py',1285),
  ('gexpp -> empty','gexpp',1,'p_gexpp','lex.py',1286),
  ('addPO -> MAYQ','addPO',1,'p_addPO','lex.py',1289),
  ('addPO -> MENQ','addPO',1,'p_addPO','lex.py',1290),
  ('addPO -> MAYI','addPO',1,'p_addPO','lex.py',1291),
  ('addPO -> MENI','addPO',1,'p_addPO','lex.py',1292),
  ('addPO -> IGUAL IGUAL','addPO',2,'p_addPO','lex.py',1293),
  ('addPO -> DIF','addPO',1,'p_addPO','lex.py',1294),
  ('mexp -> termino mexpp','mexp',2,'p_mexp','lex.py',1300),
  ('mexpp -> operSR mexp','mexpp',2,'p_mexpp','lex.py',1326),
  ('mexpp -> empty','mexpp',1,'p_mexpp','lex.py',1327),
  ('operSR -> MENOS','operSR',1,'p_operSR','lex.py',1332),
  ('operSR -> MAS','operSR',1,'p_operSR','lex.py',1333),
  ('termino -> factor terminop','termino',2,'p_termino','lex.py',1341),
  ('terminop -> oper termino','terminop',2,'p_terminop','lex.py',1365),
  ('terminop -> empty','terminop',1,'p_terminop','lex.py',1366),
  ('oper -> DIV','oper',1,'p_oper','lex.py',1371),
  ('oper -> POR','oper',1,'p_oper','lex.py',1372),
  ('factor -> APAR exp CPAR','factor',3,'p_factor','lex.py',1379),
  ('factor -> ctes','factor',1,'p_factor','lex.py',1380),
  ('factorp -> APAR createEra exp valParams factorpp cparParams','factorp',6,'p_factorp','lex.py',1418),
  ('factorp -> ACOR exp CCOR','factorp',3,'p_factorp','lex.py',1419),
  ('factorp -> empty','factorp',1,'p_factorp','lex.py',1420),
  ('cparParams -> CPAR','cparParams',1,'p_cparParams','lex.py',1424),
  ('createEra -> <empty>','createEra',0,'p_createEra','lex.py',1440),
  ('valParams -> <empty>','valParams',0,'p_valParams','lex.py',1455),
  ('factorpp -> COMA exp valParams factorpp','factorpp',4,'p_factorpp','lex.py',1476),
  ('factorpp -> empty','factorpp',1,'p_factorpp','lex.py',1477),
  ('ctes -> CTEC','ctes',1,'p_ctes','lex.py',1486),
  ('ctes -> CTEI','ctes',1,'p_ctes','lex.py',1487),
  ('ctes -> CTEF','ctes',1,'p_ctes','lex.py',1488),
  ('ctes -> ID validateExistance factorp','ctes',3,'p_ctes','lex.py',1489),
  ('validateExistance -> <empty>','validateExistance',0,'p_validateExistance','lex.py',1498),
  ('empty -> <empty>','empty',0,'p_empty','lex.py',1509),
]
