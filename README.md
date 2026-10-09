# deslugger

A simple reminder to move and drink water when stuck at a desk all day. 


Set with a cron job in Linux

In Windows 11:

1.Open Task Scheduler:Press the Windows Key, type "Task Scheduler", and hit Enter. In the right-hand Actions pane, click Create Task... (Do not use "Create Basic Task," as it lacks the advanced repeating options you need to mimic a cron job).

2.Configure the General Settings:Name your task something recognizable like "Kinetic Reset". Ensure Run only when user is logged on is selected. This is critical because GUI applications like tkinter cannot render if the task is run in the background under the system account.

3.Build the Cron Schedule (Triggers):Click the Triggers tab and click New....Set "Begin the task" to On a schedule.Select Weekly, check Monday through Friday, and set your start time to 8:00 AM.Under Advanced settings, check Repeat task every: and type 1 hour 30 minutes.Set "for a duration of:" to 9 hours (covering your 8 AM to 5 PM shift).Click OK.

4.Set the Python Action:Use pythonw.exe to prevent the command prompt from flashing.Click the Actions tab and click New....Action should be Start a program.Program/script: Enter the full path to pythonw.exe. The "w" stands for windowless, meaning the script will execute silently in the background and only the tkinter pop-up will appear. (You can find your Python path by opening Command Prompt and typing where pythonw).Add arguments: Enter the full, absolute path to your script wrapped in quotes (e.g., "C:\Users\Jeffrey\Documents\movement_break.py"). Click OK.