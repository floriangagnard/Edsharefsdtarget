# EDsharesystem

The purpose of this small tool is to get the FSDtarget of your wingman and put it in your clipboard. 
I've made this to replace the faulty "select wingman target" to make coop exploration easier.

How I made that : 
1. parse in real time the log to search for selected fsd target
2. get a fsd target
3. send it to EDSM thanks to their API : it's stored in a comment in the flights logs
4. on the the wingman side (who wants your selected fsd target) get the comment w/ EDSM API
5. on the the wingman side (who wants your selected fsd target) store it in his clipboard

some geeky features will come in future, like sounds, toggle on/off the paste feature, IDK maybe smt else but yeah...

I'm not a dev at all so my code could be reaaaaly crappy, plz be nice to me 🙇‍♀️