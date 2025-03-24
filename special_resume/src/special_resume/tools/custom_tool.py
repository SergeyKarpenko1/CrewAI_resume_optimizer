from crewai.tools import tool
import chardet
import ftfy
import re
import unicodedata

@tool
def clean_text_tool(text: str) -> str:
    """
    Очищает текст вакансии от битой кодировки, спецсимволов и лишних пробелов.
    Используется для корректировки текста перед анализом.
    
    🔹 Определяет кодировку с помощью `chardet`.
    🔹 Пробует исправить битую кодировку (`ftfy`).
    🔹 Убирает ненужные символы и нормализует текст (`unicodedata`).
    
    📌 Вход: текст вакансии (сырой).
    📌 Выход: очищенный текст.
    """
    if not text:
        return "❌ Нет данных"

    # 🏷 Определяем кодировку
    detected_encoding = chardet.detect(text.encode())["encoding"]

    # 📌 Пробуем декодировать
    try:
        text = text.encode("latin1").decode(detected_encoding)
    except Exception:
        text = ftfy.fix_encoding(text)  # Альтернативный способ исправления

    # 🧹 Убираем ненужные символы
    text = unicodedata.normalize("NFKC", text)  # Нормализуем символы
    text = re.sub(r"[^\w\s.,;!?«»—()-]", "", text)  # Удаляем мусорные символы
    text = re.sub(r"\s+", " ", text).strip()  # Убираем лишние пробелы

    return text