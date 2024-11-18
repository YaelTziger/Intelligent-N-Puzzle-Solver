# mmn 11 Yael Tzaiger 326021672
#בממן זה הושקעו דם יזע ודמעות
import sys
from collections import deque
import heapq

def create_state(array):
    return tuple(array)

#הפונקציות הבאות מגדירות מהלכים חוקיים ומחזירות מצב לוח המתקבל לאחר הפעלתן או נאל אם הפעולה אינה חוקית
def up(state,i):
    if i < 3:
        return None
    new_order = list(state)
    new_order[i], new_order[i - 3] = new_order[i - 3], new_order[i]
    return tuple(new_order)


def down(state,i):
    if i > 5:
        return None
    new_order = list(state)
    new_order[i], new_order[i + 3] = new_order[i + 3], new_order[i]
    return tuple(new_order)


def left(state,i):
    if i % 3 == 0:
        return None
    new_order = list(state)
    new_order[i], new_order[i - 1] = new_order[i - 1], new_order[i]
    return tuple(new_order)


def right(state,i):
    if i % 3 == 2:
        return None
    new_order = list(state)
    new_order[i], new_order[i + 1] = new_order[i + 1], new_order[i]
    return tuple(new_order)


def is_goal_state(state):
    return state == tuple(range(9))

    # expand_count += 1
    # path.append()
    # explored.add()
    #if path not in explored:


moves = [up,down,right,left]
def expand(state,path,moves):
    #השיטה הזו מפתחת מצב ומחזירה מערך עם המצבים השכנים שלו
    i = state.index(0)
    res = []
    for move in moves:
        neighbor = move(state, i)
        if neighbor:
            res.append((neighbor,neighbor[i]))
            # נחזיר גם את המספר במקום ה-איי, הוא זה שהוחלף עם ה0ויתווסף למסלול כשניקח את השכן
    return res



def bfs(initial_state):
    #  מבני נתונים
    frontier = deque([(initial_state, [])])  # תור של מצבים, לכל מצב נשמור את המסלול שהוביל אליו
    explored = set()  # סט לשמירת מצבים שכבר ביקרנו בהם
    expand_count = 0  # מספר הצמתים שפותחו

    while frontier:
        # נתחיל ממצב שבראש התור
        current_state, path = frontier.popleft()

        # הגענו לפתרון, נחזיר אותו
        if is_goal_state(current_state):
            return expand_count, path

        explored.add(current_state)

        # מתקדמים לשכנים של הצומת הנוכחי
        for neighbor, swapped_number in expand(current_state, path, moves):
            if neighbor not in explored and neighbor not in [state for state, _ in frontier]:
                # מוסיפים את המצב החדש לתור ומעדכנים את המסלול שלו
                frontier.append((neighbor, path + [swapped_number]))

        expand_count += 1  # מעדכנים את הקאונטר

    # אם לא נמצא פתרון
    return expand_count, None

def iddfs(initial_state):

    def dls(state, depth, path):
        """Recursive Depth Limited Search"""
        nonlocal expand_count
        expand_count += 1
        if is_goal_state(state):
            return path
        if depth == 0:
            return None
        explored.add(state)
        i = state.index(0)
        for move in moves:
            neighbor = move(state, i)
            if neighbor and neighbor not in explored:
                result = dls(neighbor, depth - 1, path + [neighbor[i]])
                if result is not None:
                    return result
        return None

    depth = 0
    while True:
        explored = set()
        expand_count = 0
        result = dls(initial_state, depth, [])
        if result is not None:
            return expand_count, result
        depth += 1



def heuristic(state):
    """
    יוריסטיקה המבוססת על מספר השכנים השגויים לכל אריח.
    """
    goal_state = tuple(range(9))
    incorrect_neighbors = 0

    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # מעלה, מטה, שמאל, ימין
    for i, value in enumerate(state):
        if value == 0:  # מתעלמים מהרווח
            continue
        for dx, dy in neighbors:
            x, y = divmod(i, 3)
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                neighbor_index = nx * 3 + ny
                if state[neighbor_index] != goal_state[neighbor_index]:
                    incorrect_neighbors += 1
    return incorrect_neighbors


def gbfs(initial_state, heuristic):
    frontier = [(heuristic(initial_state), initial_state, [])]  # תור עדיפות
    heapq.heapify(frontier)
    explored = set()  # צמתים שכבר ביקרנו בהם
    expand_count = 0

    while frontier:
        # מוציאים את המצב עם הערך היוריסטי הנמוך ביותר
        _, current_state, path = heapq.heappop(frontier)

        # בדיקת יעד
        if is_goal_state(current_state):
            return expand_count, path

        # סימון המצב כ"מפותח"
        explored.add(current_state)
        expand_count += 1

        # הרחבת הצומת הנוכחי
        i = current_state.index(0)  # מיקום הרווח
        for move in moves:
            neighbor = move(current_state, i)
            if neighbor and neighbor not in explored:
                # הערכת המצב החדש על בסיס היוריסטיקה
                heapq.heappush(frontier, (heuristic(neighbor), neighbor, path + [neighbor[i]]))
    return expand_count, None


def a_star(initial_state, heuristic):

    frontier = [(heuristic(initial_state), 0, initial_state, [])]
    heapq.heapify(frontier)
    explored = set()
    expand_count = 0

    while frontier:
        f, g, current_state, path = heapq.heappop(frontier)

        if is_goal_state(current_state):
            return expand_count, path

        explored.add(current_state)
        i = current_state.index(0)
        expand_count += 1

        for move in moves:
            neighbor = move(current_state, i)
            if neighbor and neighbor not in explored:
                new_g = g + 1
                heapq.heappush(frontier, (new_g + heuristic(neighbor), new_g, neighbor, path + [neighbor[i]]))
    return expand_count, None


if __name__ == '__main__':
    if len(sys.argv) != 10:
        print("Usage: python program_name.py num1 num2 num3 num4 num5 num6 num7 num8 num9")
        sys.exit(1)

    try:
        board_array = list(map(int, sys.argv[1:]))
    except ValueError:
        print("All inputs must be integers.")
        sys.exit(1)

    if len(board_array) != 9 or sorted(board_array) != list(range(9)):
        print("Invalid input! Please enter exactly 9 unique numbers from 0 to 8.")
        sys.exit(1)

    #קריאה לאלגוריתמים והדפסת הפלט

    initial_state = create_state(board_array)
    expanded_count,path = bfs(initial_state)
    print("BFS:")
    print("nodes expanded:", expanded_count)
    print("solution path: ", path)

    expanded_count, path = iddfs(initial_state)
    print("IDDFS:")
    print("nodes expanded:", expanded_count)
    print("solution path: ", path)

    expanded_count, path = gbfs(initial_state,heuristic)
    print("GBFS:")
    print("nodes expanded:", expanded_count)
    print("solution path: ", path)

    expanded_count, path = a_star(initial_state, heuristic)
    print("A*:")
    print("nodes expanded:", expanded_count)
    print("solution path: ", path)







