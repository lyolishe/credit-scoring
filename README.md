# Банковский скоринг

## Описание проекта
Этот проект посвящен разработке и сравнению моделей машинного обучения для оценки кредитного риска заемщиков. 
Цель моделей - предсказать вероятность дефолта по кредиту на основе характеристик клиента.

Цель проекта - научиться самостоятельно делать разведывательный анализ данных, реализовывать различные модели и сравнивать их эффективности.  

## Используемые технологии
- Python3
- Библиотеки:
  - pandas - для обработки и анализа данных
  - numpy - для численных операций
  - matplotlib - для визуализации данных

## Данные
Для обучения модели используется датасет:  
[Bank Credit Risk Assessment Dataset](https://www.kaggle.com/datasets/kapturovalexander/bank-credit-risk-assessment)

Для тестирования модели используется дополнительный датасет:  
[Credit Risk Analysis for Extending Bank Loans](https://www.kaggle.com/datasets/atulmittal199174/credit-risk-analysis-for-extending-bank-loans)

## Реализуемые модели
1. Логистическая регрессия
2. Случайный лес (Random Forest)
3. (Дополнительные модели по мере разработки)

## Метрики оценки
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

## Структура проекта
```
bank-scoring/
├── data/                    # Папка с данными
│   ├── train_data.csv       # Обучающий датасет
│   └── test_data.csv        # Тестовый датасет
├── models/                  # Сохраненные модели
├── notebooks/               # Jupyter notebooks с анализом
├── src/                     # Исходный код
│   ├── data_preprocessing.py
│   ├── models.py
│   └── evaluation.py
├── requirements.txt         # Зависимости
└── README.md                # Этот файл
```

## Установка и запуск
1. Клонировать репозиторий
2. Установить зависимости:
```bash
pip install -r requirements.txt
```
3. Запустить Jupyter notebook
