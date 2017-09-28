from Settings_points import POINTS_NAME_PLURAL, POINTS_USE

CHANNEL = "rubmybum"

# If you send more than 20 commands or messages to the server within 30 seconds, you will be locked out for 30 minutes.
# If you send commands/messages only to channels in which you have Moderator or Operator status, the limit is 100 messages per 30 seconds.
MESSAGES_ALLOWED = 20 # number of messages allowed...
MESSAGES_SECONDS = 30 # ... in this many seconds.
MESSAGE_SPLIT_SIZE = 400 # if a string being sent to IRC is longer than this it will be segmented and app/prepended with... (note max is 500 char for IRC command&params see chapter above https://tools.ietf.org/html/rfc2812.html#section-2.3.1)
MESSAGE_SPLIT_MARKER = "--"

# settings for users
USER_STARTING_POINTS = 50 # how many points a brand new user starts with
USER_AFK_TIMER = 180 # how long in seconds since last message before a user is considered AFK (900 = 15 mins)
USER_MESSAGES_STORED = 5 # how many messages to remember.

# file management settings
FILE_SAVE_PERIOD = 5 # how often in seconds to update the files
COMMAND_CLEAR_TIMER = 300 # how often in seconds to clear out unresolved pending commands. 300 is 5 minutes
COMMAND_CLEAR_RUN = 5 # how often in seconds to check for unresolved pending commands

# Bot sends this if user types !help
HELP_STRING=  "\"!"+POINTS_NAME_PLURAL+"\" to show how many "+POINTS_NAME_PLURAL+" you have. " # !eccies
HELP_STRING+= "\"!"+POINTS_USE+"\" or \"!"+POINTS_USE+" N\" to "+POINTS_USE+" N of your "+POINTS_NAME_PLURAL+". " #!dunt N
HELP_STRING+= "\"!give username N\" to give that user N of your "+POINTS_NAME_PLURAL+" (if you have that many). " #!give username N

# admin help
ADMIN_HELP_STRING = "Example poll creation: \"!poll Which is the best colour? [Red, Green, Blue] 180\" (where 180 is seconds until poll ends). "
ADMIN_HELP_STRING+= "Example bet creation: \"!bet Which team will win? [Red, Green, Blue]\". "
ADMIN_HELP_STRING+= "Show user points: \"!points userNameHere\". "
ADMIN_HELP_STRING+= "Add/subtract user points: \"!points userNameHere -150\" (negative subtracts, positive adds). "
ADMIN_HELP_STRING+= "Set user points: \"!setpoints userNameHere 250\" (negative subtracts, positive adds). "
ADMIN_HELP_STRING+= "Show all users points: \"!allpoints\" (negative subtracts, positive adds). "
