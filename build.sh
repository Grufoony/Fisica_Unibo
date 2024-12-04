cd source
# for each file ending with .tex, call htlatex filename.tex
for i in *.tex; do htlatex $i; done
cd ..
htlatex index.tex