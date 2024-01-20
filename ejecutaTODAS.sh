#!/bin/bash

for i in *py;
 do
   if [[ -a `basename $i .py`.out ]];
   then
      echo -n "YA SIMULADO: "      
      #echo "   INASim -p $i -f `basename $i .xml`.out   "
      echo "   sst $i   "
   else
      #echo -n "   INASim -p $i -f `basename $i .xml`.out   "
      echo -n "   sst $i   "
      SALIDA=`basename $i .py`.out
      bash ejecutaSimulacion.sh $i
      echo "... Done"
   fi
done