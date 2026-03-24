from reportlab.pdfgen import canvas
from PIL import Image
import os

def create_interactive_card():
    img_path = 'cartao.png'
    pdf_path = 'cartao_interativo.pdf'
    
    if not os.path.exists(img_path):
        print(f"File {img_path} not found.")
        return
        
    img = Image.open(img_path)
    width, height = img.size
    
    # Create canvas matching image dimensions
    c = canvas.Canvas(pdf_path, pagesize=(width, height))
    
    # Draw image, origin is bottom-left
    c.drawImage(img_path, 0, 0, width, height)
    
    # --- Link Areas ---
    # Horizontally: from roughly 45% to 98% of the width
    w_start = width * 0.45
    w_end = width * 0.98
    
    # Vertically: The 3 lines of text
    # The origin (0,0) is bottom-left, so higher Y means higher up the image.
    h1_y0 = height * 0.33
    h1_y1 = height * 0.40
    
    h2_y0 = height * 0.23
    h2_y1 = height * 0.30
    
    h3_y0 = height * 0.13
    h3_y1 = height * 0.20

    # 1) WhatsApp: Phone -> (91) 98112-4227
    c.linkURL('https://wa.me/5591981124227', (w_start, h1_y0, w_end, h1_y1), thickness=0)
    
    # 2) Email -> lvfernandes_contabilidade@outlook.com
    c.linkURL('mailto:lvfernandes_contabilidade@outlook.com', (w_start, h2_y0, w_end, h2_y1), thickness=0)
    
    # 3) Website -> luinyfernandes.com.br
    c.linkURL('https://luinyfernandes.com.br', (w_start, h3_y0, w_end, h3_y1), thickness=0)
    
    c.save()
    print(f"Created {pdf_path}")

if __name__ == '__main__':
    create_interactive_card()
