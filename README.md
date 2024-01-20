# Modelado y evaluación de redes de interconexión de altas prestaciones con el simulador SST

Para este proyecto se hizo uso del Structural Simulation Toolkit (SST). Por ello, es necesario la instalación de los elementos y núcleo de este para el correcto funcionamiento:

https://github.com/sstsimulator

Una vez instalados, clonar el siguiente repositorio en la carpeta /sst/scratch/src/sst-elements-library-13.0.0/src/sst/elements/ember/mpi/motifs/.

#### Estructura final del Proyecto.

Para cada experimento, necesitaremos modificar los ficheros .h y .cc de los motifs ,incluidos en la carpeta /sst/scratch/src/sst-elements-library-13.0.0/src/sst/elements/ember/mpi/motifs/. Por ello, he añadido en la carpeta correspondiente a cada patrón de tráfico, otra carpeta denominada "Motifs" donde se encuentran estos dos ficheros para los distintos tamaños del sistema. Lo que se debe hacer es copiar el contenido de estos en los propios ficheros contenidos en la carpeta /motifs.

Antes de eso, debemos modificar la ubicación de ejecutarMotif.sh y moverlo a la carpeta:

/sst/scratch/src/sst-elements-library-13.0.0/

#### ¿Cómo funciona?

Una vez realizados los cambios previamente descritos en la estructura debemos:

Después de cualquier modificación que se haga en los Motifs hay que ejecutar el script ejecutarMotif.sh:

```bash
cd /sst/scratch/src/sst-elements-library-13.0.0/
bash ejecutarMotif.sh
```

Posteriormente, para ejecutar las simulaciones, basta con moverse a la carpeta correspondiente (por ejemplo: Halo3D/16K/lineal) y ejecutar el archivo "ejecutaTODAS.sh".

```bash
bash ejecutaTODAS.sh
```


