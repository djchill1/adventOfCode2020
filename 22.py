import collections, logging

def read_data(isTest=False):
    if isTest:
        filename = "22_test.txt"
        logging.warning(" Using Test Data from " + filename)
    else:
        filename = "22_input.txt"
    with open(filename) as f:
        playerA, playerB = f.read().split('\n\n')
        queueA = collections.deque([int(x) for x in playerA.split('\n')[1:]])
        queueB = collections.deque([int(x) for x in playerB.split('\n')[1:]])
    return queueA, queueB


def play_round(queueA, queueB, isRecursive=False):
    cardA, cardB = queueA[0], queueB[0]
    winner = None
    if cardA > cardB:
        winner = 'A'
    elif cardA < cardB:
        winner = 'B'
    else:
        logging.error('NO WINNER FOR CARDS' + cardA + cardB)

    # remove cards from queue
    queueA.popleft()
    queueB.popleft()

    if isRecursive:
        if len(queueA) >= cardA and len(queueB) >= cardB:
            # need to play a subgame
            print('** Playing a sub-game to determine the winner...')
            subQueueA = collections.deque(queueA[:cardA])
            print(subQueueA)
        else:
            # no need to subgame
            if cardA > cardB:
                winner = 'A'
            else:
                winner = 'B'
    else:
        if cardA > cardB:
            winner = 'A'
        elif cardA < cardB:
            winner = 'B'
        else:
            logging.error('NO WINNER FOR CARDS' + cardA + cardB)
    # add cards to winners queue
    if winner == 'A':
        queueA.append(cardA)
        queueA.append(cardB)
    elif winner == 'B':
        queueB.append(cardB)
        queueB.append(cardA)

    return queueA, queueB


def part1():
    queueA, queueB = read_data(False)
    while len(queueA) > 0 and len(queueB) > 0:
        queueA, queueB = play_round(queueA, queueB)
        print(queueA, queueB)

    if len(queueA) > 0:
        queueA.reverse()
        winner = queueA
    else:
        queueB.reverse()
        winner = queueB

    # calculate score
    score = 0
    for index, value in enumerate(winner):
        score += (index + 1) * value
    return score


def part2():
    i = 0
    queueA, queueB = read_data(True)
    pastAs = set()
    pastBs = set()
    print('start', queueA, queueB)
    winner = None
    while winner is None:
        print("-- Round", i := i + 1, '--')
        queueA, queueB = play_round(queueA, queueB, True)
        if tuple(queueA) in pastAs and tuple(queueB) in pastBs:
            print('A wins due to recursion')
            winner = 'A'
            break
        pastAs.add(tuple(queueA))
        pastBs.add(tuple(queueB))
        print('iter', queueA, queueB)
        # print('pasts', pastAs, pastBs)


    return winner

print(part2())

# print(f'Part 1: {part1()}, Part 2: {part2()}')
