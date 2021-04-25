def tournamentWinner(competitions, results):
    # Write your code here.
    participants = {}
    for i in range(len(results)):
        home, away = competitions[i]
        result = results[i]
        participants[home] = participants.get(home, 0) + (3 if result else 0)
        participants[away] = participants.get(away, 0) + (0 if result else 3)

    winner, max_points = '', -1
    for participant, points in participants.items():
        if points > max_points:
            winner, max_points = participant, points

    return winner


comp = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]
res = [0, 0, 1]

print(tournamentWinner(comp, res))
