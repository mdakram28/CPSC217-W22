import discord
import math

client = discord.Client()

#Change your token you got from the first part of the assignment here.
TOKEN = ""

xc = -1.0
yc = -1.0
r = -1.0
x1 = -1.0
y1 = -1.0
x2 = -1.0
y2 = -1.0

numberOfIntersectionPoints = 0
xIntersectionPointOne = -1.0
yIntersectionPointOne = -1.0
xIntersectionPointTwo = -1.0
yIntersectionPointTwo = -1.0

#
def solveEquation():
    # Do NOT change anything from lines 28-40!
    # This is just the starter code and you do not need to understand what is going on here.
    # Unless you are curious, of course.
    global numberOfIntersectionPoints
    global xIntersectionPointOne
    global yIntersectionPointOne
    global xIntersectionPointTwo
    global yIntersectionPointTwo

    global xc
    global yc
    global r
    global x1
    global y1
    global x2
    global y2
    #Students, you write your code starting from here! Make sure your indentation is in line with lines 28-40

    print(f"xc = {xc}")
    print(f"yc = {yc}")
    print(f"r  = {r}")
    print(f"x1 = {x1}")
    print(f"y1 = {y1}")
    print(f"x2 = {x2}")
    print(f"y2 = {y2}")

    # if discriminant > 0
        # Calculate alpha1 and alpha2
    # else if discriminant = 0
        # Calculate alpha 1
    # else if discriminant < 0
        # Do nothing
    # else something is wrong

    # set numberOfIntersectionPoints -> 0
    # if alpha1 is b/w 0 and 1
        # Add 1 to numberOfIntersectionPoints
        # calculate 1st intersection point
    # if alpha2 is b/w 0 and 1
        # Add 1 to numberOfIntersectionPoints
        # calculate 2nd intersection point

###
# Do NOT change anything below here!
# This is just the starter code and you do not need to understand what is going on here.
# Unless you are curious, of course.
###
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$xc'):
        global xc
        xc = message.content.split("=")[1].strip()
        sendMessageToUser = "Your xc coord is: " + xc
        await message.channel.send(sendMessageToUser)

    if message.content.startswith('$yc'):
        global yc
        yc = message.content.split("=")[1].strip()
        sendMessageToUser = "Your yc coord is: " + yc
        await message.channel.send(sendMessageToUser)

    if message.content.startswith('$r'):
        global r
        r = message.content.split("=")[1].strip()
        sendMessageToUser = "Your r coord is: " + r
        await message.channel.send(sendMessageToUser)

    if message.content.startswith('$x1'):
        global x1
        x1 = message.content.split("=")[1].strip()
        sendMessageToUser = "Your x1 coord is: " + x1
        await message.channel.send(sendMessageToUser)

    if message.content.startswith('$y1'):
        global y1
        y1 = message.content.split("=")[1].strip()
        sendMessageToUser = "Your y1 coord is: " + y1
        await message.channel.send(sendMessageToUser)

    if message.content.startswith('$x2'):
        global x2
        x2 = message.content.split("=")[1].strip()
        sendMessageToUser = "Your x2 coord is: " + x2
        await message.channel.send(sendMessageToUser)

    if message.content.startswith('$y2'):
        global y2
        y2 = message.content.split("=")[1].strip()
        sendMessageToUser = "Your y2 coord is: " + y2
        await message.channel.send(sendMessageToUser)

    if message.content.startswith('$solve equation'):
        solveEquation()
        sendMessageToUser = "Equation solved, based on your algorithm 😉. Type **$show results** to see your results!"
        await message.channel.send(sendMessageToUser)

    if message.content.startswith('$show results'):
        sendMessageToUserNumberOfIntersections = "There are " + str(numberOfIntersectionPoints) + " total number of intersection points. \n"
        sendMessageToUserFirstIntersectionCoordinates = "The first intersection coordinates are ({:.2f},{:.2f}) \n".format(xIntersectionPointOne, yIntersectionPointOne)
        sendMessageToUserSecondIntersectionCoordinates = "The second intersection coordinates are ({:.2f},{:.2f}) \n".format(xIntersectionPointTwo, yIntersectionPointTwo)
        sendMessageToUser = sendMessageToUserNumberOfIntersections + sendMessageToUserFirstIntersectionCoordinates + sendMessageToUserSecondIntersectionCoordinates
        await message.channel.send(sendMessageToUser)

client.run(TOKEN)


