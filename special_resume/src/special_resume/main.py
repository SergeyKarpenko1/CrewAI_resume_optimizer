#!/usr/bin/env python
import sys
import warnings

from special_resume.crew import SpecialResume
from special_resume.tools.custom_tool import clean_text_tool

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()

# Проверяем, загружается ли ключ
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

# def run():
#     """
#     Run the crew.
#     """
#     inputs = {
#         'topic': 'AI LLMs'
#     }
#     SpecialResume().crew().kickoff(inputs=inputs)


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "job_description": "https://ods.ai/jobs/366c0d8e-fdb3-4e4b-9fd8-183d855a5962", 
#                   # ✅ Добавь любое описание
#         "resume_text": "/Users/sergey/Desktop/CrewAI_resume/Kарпенко Сергей.pdf"  # ✅ Добавь любое резюме
#     }
#     try:
#         SpecialResume().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         SpecialResume().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """Функция тестирования CrewAI"""

#     inputs = {
#         "job_description": "JuniorMiddle Data Scientist (NLP) — Open Data Science Tracks Competitions Hacks Tasks Events"
#         " Projects Hubs Jobs Privacy policy Service agreement Website agreement Public offer on the transfer of the right"
#         " to use speeches Offer with the author ContactSupport По-русски ODS.AI 2015—2025 JuniorMiddle Data Scientist (NLP)"
#         " ze4b2d6ac0156 Posted RUB 150,000 350,000 month Remote or office Full-time NLP LLM Text-classification "
#         "Text-clustering Add Reaction Brief description of the vacancy В расположении РЦНИ находятся данные по мировым"
#         " публикациям, проектам, патентам. Для обработки этих данных с целью представления их экспертам и федеральным центрам"
#         " необходимо обучать классификаторы, выделять кластеры, создавать рекомендательные системы. В связи с этим мы "
#         "находимся в поиске сотрудника, которому близки эти задачи. About the company Company Федеральное государственное "
#         "бюджетное учреждение «Российский центр научной информации» Федеральное государственное бюджетное "
#         "учреждение «Российский центр научной информации» (далее - РЦНИ) . Основными направлениями деятельности РЦНИ являются"
#         " обеспечение работы с данными сферы исследований и разработок; выполнение функций оператора Белого списка журналов,"
#         " созданного в целях обеспечения мониторинга и оценки публикационной активности научных и образовательных организаций,"
#         " научных и научно-педагогических кадров; реализация экспертных услуг с организациями, осуществляющими научную"
#         " и научно-техническую деятельность. Responsibilities Решение классических задач NLP; обучение моделей, "
#         "включая обучение моделей с нуля и дообучение SOTA моделей; Поддержка и улучшение существующих моделей; "
#         "Написание эффективного и читаемого Python кода и документации к нему. Requirements Опыт работы с NLP задачами "
#         "(классификация, извлечение сущностей и т.д.); Уверенные знания Python NLP-библиотек ( spaCy, NLTK, Natasha, Gensim,"
#         " scikit-learn, Regex, AllenNLP, flair); Опыт работы c DL библиотеками (Hugging Face, PyTorch, Transformers); "
#         "Опыт работы с крупными языковыми моделями (LLM, RAG, LLaMA-Factory); Опыт работы с базами данных и системами "
#         "контроля версий (Postgres, GIT) . Будет плюсом Умение находить и предлагать новые решения; Опыт работы с векторными"
#         " базами данных и поисковыми индексами; Опыт работы с рекомендательными системами. Working conditions Гибкий "
#         "гибридный формат работы в Москве; Оформление в соответствии с ТК РФ, официальная заработная плата; Участие в "
#         "интересных проектах; Мощный GPU сервер. ", 
#                   # ✅ Добавь любое описание
#         "resume_text": "Kарпенко Сергей Мужчина 7 (962) 4494951 iskarp35gmail.com — предпочитаемый способ связи Другой сайт "
#         "httpsgithub.comSergeyKarpenko1 Проживает Москва Гражданство Россия, есть разрешение на работу Россия Не готов к переезду, "
#         "готов к командировкам Желаемая должность и зарплата Data Scientist (NLP) Специализации — Дата-сайентист Занятость полная занятость "
#         "График работы полный день, удаленная работа Желательное время в пути до работы не имеет значения "
#         "Опыт работы — 3 года 1 месяц Сентябрь 2024 — Февраль 2025 6 месяцев FronTech AI Москва Информационные технологии, системная интеграция, "
#         "интернет Разработка программного обеспечения Системная интеграция, автоматизации технологических и бизнес-процессов предприятия, "
#         "ИТ-консалтинг Data Scientist (NLPRAG) Стек Python, pdfplumber, PyTorch, Hugging Face, Transformers, OpenAI, FastAPI, LangChain, Chroma, "
#         "pytesseract. Cпроектировал и разработал с нуля систему Retrieval-Augmented Generation (RAG) для оптимизации поиска и генерации релевантной "
#         "информации на основе корпоративных данных, включая регламенты, закупочную документацию и прайс-листы. Использовал библиотеки PyPDFLoader и "
#         "pytesseract для обработки документов в различных форматах (PDF, изображения), обеспечив 95 точность извлечения текста. Реализовал семантическое "
#         "разделение документов на чанки, что улучшило структуризацию данных и ускорило обработку. Настроил и оптимизировал базу данных Chroma для "
#         "индексирования данных, что сократило время поиска релевантной информации. Применил алгоритмы MMR (Maximal Marginal Relevance), что повысило "
#         "точность поиска релевантной информации в векторной базе на 20. Использовал GPT-4o-mini для генерации текстов и решения задач обработки "
#         "естественного языка, что позволило сократить время и улучшить качество генерации ответов. Построил с использованием LangChain сложные цепочки "
#         "обработки данных, автоматизировав ключевые сценарии работы с текстом. Результат Система успешно внедрена и обеспечивает быстрый и точный доступ "
#         "к данным, что повышает эффективность сотрудников и снижает затраты на поиск и обработку информации. Ноябрь 2023 — Август 2024 10 месяцев "
#         "TWINO Москва Финансовый сектор Резюме обновлено 14 марта 2025 в 1723 Финансово-кредитное посредничество (биржа, брокерская деятельность, "
#         "выпуск и обслуживание карт, оценка рисков, обменные пункты, агентства по кредитованию, инкассация, ломбард, платежные системы) Банк "
#         "Data scientist (ML) Стек Python, Pandas, Numpy, Matplotlib, Sklearn, CatBoost, Git, PostgresSQL Участвовал в полном цикле разработки "
#         "ML-моделей от формулирования целей и задач до оценки экономического эффекта, включая сбор и подготовку данных, обучение, валидацию и тестирование"
#         " моделей. Разрабатывал предложения и инструменты для улучшения процессов разработки ML-моделей, что позволило ускорить разработку и внедрение "
#         "решений. Мониторил текущие ML-модели и оптимизировал их для повышения точности и эффективности. Инициировал и тестировал новые источники данных, "
#         "что привело к улучшению ключевых метрик моделей. Рефакторил существующие R-скрипты и эндпоинты на Python для унификации и повышения "
#         "производительности системы. Сентябрь 2021 — Май 2023 1 год 9 месяцев XFIT Ставрополь Data scientist ML engineer Стек Python, Pandas, Numpy, "
#         "Matplotlib, Sklearn, Xgboost, CatBoost, LightGBM, Git XFIT это международная компания, которая уже не первый год является признанным "
#         "лидером рынка фитнес-услуг в России и активно развивается за рубежом. Мои основные обязанности Выявлял проблемы в бизнесе, которые можно "
#         "решить при помощи Data Science; обрабатывал и анализировал данные с использованием статистических методов (python, pandas, numpy). "
#         "Создавал информативные графические представления данных и извлекал ключевую информацию, которая помогала в принятии решений (mathplotlib, seaborn)."
#         " Строил ML модели для оптимизации работы фитнес клуба, включая прогнозирование факторов, таких как посещаемость, выручка и эффективность "
#         "маркетинговых мероприятий (LogisticRegression). Выявлял потребности клиентов в новых видах услуг при помощи анализа посещения различных зон клуба."
#         " Решал задачи детекции при помощи CV (YOLO, detectron2). Внедрял и оптимизировал модели, а также мониторил и улучшал их эффективность в "
#         "рабочем процессе. Достижения Используя базу данных переписок отдела продаж с клиентами, разработал телеграм-бот с применением глубокого обучения "
#         "(DL) и Sentence Transformers (PyTorch), что помогло улучшить эффективность коммуникации отдела продаж с клиентами клуба. Увеличил прибыль фитнес "
#         "департамента на 9 гг, в последний год работы на 14 гг. Образование Высшее 2008 Ставропольский государственный университет, Ставрополь Информатика "
#         "и вычислительная техника, Автоматизированные системы обработки информации и управления Навыки Знание языков Русский — Родной Kарпенко Сергей Резюме"
#         " обновлено 14 марта 2025 в 1723 Английский — B1 — Средний Навыки Python Big Data Machine Learning Jupiter NLP Computer Vision Seaborn Matplotlib "
#         "pandas Numpy Git Docker NN Deep Learning PostgreSQL RAG BERT GPT HaggingFace FastAPI CatBoost sklearn LangChain Дополнительная информация Обо мне "
#         "Я Data Scientist с 3-летним стажем работы в области machine learning и deep learning. Специализируюсь на разработке решений с применением нейронных"
#         " сетей и трансформеров для задач обработки естественного языка (NLP), включая BERT, GPT, и адаптацию моделей с использованием PEFT. Имею опыт "
#         "реализации Retrieval-Augmented Generation (RAG) систем для интеграции внешних данных в генерацию текстов. Моя экспертиза включает построение, "
#         "обучение и оптимизацию моделей для классификации, предсказания последовательностей и генерации текстов. Имею опыт полного цикла разработки "
#         "ML-моделей от формулирования целей до оценки экономического эффекта, включая сбор данных, обучение, тестирование и валидацию. Разрабатывал "
#         "инструменты для оптимизации процессов разработки ML, что ускорило внедрение решений. Оптимизировал текущие ML-модели, улучшая их точность и "
#         "эффективность. Стек Python, Pandas, Numpy, Matplotlib, Sklearn, PyTorch, Hugging Face, Transformers (BERT, GPT), PEFT (LoRA, prompt tuning), "
#         "RAG , XGBoost, CatBoost, LightGBM, PostgreSQL, Git Катаюсь на сноуборде, люблю спорт. Телеграм Karpenko_Sergey1 Kарпенк"  # ✅ Добавь любое резюме
#     }

#     try:
#         SpecialResume().crew().test(
#             n_iterations=int(sys.argv[1]), 
#             eval_llm=sys.argv[2], 
#             inputs=inputs  # ✅ Теперь передаём входные данные
#         )
#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")
