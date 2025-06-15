:- use_module(aleph).
:- if(current_predicate(use_rendering/1)).
:- use_rendering(prolog).
:- endif.
:- aleph.
:-style_check(-discontiguous).
:- aleph_set(noise,2).
:- aleph_set(minpos,2).
:- aleph_set(clauselength,4).
:- aleph_set(search,df).
:- style_check(-singleton).
:- style_check(-discontiguous).
:- modeb(*,lt(+int,+int)).
:- modeh(1,illegal(+int,+int,+int,+int,+int,+int)).
:- modeb(*,adj(+int,+int)).
:- determination(illegal/6, lt/2).
:- determination(illegal/6, adj/2).

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
illegal(0,6,0,5,0,4).
illegal(6,6,2,0,5,7).
illegal(5,4,6,3,4,5).
illegal(7,4,5,1,6,4).
illegal(2,5,1,0,3,0).
illegal(2,6,0,5,3,6).
illegal(1,6,5,2,5,3).
illegal(6,6,6,6,1,7).
illegal(4,0,3,7,6,7).
illegal(3,3,4,2,2,4).
illegal(5,4,1,7,1,2).
illegal(1,5,3,2,1,6).
illegal(5,7,5,7,4,0).
illegal(1,7,6,1,6,4).
illegal(6,7,1,7,7,7).
illegal(6,5,4,0,7,6).
illegal(4,3,1,1,3,3).
illegal(6,2,4,7,1,7).
illegal(5,2,5,1,3,1).
illegal(3,0,1,6,4,1).
illegal(2,2,4,3,4,7).
illegal(6,7,5,6,5,4).
illegal(4,4,7,4,6,4).
illegal(5,6,0,6,0,4).
illegal(3,6,2,4,1,4).
illegal(0,1,2,6,2,7).
illegal(0,3,6,6,1,4).
illegal(5,6,7,6,7,2).
illegal(2,2,0,2,2,3).
illegal(3,3,5,5,5,7).
illegal(3,5,3,5,2,0).
illegal(5,0,5,0,6,4).
illegal(0,7,0,2,0,2).
illegal(4,4,0,6,1,6).
illegal(3,2,2,0,3,1).
illegal(1,2,6,5,6,4).
illegal(4,6,3,7,7,7).
illegal(5,6,7,5,1,5).
:-end_in_pos.

:-begin_in_neg.
illegal(7,2,6,7,1,1).
illegal(3,2,7,7,1,0).
illegal(3,7,6,2,1,5).
illegal(4,1,2,1,1,7).
illegal(3,1,1,2,0,6).
illegal(4,7,6,2,5,3).
illegal(5,4,7,5,0,7).
illegal(7,2,5,1,4,2).
illegal(6,7,0,1,3,3).
illegal(7,5,0,7,5,4).
illegal(7,7,2,3,7,1).
illegal(3,3,5,0,1,1).
illegal(2,7,6,2,0,5).
illegal(6,2,0,4,1,5).
illegal(3,6,1,7,6,3).
illegal(6,4,7,3,6,7).
illegal(1,1,5,3,7,7).
illegal(5,3,7,6,0,5).
illegal(0,6,0,0,5,5).
illegal(1,3,7,0,2,7).
illegal(5,5,1,4,0,6).
illegal(5,5,3,2,5,1).
illegal(0,2,1,3,7,7).
illegal(7,2,7,0,5,6).
illegal(2,2,5,1,7,5).
illegal(6,7,2,1,5,2).
illegal(3,0,5,4,6,6).
illegal(5,3,3,6,6,1).
illegal(4,4,7,5,6,4).
illegal(5,3,7,6,4,7).
illegal(5,2,3,7,0,3).
illegal(6,3,3,2,6,1).
illegal(6,7,0,2,5,0).
illegal(4,2,0,0,6,5).
illegal(6,4,3,4,6,6).
illegal(1,5,6,4,5,6).
illegal(5,3,3,3,0,6).
illegal(5,1,7,1,2,1).
illegal(4,7,2,0,5,1).
illegal(6,2,7,2,1,1).
illegal(0,4,3,0,6,3).
illegal(3,1,4,0,6,5).
illegal(0,0,2,3,7,2).
illegal(2,6,6,5,4,0).
illegal(0,0,0,7,4,1).
illegal(4,5,6,4,2,7).
illegal(7,3,7,0,4,6).
illegal(5,0,3,7,0,1).
illegal(4,2,4,5,2,3).
illegal(3,3,4,2,5,3).
illegal(6,6,3,1,4,6).
illegal(4,4,5,3,7,5).
illegal(6,6,4,5,2,4).
illegal(1,7,0,2,6,0).
illegal(0,5,3,2,0,7).
illegal(7,6,0,4,5,1).
illegal(3,2,2,3,5,7).
illegal(0,5,0,2,7,5).
illegal(7,4,5,7,4,2).
illegal(5,5,2,4,1,7).
illegal(2,3,0,4,4,5).
illegal(0,0,1,5,3,6).
illegal(1,6,7,7,5,3).
illegal(3,1,6,5,5,7).
illegal(7,2,5,5,4,3).
illegal(4,0,6,1,4,4).
illegal(0,3,3,0,6,4).
illegal(5,0,0,6,5,2).
illegal(7,0,2,3,7,6).
illegal(7,1,5,5,7,6).
illegal(6,1,7,5,1,7).
illegal(3,0,4,3,5,0).
illegal(3,2,4,7,6,0).
illegal(0,4,2,6,4,1).
illegal(0,7,4,6,7,5).
:-end_in_neg.
