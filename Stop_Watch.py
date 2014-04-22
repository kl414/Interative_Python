# template for "Stopwatch: The Game"

# define global variables
import simplegui
curr_time = 0
whole_second = 0
total_stop = 0
flag = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    #A:BC.D
    D = t % 10
    C = t / 10 % 10
    B = t / 100 % 6
    A = t / 600
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer, flag
    timer.start()
    flag = 1

def stop():
    global timer, whole_second, total_stop, curr_time, flag
    timer.stop()
    if flag != 0:
        if curr_time % 10 == 0:
            whole_second += 1
        total_stop += 1
        flag = 0
    
def reset():
    global timer, curr_time, flag
    global whole_second, total_stop
    timer.stop()
    curr_time = 0
    whole_second = 0
    total_stop = 0
    flag = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global curr_time
    curr_time+=1

# define draw handler
def draw_handler(canvas):
    global curr_time, whole_second, total_stop
    text = format(curr_time)
    canvas.draw_text(text, [150, 140], 40, "White")
    canvas.draw_text(str(whole_second) + "/" + str(total_stop),\
                     [310, 30], 30, "Green")
    
# create frame
frame = simplegui.create_frame("StopWatch", 400, 300)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)
# start frame
frame.start()

# Please remember to review the grading rubric
