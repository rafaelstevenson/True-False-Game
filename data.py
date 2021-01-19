
def choose_data():
    global question_data
    question_topic = input("Which Topic do you want (1/2/3/4)? ")
    if question_topic=='3':
        question_data = [
            {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
             "question": "Linus Torvalds created Linux and Git.", "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
             "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
             "question": "The logo for Snapchat is a Bell.", "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
             "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
             "question": "RAM stands for Random Access Memory.", "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
             "question": "Ada Lovelace is often considered the first computer programmer.", "correct_answer": "True",
             "incorrect_answers": ["False"]}, {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
                                               "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
                                               "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
             "question": "Time on Computers is measured via the EPOX System.", "correct_answer": "False",
             "incorrect_answers": ["True"]}, {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
                                              "question": "The Windows 7 operating system has six main editions.",
                                              "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
             "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
             "correct_answer": "True", "incorrect_answers": ["False"]}]
    elif question_topic=='2':
        question_data = [
            {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
             "question": "Igneous rocks are formed by excessive heat and pressure.", "correct_answer": "False",
             "incorrect_answers": ["True"]}, {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                                              "question": "Salt is 100% composed of Sodium.", "correct_answer": "False",
                                              "incorrect_answers": ["True"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
             "question": "An atom contains a nucleus.", "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
             "question": "An exothermic reaction is a chemical reaction that releases energy by radiating electricity.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
             "question": "An Astronomical Unit is the distance between Earth and the Moon.", "correct_answer": "False",
             "incorrect_answers": ["True"]}, {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                                              "question": "An average human can go two weeks without water.",
                                              "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
             "question": "Celiac Disease is a disease that effects the heart, causing those effected to be unable to eat meat.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
             "question": "Water always boils at 100&deg;C, 212&deg;F, 373.15K, no matter where you are.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
             "question": "Not including false teeth; A human has two sets of teeth in their lifetime.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
             "question": "A plant that has a life cycle for more than a year is known as an annual.",
             "correct_answer": "False", "incorrect_answers": ["True"]}]
    elif question_topic=='4':
        question_data = [
            {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy",
             "question": "In the 1988 film &quot;Akira&quot;, Tetsuo ends up destroying Tokyo.", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy",
             "question": "Studio Ghibli is a Japanese animation studio responsible for the films &quot;Wolf Children&quot; and &quot;The Boy and the Beast&quot;.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy",
             "question": "In Kill La Kill, the weapon of the main protagonist is a katana. ", "correct_answer": "False",
             "incorrect_answers": ["True"]},
            {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy",
             "question": "The anime &quot;Lucky Star&quot; follows the story of one girl who is unaware she is God.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy",
             "question": "Gosho Aoyama Made This Series: (Detective Conan \/ Case Closed!)", "correct_answer": "True",
             "incorrect_answers": ["False"]},
            {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy",
             "question": "In the &quot;Melancholy of Haruhi Suzumiya&quot; series, the narrator goes by the nickname Kyon.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy",
             "question": "In the &quot;Toaru Kagaku no Railgun&quot; anime,  espers can only reach a maximum of level 6 in their abilities.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy",
             "question": "The name of the attack &quot;Kamehameha&quot; in Dragon Ball Z was named after a famous king of Hawaii.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy",
             "question": "In the &quot;To Love-Ru&quot; series, Golden Darkness is sent to kill Lala Deviluke.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy",
             "question": "In Chobits, Hideki found Chii in his apartment.", "correct_answer": "False",
             "incorrect_answers": ["True"]}]
    elif question_topic=='1':
        question_data = [
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
             "question": "French is an official language in Canada.", "correct_answer": "True",
             "incorrect_answers": ["False"]}, {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
                                               "question": "It is automatically considered entrapment in the United States if the police sell you illegal substances without revealing themselves.",
                                               "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
             "question": "Bulls are attracted to the color red.", "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
             "question": "&quot;Ananas&quot; is mostly used as the word for Pineapple in other languages.",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy", "question": "Pluto is a planet.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
             "question": "When you cry in space, your tears stick to your face.", "correct_answer": "True",
             "incorrect_answers": ["False"]}, {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
                                               "question": "The Lego Group was founded in 1932.", "correct_answer": "True",
                                               "incorrect_answers": ["False"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
             "question": "Romanian belongs to the Romance language family, shared with French, Spanish, Portuguese and Italian. ",
             "correct_answer": "True", "incorrect_answers": ["False"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
             "question": "Vietnam&#039;s national flag is a red star in front of a yellow background.",
             "correct_answer": "False", "incorrect_answers": ["True"]},
            {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
             "question": "The mitochondria is the powerhouse of the cell.", "correct_answer": "True",
             "incorrect_answers": ["False"]}]
    else:
        print("Please input the topic's number correctly ~\n")
        choose_data()

question_data = []
choose_data()