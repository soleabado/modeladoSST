#!/bin/bash

# Check the input parameters

if [[ $# -eq 0 ]]; then
   echo -e "Program Use:\n"   
   echo -e "\t $0 parameter_file.py \n"
   exit
fi

# Define the variables

SALIDA="`basename $1 .py`.slurm"
OUTFILE="`basename $1 .py`.sout"
ERRFILE="`basename $1 .py`.serr"
NAME="trabajo"
RESULTFILE="$NAME.out"

# Create the Slurm submitting script
echo "#!/bin/bash" >> $SALIDA
echo "#" >> $SALIDA
echo "#SBATCH --partition=slurmnuevo" >> $SALIDA
echo "#SBATCH --job-name=$NAME" >> $SALIDA
echo "#SBATCH --error=$ERRFILE" >> $SALIDA
echo "#SBATCH --output=$OUTFILE" >> $SALIDA
echo "#SBATCH --cpus-per-task=1" >> $SALIDA
echo "#SBATCH --mem-per-cpu=8000" >> $SALIDA
echo "[ ! -d "/tmp/soledad/" ] && mkdir "/tmp/soledad/"" >> $SALIDA
echo "cp $1 /tmp/soledad/" >> $SALIDA
echo "cd /tmp/soledad/" >> $SALIDA
echo "sst $1" >> $SALIDA

sbatch $SALIDA
rm $SALIDA