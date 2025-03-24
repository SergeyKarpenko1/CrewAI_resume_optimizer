import os
import time
import fitz  # PyMuPDF для работы с PDF
import yaml
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# ✅ Загрузка переменных окружения
load_dotenv()

# ✅ Импорт инструментов
scrap_web_tool = ScrapeWebsiteTool()
search_tool = SerperDevTool()

from tools.custom_tool import clean_text_tool  # Очистка текста
# from special_resume.tools.custom_tool import clean_text_tool


@CrewBase
class SpecialResume:
    """Crew for resume optimization and interview preparation"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        # self.llm = ChatOpenAI(
        #     model="openrouter/google/gemini-flash-1.5",
        #     openai_api_base="https://openrouter.ai/api/v1",
        #     openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        # )
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",  
            openai_api_key=os.getenv("OPENAI_API_KEY")  # ✅ Используем OpenAI ключ
            )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            verbose=True,
            tools=[search_tool, scrap_web_tool, clean_text_tool],  # ✅ Агент теперь может очищать текст сам!
            llm=self.llm
        )

    @agent
    def profiler(self) -> Agent:
        return Agent(
            config=self.agents_config["profiler"],
            verbose=True,
            llm=self.llm
        )

    @agent
    def resume_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config["resume_strategist"],
            verbose=True,
            llm=self.llm
        )

    @agent
    def interview_preparer(self) -> Agent:
        return Agent(
            config=self.agents_config["interview_preparer"],
            verbose=True,
            llm=self.llm
        )

    @task
    def analyze_job_posting(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_job_posting"]
        )

    @task
    def analyze_resume(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_resume"]
        )

    @task
    def optimize_resume(self) -> Task:
        return Task(
            config=self.tasks_config["optimize_resume"],
            output_file="/Users/sergey/Desktop/CrewAI_resume/special_resume/outputsoutputs/trained_crew/tailored_resume.md"
        )

    @task
    def prepare_technical_questions(self) -> Task:
        return Task(
            config=self.tasks_config["prepare_technical_questions"],
            output_file="/Users/sergey/Desktop/CrewAI_resume/special_resume/outputsoutputs/trained_crew/interview_materials.md"
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )

# ✅ **Функция извлечения текста из PDF**
def extract_text_from_pdf(pdf_path):
    """Извлекает текст из PDF и очищает его."""
    doc = fitz.open(pdf_path)
    text = "\n".join(page.get_text("text") for page in doc)
    return clean_text_tool.run(text)   # ✅ Теперь используем `clean_text_tool`

# ✅ **Функция запуска CrewAI**
def run_application_process(job_posting_url, resume_path="resume.pdf"):
    """Запускает CrewAI, исправляет текст вакансии и резюме перед подачей агентам."""
    
    print("🚀 Скачивание и исправление текста вакансии...")
    scraped_text = scrap_web_tool.run(website_url=job_posting_url)
    job_description = clean_text_tool.run(scraped_text)  # ✅ Используем `clean_text_tool`

    print("🚀 Извлечение и исправление текста резюме...")
    resume_text = extract_text_from_pdf(resume_path)

    print("🔗 Job Posting URL:", job_posting_url)
    print("📄 Cleaned Job Description (first 500 chars):", job_description[:500])
    print("📄 Resume Text (first 500 chars):", resume_text[:500])

    # ✅ **Передаем исправленный текст агентам!**
    result = SpecialResume().crew().kickoff(inputs={
        "job_description": job_description,  # ✅ Передаём уже исправленный текст!
        "resume_text": resume_text
    })

    print("📝 CrewAI завершил обработку. Сохранение результата...")

    time.sleep(2)

    tailored_resume_path = "/Users/sergey/Desktop/CrewAI_resume/special_resume/outputsoutputs/trained_crew/tailored_resume.md"
    if os.path.exists(tailored_resume_path):
        print(f"✅ Оптимизированное резюме сохранено: {tailored_resume_path}")
    else:
        print("⚠️ Итоговое резюме не найдено. Проверьте выполнение CrewAI.")

# ✅ **Запуск**
if __name__ == "__main__":
    run_application_process(
        "https://ods.ai/jobs/366c0d8e-fdb3-4e4b-9fd8-183d855a5962",
        resume_path="/Users/sergey/Desktop/CrewAI_resume/Kарпенко Сергей.pdf"
    )