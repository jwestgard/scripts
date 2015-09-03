gs -dPDFA -dNOOUTERSAVE -dUseCIEColor -sProcessColorModel=DeviceRGB \
	-sDEVICE=pdfwrite -o $2 -dPDFACompatibilityPolicy=1 \
	/usr/share/ghostscript/9.10/lib/PDFA_def.ps $1
