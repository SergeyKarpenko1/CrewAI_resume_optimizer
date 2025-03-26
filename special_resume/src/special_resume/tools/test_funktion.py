import os
import markdown

import os
os.environ['DYLD_LIBRARY_PATH'] = '/opt/homebrew/lib'

import ctypes.util
print("libgobject path:", ctypes.util.find_library("gobject-2.0"))

from weasyprint import HTML, CSS
import tempfile


def save_pretty_pdf(markdown_path: str, output_path: str):
    # Читаем Markdown
    with open(markdown_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Преобразуем в HTML
    html_body = markdown.markdown(md_text, output_format='html5')

    # Оборачиваем в HTML с компактными стилями
    full_html = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="utf-8">
        <style>
            @page {{
                size: A4;
                margin: 1.5cm;
            }}
            body {{
                font-family: "Georgia", serif;
                font-size: 10pt;
                line-height: 1.2;
                color: #2e2e2e;
                background: white;
                width: 100%;
                margin: 0;
                padding: 0;
            }}
            h1, h2, h3 {{
                color: #1a1a1a;
                margin-top: 0.6em;
                margin-bottom: 0.2em;
            }}
            h1 {{
                font-size: 18pt;
                text-align: center;
                border-bottom: 1px solid #ccc;
                padding-bottom: 0.2em;
            }}
            h2 {{
                font-size: 14pt;
                border-bottom: 1px solid #ddd;
            }}
            h3 {{
                font-size: 12pt;
                font-style: italic;
            }}
            p {{
                margin: 0 0 0.5em 0;
                text-align: justify;
                text-indent: 1em;
            }}
            ul, ol {{
                margin: 0 0 0.5em 1em;
            }}
            strong {{
                color: #000;
            }}
            em {{
                color: #555;
            }}
            code {{
                font-family: "Courier New", monospace;
                background: #f4f4f4;
                padding: 1px 3px;
                border-radius: 4px;
            }}
        </style>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """

    # Генерация PDF
    HTML(string=full_html).write_pdf(output_path)

save_pretty_pdf(
    markdown_path='/Users/sergey/Desktop/CrewAI/Special_resume/Resume_Database/DeepPavlov.ai/tailored_resume.md',
    output_path='/Users/sergey/Desktop/CrewAI/Special_resume/Resume_Database/DeepPavlov.ai/Карпенко Сергей.pdf'
)

# python3 /Users/sergey/Desktop/CrewAI/Special_resume/special_resume/src/special_resume/tools/test_funktion.py