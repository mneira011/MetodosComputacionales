mkdir Convection
cd Convection
awk '{print $2, $3}' ../DatosRadioSonda.dat > TempHeight.txt
python ../PLOTS_Convection.py 


