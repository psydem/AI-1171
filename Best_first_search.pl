% Define edges of the graph with their respective costs
edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 3).
edge(c, d, 1).
edge(c, e, 5).
edge(d, e, 1).

% Define heuristic values for each node
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 2).
heuristic(d, 1).
heuristic(e, 0).

% Best-First Search algorithm
best_first_search(Start, Goal, Path) :-
    heuristic(Start, H),
    bfs([(H, Start, [Start])], Goal, Path).

% Base case: if the first element in the priority queue is the goal
bfs([(_, Goal, Path) | _], Goal, Path).

% Recursive case: expand the first node and add its neighbors to the priority queue
bfs([(_, Node, Path) | Rest], Goal, FinalPath) :-
    findall((H, Neighbor, NewPath),
            (edge(Node, Neighbor, _),
             \+ member(Neighbor, Path), % avoid cycles
             append(Path, [Neighbor], NewPath),
             heuristic(Neighbor, H)),
            Neighbors),
    append(Rest, Neighbors, NewQueue),
    insertion_sort(NewQueue, SortedQueue),
    bfs(SortedQueue, Goal, FinalPath).

% Insertion sort based on heuristic value
insertion_sort(List, Sorted) :- i_sort(List, [], Sorted).
i_sort([], Acc, Acc).
i_sort([(H, N, P) | T], Acc, Sorted) :-
    insert((H, N, P), Acc, NAcc),
    i_sort(T, NAcc, Sorted).

insert((H, N, P), [(H1, N1, P1) | T], [(H1, N1, P1) | NT]) :-
    H > H1, !, 
    insert((H, N, P), T, NT).
insert((H, N, P), T, [(H, N, P) | T]).

% Query example: best_first_search(a, e, Path).
