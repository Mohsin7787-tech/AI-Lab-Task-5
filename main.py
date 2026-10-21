import math

leaves_mm = 0
leaves_ab = 0

scores = [7, 1, 4, 9, 2, 8, 6, 3]


def minimax(values, depth, maxDepth, maxTurn):
    global leaves_mm

    if depth == maxDepth:
        leaves_mm += 1
        return values[0]

    mid = len(values) // 2

    left = values[:mid]
    right = values[mid:]

    if maxTurn:
        return max(
            minimax(left, depth + 1, maxDepth, False),
            minimax(right, depth + 1, maxDepth, False)
        )
    else:
        return min(
            minimax(left, depth + 1, maxDepth, True),
            minimax(right, depth + 1, maxDepth, True)
        )


def alpha_beta(values, depth, maxDepth, maxTurn,
               alpha, beta):
    global leaves_ab

    if depth == maxDepth:
        leaves_ab += 1
        return values[0]

    mid = len(values) // 2
    children = [values[:mid], values[mid:]]

    if maxTurn:
        value = -math.inf

        for child in children:
            value = max(value, alpha_beta(
                child, depth + 1, maxDepth, False,
                alpha, beta
            ))
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = math.inf

        for child in children:
            value = min(value, alpha_beta(
                child, depth + 1, maxDepth, True,
                alpha, beta
            ))
            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


answer1 = minimax(scores, 0, 3, True)

answer2 = alpha_beta(
    scores, 0, 3, True, -math.inf, math.inf
)

print("Minimax Root Value:", answer1)
print("Minimax Leaves Checked:", leaves_mm)
print("Alpha-Beta Root Value:", answer2)
print("Alpha-Beta Leaves Checked:", leaves_ab)
