# Bruhmongus AppStore

## Een een homemade multiapplicatie hub met zelf geschreven programma's
In met deze app kan je verschillende dingen doen:
- Spelletjes zoals Guess the Num of Hangman spelen
- Berekeningen doen met de rekenmachine
- Je dag bij houden met je eigen dagboek!



# Geavanceerde features:

In de main gebruik ik de os library om de gebruiker van de device op te vragen
```python
    import os
    user = os.getlogin()
```
In Hangman gebruik ik de door [Noah](https://github.com/TheBiemGamer) en ik gemaakte library [The_Hangman_Wordlist](https://github.com/TheBiemGamer/TheHangmanWordlist) voor het opvragen van woorden
```python
    from the_hangman_wordlist import HangmanWordlist
    wordlist = HangmanWordlist()
    word = wordlist.pull_word(difficulty)
```
In de rekenmachine:
```python
    from tkinter import *
    from tkinter import ttk
```