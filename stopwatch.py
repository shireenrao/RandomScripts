# "Stopwatch: The Game"
import simplegui

# define global variables
t = 550
score_comp = 0
score_player = 0
play_stop = 0

control = 0


# counting tenths of seconds into formatted string A:BC.D
def format(t):
    D = str(((t%600)%100)%10)
    C = str(int(((t%600)%100)/10))
    B = str(int((t%600)/100))
    A = str(int(t/600))
    # make formatted string A:BC.D
    format_time = A + ":" + B + C + "." + D
    return format_time


# define draw method
def draw(canvas):
    canvas.draw_text(format(t), (90, 120), 40, "Green")
    canvas.draw_text(str(score_player) + "/" + str(score_comp), (230, 30), 20, "Red")


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global control
    timer.start()
    #variable control is used to prevent cheating incase you multiple press the Stop button
    control = 1

def stop():
    timer.stop()
    global score_player, score_comp, control
    d = ((t%600)%100)%10
    if ((d == 0) and (control == 1)):
        score_player += 1
        control = 0
    elif ((d != 0) and (control == 1)):
        score_comp += 1
        control = 0
    
def reset():
    global t, score_player, score_comp
    t = 0
    score_player = 0
    score_comp = 0


# define event handler for timer with 0.1 sec interval
def time_handler():
    global t
    # every 100ms increase variable t
    t  += 1

# create frame
frame = simplegui.create_frame("Frame", 300, 200)
  
# register event handlers
timer = simplegui.create_timer(100, time_handler)
frame.set_draw_handler(draw)

frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()



