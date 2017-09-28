# loyalty point settings
POINTS_NAME = "quid"
POINTS_NAME_PLURAL = "quids" # user types !POINTS_NAME_PLURAL for bot to tell them how many they have
POINTS_AK_ADD = 1 # how many points are earned just by being in chat
POINTS_AK_PERIOD = 20 # how many seconds apart the above is added

# points use
POINTS_USE = "drop" # user types !POINTS_USER with optional number

# response strings.
# the parts {like this} are replaced automatically. They don't need to be there though.

# using
POINTS_USED = "{username} drop {amountuserd} "+POINTS_NAME_PLURAL+" ooft"
POINT_USED = "{username} drop an "+POINTS_NAME

# giving and recieving
POINTS_BAD_FORMAT = "bad format !give request"
POINTS_GIFT_SELF = "can't give points to yourself"
POINTS_NOT_ENOUGH = "Not enough "+POINTS_NAME_PLURAL+" only {pointamount} left"
POINTS_CONFIRM = "user {giver} gave user {target} {amountgiven} of their "+POINTS_NAME_PLURAL
POINTS_BOT_RESPONSE = ". Ta babes <3"# added to the end of confirm string if user gave points to the bot
