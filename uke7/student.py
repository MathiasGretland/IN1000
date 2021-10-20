class Student:
    def __init__(self, navn, quizScore, antallQuiz):
        self._navn = navn
        self._quizScore = quizScore
        self._antallQuiz = antallQuiz

    def leggTilQuizScore(self, poeng):
        self._quizScore += poeng
        self._antallQuiz += 1

    def gjennomsnittligScore(self):
        return self._quizScore / self._antallQuiz

    def printInformasjon(self):
        print(self._navn, "Har fått totalt", self._quizScore, "poeng på", self._antallQuiz, "quizzer.")

joakim = Student("Joakim", 0, 0)
kristin = Student("Kristin", 100, 1)
dag = Student("Dag", 50, 1)

joakim.leggTilQuizScore(40)
joakim.leggTilQuizScore(95)

kristin.leggTilQuizScore(70)
kristin.leggTilQuizScore(20)

dag.leggTilQuizScore(40)
dag.leggTilQuizScore(70)

joakim.printInformasjon()
print(joakim.gjennomsnittligScore())
kristin.printInformasjon()
print(kristin.gjennomsnittligScore())
dag.printInformasjon()
print(dag.gjennomsnittligScore())
