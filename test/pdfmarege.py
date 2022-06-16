from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

for pdf in ["sample.pdf","sample1.pdf"]:
	merger.append(pdf)
	

merger.write("output.pdf")
merger.close()