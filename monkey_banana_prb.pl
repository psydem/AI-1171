% Facts
on(floor, monkey).
on(floor, chair).
in(room, monkey).
in(room, chair).
in(room, banana).
at(ceiling, banana).
strong(monkey).
grasp(monkey).
climb(monkey, chair).

% Rules
push(monkey, chair) :-
    strong(monkey).

under(banana, chair) :-
    push(monkey, chair).

canreach(banana, monkey) :-
    at(floor, banana);
    (at(ceiling, banana),
    under(banana, chair),
    climb(monkey, chair)).

canget(banana, monkey) :-
    canreach(banana, monkey),
    grasp(monkey).

% Custom rule to print the desired message
get_banana_message :-
    canget(banana, monkey),
    write('monkey can get banana.').

% If the monkey cannot get the banana, we handle the false case to provide a message
get_banana_message :-
    \+ canget(banana, monkey),
    write('monkey cannot get banana.').

% Query example: get_banana_message.
