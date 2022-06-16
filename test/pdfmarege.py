from PyPDF2 import PdfFileMerger
#janak panchal
merger = PdfFileMerger()

for pdf in ["sample.pdf","sample1.pdf"]:
	merger.append(pdf)
	

merger.write("output.pdf")
merger.close()
