<h1 align="center"> <img width="150" height="150" src="https://user-images.githubusercontent.com/66639966/178153463-7ab79c8a-24d9-408f-9649-e1aebcf3ae24.png" /> <br> Wordle (CLI version) </h1>
Original Wordle: https://www.nytimes.com/games/wordle
<p> Wordle is a web-based word game created and developed by Welsh software engineer Josh Wardle, and owned and published by The New York Times Company since 2022.</p>
In this project, I have created a very similar version of the game which executes right on your terminal as a Python program. 

# Required Python packages
- random <br>
  See documentation <a href="https://docs.python.org/3/library/random.html">here.</a>
  
- colorama <br>
  See documentation <a href="https://pypi.org/project/colorama/">here.</a>
- enchant <br>
  See documentation <a href="https://pypi.org/project/pyenchant/">here.</a>

# Key differences
- <b> It provides hints! </b>
   <br> The original Wordle does not provide any hints to the user whereas this project allows the user to uncover any one letter from the five letter word they are trying to guess.
   
- <b> Play unlimited times in a day </b>
  <br> As we know, Wordle provides a single word each day. This version allows you to play as many times as you want with a great experience of unique words. The total number of words used in the game is 5757.
