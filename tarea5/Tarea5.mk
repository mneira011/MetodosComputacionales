# OBJS = all
all: ParamOptimos.png Canal_ionico.png
	pdflatex Resultados_hw5.tex


ParamOptimos.png: circuitoRC.py
	python circuitoRC.py

Canal_ionico.png: plots_canal_ionico.py Canal_ionico.dat
	python plots_canal_ionico.py
Canal_ionico.dat: canal.x
	./canal.x

canal.x: canal_ionico.c
	gcc canal_ionico.c -o canal.x -lm

clean:
	rm *.dat
	rm *.png
	rm *.pdf
	rm *.x
	rm *.aux
	rm *.log
