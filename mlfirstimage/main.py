import fitz  # PyMuPDF kütüphanesinin fitz modülü


def pdf_to_text(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf_document:
        num_pages = pdf_document.page_count
        for page_num in range(num_pages):
            page = pdf_document[page_num]
            text += page.get_text()
    return text


pdf_path = 'veriseti/minmax.pdf'
pdf_text = pdf_to_text(pdf_path)

# Şimdi pdf_text'i işleyerek istediğiniz diziyi oluşturabilirsiniz.
# Burada örnek bir diziye aktarma işlemi yapıyorum, sizin tablonuza göre adapte etmeniz gerekebilir.
table_rows = [row.split('\t') for row in pdf_text.split('\n') if row.strip()]

# Dizi elemanlarını yazdırma
for row in table_rows:
    print(row)
