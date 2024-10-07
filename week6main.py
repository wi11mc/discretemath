# william mcandrew week 6 secondary
import ttg 

print(ttg.Truths(['(p ∧ q ) ∨ ~p']))
#this is using 'and'(conjunction), 'or'(disjunction), 'not'(negation) operators

print(ttg.Truths(['~ p→ (~q ∨ p )']))
#this is using '~'(negation), '→'(implication), 'V'(disjunction) operators

print(ttg.Truths(['(~ p→q ) ∨ (~p ∧ ~q)']))

print(ttg.Truths(['~p →(q ∧ r).']))