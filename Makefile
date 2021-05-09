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
	xelatex fisica_relativistica.tex
	rm fisica_relativistica.aux
	rm fisica_relativistica.log
	xelatex analisi_1.tex
	rm analisi_1.aux
	rm analisi_1.log
	xelatex analisi_2.tex
	rm analisi_2.aux	
	rm analisi_2.log
	clear