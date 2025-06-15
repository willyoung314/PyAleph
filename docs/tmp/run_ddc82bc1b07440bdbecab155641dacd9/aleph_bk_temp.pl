:- use_module(aleph).
:- if(current_predicate(use_rendering/1)).
:- use_rendering(prolog).
:- endif.
:- aleph.
:-style_check(-discontiguous).
:- aleph_set(noise,4).
:- aleph_set(minpos,2).
:- aleph_set(clauselength,4).
:- aleph_set(search,df).
:- aleph_set(i,0).
:- style_check(-singleton).
:- style_check(-discontiguous).
:- determination(illegal/6, adj/2).
:- determination(illegal/6, lt/2).
:- modeb(*,lt(+int,+int)).
:- modeb(*,adj(+int,+int)).
:- modeh(1,illegal(+int,+int,+int,+int,+int,+int)).

:-begin_bg.
lt(0,1).
lt(0,2).
lt(0,3).
lt(0,4).
lt(0,5).
lt(0,6).
lt(0,7).
lt(1,2).
lt(1,3).
lt(1,4).
lt(1,5).
lt(1,6).
lt(1,7).
lt(2,3).
lt(2,4).
lt(2,5).
lt(2,6).
lt(2,7).
lt(3,4).
lt(3,5).
lt(3,6).
lt(3,7).
lt(4,5).
lt(4,6).
lt(4,7).
lt(5,6).
lt(5,7).
lt(6,7).
adj(0,0).
adj(1,1).
adj(2,2).
adj(3,3).
adj(4,4).
adj(5,5).
adj(6,6).
adj(7,7).
adj(0,1).
adj(1,2).
adj(2,3).
adj(3,4).
adj(4,5).
adj(5,6).
adj(6,7).
adj(7,6).
adj(6,5).
adj(5,4).
adj(4,3).
adj(3,2).
adj(2,1).
adj(1,0).
:-end_bg.

:-begin_in_pos.
illegal(6,6,6,6,1,7).
illegal(1,7,5,3,2,3).
illegal(6,7,1,7,7,7).
illegal(1,2,6,5,6,4).
:-end_in_pos.

:-begin_in_neg.
illegal(3,6,1,7,6,3).
illegal(4,3,4,0,3,1).
illegal(6,4,7,3,6,7).
illegal(5,3,3,6,6,1).
illegal(0,0,0,6,1,2).
illegal(6,1,7,5,1,7).
illegal(7,6,0,4,5,1).
:-end_in_neg.
