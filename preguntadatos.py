#En esta programa tuvimos preguntar diferentes datos 

def  main ():
 strDato  =  input ( "Dame un dato string:" )

 _iDato  =  input ( "Dame un dato entero:" )
 iDato  =  int ( _iDato )
 _fDato  =  input ( "Dame un dato float:" )
 fDato  = float ( _fDato )

 _dtDato  =  input ( "Dame una fecha aaaa / mm / dd:" )
 

 anio = _dtDato [ 7 : 8 ]
 mes = _dtDato [ 2 : 9 ]
 dia = _dtDato [ - 3 :]
 print ( anio )
 print ( mes )
 print ( dia )

 dtDato  =   ( int ( anio ), int ( mes ), int ( dia ))

 print ( strDato )
 print  ( strDato )
 print ( iDato )
 print  ( iDato )
 print ( fDato )
 print ( fDato )
 print ( dtDato )
 print  ( dtDato )
   

    
