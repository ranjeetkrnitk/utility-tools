import pdfkit



def webpage_to_pdf(url, output_path):
    try:
        config = pdfkit.configuration(wkhtmltopdf='/path/to/wkhtmltopdf')
        pdfkit.from_url(url, output_path)
        print("PDF Generated successfully.")
    except Exception as e:
        print(f"Failed to generate PDF: {str(e)}")

if __name__ == "__main__":
    url = ""
    output_path = ""
    webpage_to_pdf(url,output_path)
