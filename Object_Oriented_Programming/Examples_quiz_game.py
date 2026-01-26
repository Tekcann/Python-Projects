# Question classı olacak ve sorular burada olacak

# Quiz classı olacak ve quiz ile ilgili işlemler burada olacak
# bir skor olacak en son kullanıcıya puan söylenecek

class Question: 
        #soru adı(sayısı)/Sorunun kendisi/seçenekleri(list-dizi şeklinde)/ cevap tek bitane
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
        
    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {question.text} ")

        for q in question.choices:
            print("-" + q)

        answer = input("cevap: ")
        self.guess(answer)
        self.loadQuestion()
    
    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1

        self.questionIndex += 1

    def loadQuestion(self):
        self.displayProgress()
        if (len(self.questions) == self.questionIndex):
            self.showScore()
        else:           
            self.displayQuestion()

    def showScore(self):
        print(f"score: {self.score}")

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if (questionNumber > totalQuestion):
            print("Sorular Bitti")
        else:
            print(f"Soru {totalQuestion} / {questionNumber}".center(51, "*"))
        


s1 = Question("Atatürk kaç yaşıda veft etti?", ["1938","1771","2009","1838"], "1938")
s2 = Question("Kaldırımlar şiiri hangi şair yazmıştır?",["Süleyman Sabah", "Nazım Hikmet Ran", "Mehmet Emin Yurdakul", "Necip Fazıl Kısakürek"], "Necip Fazıl Kısakürek")
s3 = Question("pasarofça antlaşmasının tarihi nedir?",["1785","1739","1718","68"], "1718") 
s4 = Question("Lale Devri kaç yıl sürmüştir?",["15","14","13","12"], "12")

questions = [s1,s2,s3,s4]

quiz = Quiz(questions)

quiz.displayQuestion()





