import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.blank_pos = self.find_blank_pos()
        self.cost = self.moves + self.manhattan_distance()

    def find_blank_pos(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)

    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    x, y = divmod(self.board[i][j] - 1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def is_goal(self):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.board == goal

    def possible_moves(self):
        i, j = self.blank_pos
        moves = []
        if i > 0: moves.append((i - 1, j))
        if i < 2: moves.append((i + 1, j))
        if j > 0: moves.append((i, j - 1))
        if j < 2: moves.append((i, j + 1))
        return moves

    def generate_new_state(self, move):
        new_board = [row[:] for row in self.board]
        i, j = self.blank_pos
        ni, nj = move
        new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
        return PuzzleState(new_board, self.moves + 1, self)

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(map(tuple, self.board)))

def print_solution(solution):
    steps = []
    state = solution
    while state:
        steps.append(state.board)
        state = state.previous
    steps.reverse()
    for step in steps:
        for row in step:
            print(row)
        print()
    print(f"Number of steps: {len(steps) - 1}")
    print(f"Path cost: {len(steps) - 1}")  # Path cost is the number of steps taken

def solve_puzzle(initial_board):
    initial_state = PuzzleState(initial_board)
    if initial_state.is_goal():
        return initial_state

    frontier = []
    heapq.heappush(frontier, initial_state)
    explored = set()

    while frontier:
        current_state = heapq.heappop(frontier)
        if current_state.is_goal():
            return current_state

        explored.add(current_state)

        for move in current_state.possible_moves():
            new_state = current_state.generate_new_state(move)
            if new_state not in explored:
                heapq.heappush(frontier, new_state)

    return None

# Example usage:
initial_board = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = solve_puzzle(initial_board)
if solution:
    print_solution(solution)
else:
    print("No solution found.")
