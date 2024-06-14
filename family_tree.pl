% Facts about genders (for illustration purposes)
male(john).
male(mark).
male(pat).
male(jim).

female(sue).
female(mary).
female(anne).
female(pat).

% Facts about the family relationships
parent(john, mary).
parent(john, mark).
parent(sue, mary).
parent(sue, mark).
parent(mary, anne).
parent(mary, pat).
parent(pat, jim).

% Rules to define different relationships
father(Father, Child) :-
    parent(Father, Child),
    male(Father).

mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

sibling(Sibling1, Sibling2) :-
    parent(Parent, Sibling1),
    parent(Parent, Sibling2),
    Sibling1 \= Sibling2.

ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Descendant).
ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Parent),
    ancestor(Parent, Descendant).

% Predicate to get user input and provide output
family_tree :-
    write('Enter a person: '),
    read(Person),
    nl,
    write('Grandparent: '), grandparent_output(Person),
    write('Parent: '), parent_output(Person),
    write('Sibling: '), sibling_output(Person).

grandparent_output(Person) :-
    grandparent(Grandparent, Person),
    write(Grandparent), write(', '),
    nl.

parent_output(Person) :-
    parent(Parent, Person),
    write(Parent), write(', '),
    nl.

sibling_output(Person) :-
    sibling(Sibling, Person),
    write(Sibling), write(', '),
    nl.

% Query for the user input
:- initialization(family_tree).
