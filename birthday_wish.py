import turtle
import time
import pyttsx3 # TTS লাইব্রেরি

# --- ১. টেক্সট-টু-স্পিচ (TTS) ফাংশন ---
def speak_wish(text):
    """প্রদত্ত টেক্সটটিকে ভয়েসে প্লে করে।"""
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"TTS Error: Could not initialize pyttsx3. {e}")
        print("Continuing with only graphics...")

# --- ২. টার্টল সেটআপ ও মৌলিক ফাংশন ---
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#000033")
screen.title("🎉 Happy Birthday Animation 🥳🎉")
turtle.hideturtle()
turtle.speed(0)

cake_builder = turtle.Turtle()
cake_builder.hideturtle()
cake_builder.speed(0)

def draw_cake_part(t, x, y, width, height, color):
    """কেকের একটি আয়তাকার অংশ আঁকে এবং রঙ করে।"""
    t.penup()
    t.goto(x - width/2, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# --- ৩. অ্যানিমেশন লজিক: কেক বিল্ড করা ---

def animate_cake_drop(part_color, start_y, end_y, layer_height):
    """কেকের অংশকে উপর থেকে নিচে পড়ার অ্যানিমেশন দেখায়।"""
    drop_turtle = turtle.Turtle()
    drop_turtle.hideturtle()
    drop_turtle.speed(0)
    cake_width = 200
    x_center = 0
    
    drop_turtle.penup()
    drop_turtle.goto(x_center - cake_width/2, start_y)
    
    for current_y in range(start_y, end_y, -10):
        drop_turtle.clear()
        draw_cake_part(drop_turtle, x_center, current_y, cake_width, layer_height, part_color)
        screen.update()
        time.sleep(0.02)
        
    draw_cake_part(cake_builder, x_center, end_y, cake_width, layer_height, part_color)
    drop_turtle.clear()

# --- ৪. মোমবাতি এবং আগুন লজিক ---

def draw_candle_and_fire(x, y):
    """কেকের উপর মোমবাতি ও আগুন জ্বলার প্রভাব দেখায়।"""
    candle = turtle.Turtle()
    candle.hideturtle()
    candle.penup()
    draw_cake_part(candle, x, y + 5, 10, 30, "red") 
    
    for _ in range(5):
        # সলতে
        candle.goto(x, y + 35)
        candle.color("gray")
        candle.pensize(2)
        candle.pendown()
        candle.setheading(90)
        candle.forward(5)
        
        # আগুনের শিখা (ফ্লিকারিং)
        fire = turtle.Turtle()
        fire.hideturtle()
        fire.penup()
        fire.goto(x, y + 40)
        fire.begin_fill()
        
        fire_color = "yellow" if _ % 2 == 0 else "orange"
        fire.fillcolor(fire_color)
        
        # ত্রিভুজ আকৃতির শিখা
        fire.pendown()
        fire.setheading(60)
        fire.forward(10)
        fire.setheading(180)
        fire.forward(10)
        fire.setheading(-60)
        fire.forward(10)
        
        fire.end_fill()
        screen.update()
        time.sleep(0.15)
        
        fire.clear()
        candle.clear()
        draw_cake_part(candle, x, y + 5, 10, 30, "red") # মোমবাতি আবার আঁকা

# --- ৫. মূল প্রোগ্রাম লজিক ---

def run_birthday_animation():
    
    screen.tracer(0) 

    # --- কেক তৈরি ---
    base_y = -100
    layer_height = 40
    
    animate_cake_drop("skyblue", 300, base_y, layer_height)
    animate_cake_drop("white", 350, base_y + layer_height, layer_height)
    animate_cake_drop("pink", 400, base_y + 2 * layer_height, layer_height)
    
    draw_cake_part(cake_builder, 0, base_y + 3 * layer_height, 200, 10, "gold")
    screen.update()
    time.sleep(0.5)

    # --- মোমবাতি এবং আগুন ---
    candle_y_start = base_y + 3 * layer_height + 10
    time.sleep(1)
    draw_candle_and_fire(0, candle_y_start)
    screen.update()
    time.sleep(0.5)

    # --- শুভেচ্ছা টেক্সট এবং ভয়েস ---
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.penup()
    text_turtle.goto(0, 150)
    text_turtle.color("yellow")
    
    wish_text = "Happy Birthday! Wishing you all the best on your special day."
    
    for char in wish_text:
        text_turtle.write(char, move=True, font=("Courier", 20, "bold"))
        screen.update()
        time.sleep(0.05)
        
    speak_wish(wish_text)
    
    screen.mainloop()

if __name__ == "__main__":
    run_birthday_animation()
