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

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.usain = Runner("Usain", 10)
        self.andrew = Runner("Andrew", 9)
        self.nick = Runner("Nick", 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        for _ in range(10):
            self.usain.walk()
        self.assertEqual(self.usain.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        for _ in range(10):
            self.usain.run()
        self.assertEqual(self.usain.distance, 200)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        for _ in range(10):
            self.andrew.run()
            self.nick.walk()
        self.assertNotEqual(self.andrew.distance, self.nick.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.usain = Runner("Usain", 10)
        self.andrew = Runner("Andrew", 9)
        self.nick = Runner("Nick", 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_first_tournament(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.assertEqual(results[max(results.keys())].name, "Nick")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_second_tournament(self):
        tournament = Tournament(90, self.andrew, self.nick)
        results = tournament.start()
        self.assertEqual(results[max(results.keys())].name, "Nick")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_third_tournament(self):
        tournament = Tournament(90, self.usain, self.andrew, self.nick)
        results = tournament.start()
        self.assertEqual(results[max(results.keys())].name, "Nick")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RunnerTest))
    suite.addTest(unittest.makeSuite(TournamentTest))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())