all:
	xelatex meccanica_analitica.tex
	rm meccanica_analitica.aux
	rm meccanica_analitica.log
	xelatex fisica_dei_solidi_e_dei_fluidi.tex
	rm fisica_dei_solidi_e_dei_fluidi.aux
	rm fisica_dei_solidi_e_dei_fluidi.log
	xelatex laboratorio_root.tex
	rm laboratorio_root.aux
	rm laboratorio_root.log
	xelatex onde.tex
	rm onde.aux
	rm onde.log
	clear