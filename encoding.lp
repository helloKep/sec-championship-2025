% { bama_win; tamu_win; miss_win }.

bama_loss :- not bama_win.
tamu_loss :- not tamu_win.
uga_loss  :- not uga_win.
miss_loss :- not miss_win.

bama_win :- not bama_loss.
tamu_win :- not tamu_loss.
uga_win  :- not uga_loss.
miss_win :- not miss_loss.

sec(bama) 	:- bama_win.
sec(tamu)	:- tamu_win.
sec(tamu)	:- bama_loss, miss_loss.
sec(uga) 	:- bama_loss.
sec(uga) 	:- tamu_loss.
sec(miss)	:- miss_win, bama_loss, tamu_loss.

#show sec/1.