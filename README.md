# reminderbot
Bot that reminds me to do particular things at either 30m or 1h intervals (now with 15m intervals).

Very simple Python script that runs in terminal. Asks whether you want a 1 hour interval or a 30 minute interval, then waits until the clock hits either :30 or :00.
Once this occurs, it asks a series of questions. These could very easily be changed as they are just Python print statements.
First it tells you to drink water, then it asks if you've been focused. It generates a grounding exercise in case you haven't been focused.
It then asks you what you accomplished in the last interval (30m or 1h). 
It saves this to a list and tells you the last task you accomplished, if this is the second or further occurrence of the question.
It will then go back to waiting for the next :30 or :00.

When you are finished, type "q" when at one of the prompts. It will print out all the tasks you accomplished while the program was running and it was prompting you.
It will prompt for any input, then close itself.

The script is very simple and is not intended to be advanced. It is simply for making sure that I stay on topic since I have a tendency to wander.
In the future, I want to implement this onto something like Microsoft Agent so it will pop up a little character that will ask the same questions.
However, Agent is written in C# so this is unrealistic for me at the moment. Perhaps I will get around to it sometime.
  
1/18/2023 Additions  
- Added changing line for waiting, now displays the amount of time the program has been running and how long until next reminder  
- Fixed icon, but it only works from C:/Programming/reminderbot. At the moment, there doesn't appear to be a workaround  
- Changed to initiate when time_left is equal to zero, meaning regardless of the time interval chosen, it will be calculated separately from the if statement
- Added 15 minute intervals to the allowed inputs  
  
1/19/2023 Changes  
- Fixed the way the timer was displaying (was: 00:00:00.40200, now: 00:00:10)  
- Fixed interval problems (was retaining that, at minute 45 with 30m intervals, -15 was smaller than 15, now it will only subtract from larger interval)  
  
1/20/2023 Changes  
- Added "play" mode. This just reminds you to drink water and doesn't ask about whether you're focusing on work. Will add more in the future.
  
1/24/2023 Changes  
- Added time elapsed counter to first prompt. It asks if you drank water, you respond, then it tells you how long it took you to respond to it.  
