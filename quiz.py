import random

questions_with_answers = [
        {"question": "What is the capital city of France?", "answer": "Paris"},
        {"question": "Which country has the largest population in the world?", "answer": "China"},
        {"question": "What is the national animal of Australia?", "answer": "Kangaroo"},
        {"question": "Which country is known as the Land of the Rising Sun?", "answer": "Japan"},
        {"question": "In which country is the world's highest mountain, Mount Everest, located?", "answer": "Nepal"},
        {"question": "What is the official language of Brazil?", "answer": "Portuguese"},
        {"question": "Which country has the longest coastline in the world?", "answer": "Canada"},
        {"question": "What currency is used in Japan?", "answer": "Japanese Yen"},
        {"question": "Which country is the smallest by land area?", "answer": "Vatican City"},
        {"question": "What is the name of the river that runs through Egypt?", "answer": "The Nile"},
        {"question": "Which country is home to the ancient city of Petra?", "answer": "Jordan"},
        {"question": "What is the national dish of Italy?", "answer": "Pizza"},
        {"question": "Which country is known for inventing the sauna?", "answer": "Finland"},
        {"question": "In what country can you find the historic ruins of Machu Picchu?", "answer": "Peru"},
        {"question": "What is the most spoken language in the world?", "answer": "Mandarin Chinese"},
        {"question": "Which country is famous for its fjords?", "answer": "Norway"},
        {"question": "What are the official languages of Canada?", "answer": "English and French"},
        {"question": "Which African country was formerly known as Abyssinia?", "answer": "Ethiopia"},
        {"question": "What is the largest island in the world?", "answer": "Greenland"},
        {"question": "Which country has won the most Summer Olympic medals?", "answer": "United States"}
    ]

while True:
    print("********************************")
    random_question_object = questions_with_answers[random.randint(0, len(questions_with_answers))]
    print(f"Question: {random_question_object['question']}")
    
    my_answer = input("Answer: ")
    if random_question_object["answer"] == my_answer:
        print("Urraa! You found the answer!")
    else:
        print("Don't cry! Try another question. Moskow was not built at once.")