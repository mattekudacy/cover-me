import PyPDF2
pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page()
pdf_writer.write("Hello, World!")
pdf_writer.save("hello.pdf")
