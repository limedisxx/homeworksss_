import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


# Класс для тестирования
class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Usain", 10)
        self.andrew = Runner("Andrew", 9)
        self.nick = Runner("Nick", 3)

    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(result)

    def test_usain_vs_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results[1] = {place: runner.name for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())].name == "Nick")

    def test_andrew_vs_nick(self):
        tournament = Tournament(90, self.andrew, self.nick)
        results = tournament.start()
        TournamentTest.all_results[2] = {place: runner.name for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())].name == "Nick")

    def test_usain_andrew_vs_nick(self):
        tournament = Tournament(90, self.usain, self.andrew, self.nick)
        results = tournament.start()
        TournamentTest.all_results[3] = {place: runner.name for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())].name == "Nick")


if __name__ == "__main__":
    unittest.main()