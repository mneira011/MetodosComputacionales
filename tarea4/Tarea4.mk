# OBJS = all
all: abiertasCte0.png
	pdflatex Resultados_hw4.tex

abiertasCte0.png: abiertasCte0.dat
	python Plots_Temperatura.py

abiertasCte0.dat: plots.x
	./plots.x

plots.x: DifusionTemperatura.c
	gcc DifusionTemperatura.c -o plots.x -lm

clean:
	rm *.dat
	rm *.png
	rm *.pdf
	rm *.x
	rm *.aux
	rm *.log
