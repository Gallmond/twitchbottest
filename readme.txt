Set up guide v1

====== You will need ======
a twitch account specifically for the bot (this is normal, and twitch allows multiple accounts on one email)

====== Installation (Windows) ======
- Run the Python installer found in the PythonInstaller folder. Choose the option with IDLE.

====== Configuration ======
- Generate a twitch oAuth token for the bot's twitch account at: https://twitchapps.com/tmi/
- Fill in the details in Settings_auth.example.py
- Rename Settings_auth.example.py to Settings_auth.example.py
If you'd like to change some of the words the bot uses, look in Settings_points.py
If you'd like to change the 'house' take from the betting system, look in Settings_bets.py

====== Start bot ======
- Double-click run.py (this should open a windows cmd prompt and begin outputting information to the screen)
If windows cmd prompt doesn't run this file:
- Open IDLE, the graphical user interface for running Python scripts installed earlier.
- File > Open > run.py then Run > Run Module (this will bring up a second IDLE window and begin outputting information to the screen)

- You can also run ReadUserFile.py to get human-readable information about the user list

====== Mod bot commands (all whispers) =======
Many mod commands will cause the bot to whisper you with an instruction to confirm the action, just whisper back "!confirm " followed by the code it tells you):
"!killbot" will kill the bot gracefully, and save the current userlist to file.

"!allpoints" will give a dense list of users and their current point amounts.
"!points USERNAME" will show how many points that user has.
"!points USERNAME NUMBER" will add or subtract the NUMBER of points entered for that USERNAME, negative number will subtract, positive will add.
"!setpoints USERNAME NUMBER" will set that user's points to the specified number.

"!bet QUESTION GOES HERE [Options, Go, Here]" This creates a bet, options can be multiple-words. eg: !bet Who will win this round? [Red team, Blue Team, Orange Team]
"!betcancel CODE" This silently cancels a running bet
"!betend CODE WINNINGOPTION" This ends a bet, and sets the WINNINGOPTION as the winner, payouts are calculated and "paid" to users who played.
"!betstatus CODE" This returns some dense information about the current amount bet, as well as per-option and their payout rates if they were to win at that time. 

"!poll QUESTION GOES HERE [Options, Go, Here] NUMBER" This creates a poll, options can be multiple-words. The number is seconds until poll finishes.
"!pollcancl CODE" This silently cancels a running poll.
"!pollend CODE" This ends the poll early, but still shows the results in the chat.
"!pollstatus CODE" This shows some dense information about the current votes for each option

====== User commands (whisper and in-chat) =======
Here we'll use "biscuit" and "biscuits" as the point nouns  and "eat" as the using verb as an example:
"!biscuits" this announces in the chat how many points the user has
"!give USERNAME NUMBER biscuits" This gives the stated number of points to the named user (the single noun also works when the number is 1)
"!eat" This subtracts one point, and returns the string found in Settings_points.py under POINT_USED
"!eat NUMBER" This subtracts NUMBER points, and returns the string found in Settings_points.py under POINTS_USED

"!vote OPTION" This votes for the stated OPTION. A user can only vote once per poll.

"!stake OPTION NUMBER" This stakes NUMBER of points on the stated OPTION. User can bet on multiple options per poll, but only once per option.