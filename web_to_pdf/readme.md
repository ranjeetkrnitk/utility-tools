# https://wkhtmltopdf.org/downloads.html

<!-- To convert a webpage to PDF in Python, you can use the `pdfkit` library along with `wkhtmltopdf` or `weasyprint` as the underlying HTML to PDF conversion engine. Below is an example using `pdfkit` and `wkhtmltopdf`:

First, you need to install `pdfkit` and `wkhtmltopdf`:

```bash
pip install pdfkit
```

Then you need to install `wkhtmltopdf`. You can download it from [here](https://wkhtmltopdf.org/downloads.html) and install it on your system.

Here's a simple Python script to convert a webpage to PDF:

```python
import pdfkit

def webpage_to_pdf(url, output_path):
    try:
        pdfkit.from_url(url, output_path)
        print("PDF generated successfully!")
    except Exception as e:
        print("Failed to generate PDF:", str(e))

if __name__ == "__main__":
    url = "http://example.com"  # URL of the webpage you want to convert
    output_path = "output.pdf"   # Path where the PDF will be saved
    webpage_to_pdf(url, output_path)
```

Replace `"http://example.com"` with the URL of the webpage you want to convert, and `"output.pdf"` with the path where you want to save the generated PDF.

Make sure you have `wkhtmltopdf` installed and its path is properly set. If `wkhtmltopdf` is not in your system PATH, you can specify its path explicitly like this:

```python
config = pdfkit.configuration(wkhtmltopdf='/path/to/wkhtmltopdf')
pdfkit.from_url(url, output_path, configuration=config)
```

This script will generate a PDF file containing the content of the specified webpage. -->