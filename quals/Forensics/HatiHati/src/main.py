def main():
    questions = [
        { 
            "question": "Apa Alamat IP yang dimiliki oleh penyerang?",
            "format": "127.0.0.1"
        },
        { 
            "question": "Nama plugin WordPress apa yang memiliki kerentanan yang dimanfaatkan oleh penyerang?",
            "format": "-"
        },
        { 
            "question": "CVE apa yang digunakan oleh penyerang untuk mengeksploitasi web korban?",
            "format": "CVE-2024-10101"
        },
        {
            "question": "Pukul berapa penyerang memulai melakukan serangan SQL Injection?",
            "format": "01/Jan/2024:01:02:03"
        },
        { 
            "question": "Apa nama database yang digunakan oleh web korban?",
            "format": "-"
        },
        { 
            "question": "Siapa nama pengguna (username) administrator pada web korban?",
            "format": "-"
        },
        { 
            "question": "Apa hash akun administrator pada web korban?",
            "format": "$P$B55D6LjfHDkINU5wF.v2BuuzO0/XPk/"
        },
    ]

    answers = [
        "110.138.171.206",
        "LearnPress",
        "CVE-2024-4434",
        "24/Sep/2024:16:23:22",
        "wordpress",
        "daffainfo",
        "$P$B6pFabrOXnaQVldD6M.QkHBQ/H.set/",
    ]

    print("Silahkan jawab pertanyaan-pertanyaan yang telah disediakan:")

    correct_answers = 0

    for index, q in enumerate(questions, start=1):
        print(f"\nNo {index}:")
        print("Pertanyaan: " + q["question"])
        print("Format: " + q["format"])
        user_answer = input("Jawaban: ")

        if user_answer.strip().lower() == answers[index - 1].lower():
            correct_answers += 1
            print("Correct")
        else:
            print("Incorrect")
            return
    
    if correct_answers == len(questions):
        print("\nCongrats! Flag: TCF{congrats_you_just_analyzed_nginx_log!!!}")

if __name__ == "__main__":
    main()