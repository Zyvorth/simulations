import tkinter as tk
import random
from ESTAT_DUALCHARGE_BACK import *

# ---------------- ROOT ----------------

root = tk.Tk()

root.geometry("1400x900")
root.configure(bg="black")

# ---------------- BACKGROUND CANVAS ----------------

bg_canvas = tk.Canvas(
    root,
    width=1400,
    height=900,
    bg="black",
    highlightthickness=0
)

bg_canvas.place(x=0, y=0)

# ---------------- HEADER ----------------

title = tk.Label(
    root,
    text="ELECTROSTATIC PARTICLE SIMULATOR",
    fg="white",
    bg="black",
    font=("Courier New", 36, "bold underline")
)

title.place(relx=0.5, y=20, anchor="n")

creator = tk.Label(
    root,
    text="BY ZYVORTH_CORE",
    fg="white",
    bg="black",
    font=("Courier New", 22)
)

creator.place(relx=0.5, y=80, anchor="n")

# ---------------- INSTRUCTION ----------------

instruction = tk.Label(
    root,
    text="ENTER NUMBER OF POSITIVE AND NEGATIVE PARTICLES",
    fg="white",
    bg="black",
    font=("Courier New", 26)
)

instruction.place(relx=0.5, y=150, anchor="n")

# ---------------- POSITIVE INPUT ----------------

pos_label = tk.Label(
    root,
    text="POSITIVE PARTICLES",
    fg="white",
    bg="black",
    font=("Courier New", 16)
)

pos_label.place(relx=0.42, y=380, anchor="center")

pos_frame = tk.Frame(
    root,
    bg="white",
    width=180,
    height=40
)

pos_frame.place(relx=0.42, y=430, anchor="center")

pos_entry = tk.Entry(
    pos_frame,
    bg="black",
    fg="white",
    insertbackground="white",
    font=("Courier New", 16),
    relief="flat",
    bd=0,
    justify="center"
)

pos_entry.place(
    relx=0.5,
    rely=0.5,
    anchor="center",
    width=170,
    height=30
)

# ---------------- NEGATIVE INPUT ----------------

neg_label = tk.Label(
    root,
    text="NEGATIVE PARTICLES",
    fg="white",
    bg="black",
    font=("Courier New", 16)
)

neg_label.place(relx=0.58, y=380, anchor="center")

neg_frame = tk.Frame(
    root,
    bg="white",
    width=180,
    height=40
)

neg_frame.place(relx=0.58, y=430, anchor="center")

neg_entry = tk.Entry(
    neg_frame,
    bg="black",
    fg="white",
    insertbackground="white",
    font=("Courier New", 16),
    relief="flat",
    bd=0,
    justify="center"
)

neg_entry.place(
    relx=0.5,
    rely=0.5,
    anchor="center",
    width=170,
    height=30
)

# ---------------- SIMULATION FRAME ----------------

sim_frame = tk.Frame(
    root,
    bg="black",
    highlightbackground="white",
    highlightthickness=2
)

sim_frame.place_forget()

# ---------------- SIMULATION CANVAS ----------------

sim_canvas = tk.Canvas(
    sim_frame,
    width=1396,
    height=720,
    bg="black",
    highlightthickness=0
)

sim_canvas.place(x=0, y=0)

# ---------------- BACK BUTTON ----------------

back_button = tk.Label(
    sim_frame,
    text="BACK",
    fg="white",
    bg="#b30000",
    font=("Courier New", 14, "bold"),
    padx=25,
    pady=8,
    cursor="hand2"
)

back_button.place(
    relx=0.5,
    y=740,
    anchor="center"
)

# ---------------- PARTICLE DRAWINGS ----------------

particle_drawings = []

simulation_running = False

# ---------------- DRAW PARTICLES ----------------

def draw_particles():

    particle_drawings.clear()

    for particle in charge_inst:

        x = particle[0]
        y = particle[1]

        charge = particle[4]

        if charge == 1:
            color = "red"
        else:
            color = "cyan"

        obj = sim_canvas.create_oval(
            x - radius,
            y - radius,
            x + radius,
            y + radius,
            fill=color,
            outline=""
        )

        particle_drawings.append(obj)

# ---------------- UPDATE GRAPHICS ----------------

def update_graphics():

    global simulation_running

    if simulation_running == False:
        return

    # physics update from your core
    charge_pos_inst()

    # redraw particles

    for i in range(len(charge_inst)):

        x = charge_inst[i][0]
        y = charge_inst[i][1]

        sim_canvas.coords(
            particle_drawings[i],
            x - radius,
            y - radius,
            x + radius,
            y + radius
        )

    # ultra smooth refresh
    root.after(4, update_graphics)

# ---------------- START SIMULATION ----------------

def start_simulation(event=None):

    global simulation_running

    positive_particles = int(pos_entry.get())
    negative_particles = int(neg_entry.get())

    print("Positive:", positive_particles)
    print("Negative:", negative_particles)

    # show simulation frame

    sim_frame.place(
        x=0,
        y=120,
        width=1400,
        height=780
    )

    sim_frame.lift()

    # clear old simulation

    sim_canvas.delete("all")

    charge_inst.clear()

    particle_drawings.clear()

    # initialize particles using your core

    charge_initial(
        positive_particles,
        negative_particles
    )

    # draw particles

    draw_particles()

    # start simulation

    simulation_running = True

    update_graphics()

# ---------------- BACK FUNCTION ----------------

def go_back(event=None):

    global simulation_running

    simulation_running = False

    sim_frame.place_forget()

    sim_canvas.delete("all")

    charge_inst.clear()

    particle_drawings.clear()

# ---------------- BACK BUTTON EVENTS ----------------

back_button.bind("<Button-1>", go_back)

def back_enter(e):
    back_button.config(bg="#ff1a1a")

def back_leave(e):
    back_button.config(bg="#b30000")

back_button.bind("<Enter>", back_enter)
back_button.bind("<Leave>", back_leave)

# ---------------- START BUTTON ----------------

start_button = tk.Label(
    root,
    text="START",
    fg="white",
    bg="#b30000",
    font=("Courier New", 18, "bold"),
    padx=35,
    pady=12,
    cursor="hand2"
)

start_button.place(
    relx=0.5,
    y=560,
    anchor="center"
)

# ---------------- START BUTTON EVENTS ----------------

start_button.bind("<Button-1>", start_simulation)

def start_enter(e):
    start_button.config(bg="#ff1a1a")

def start_leave(e):
    start_button.config(bg="#b30000")

start_button.bind("<Enter>", start_enter)
start_button.bind("<Leave>", start_leave)

# ---------------- BACKGROUND PARTICLES ----------------

bg_particles = []

for _ in range(120):

    x = random.randint(0, 1400)
    y = random.randint(0, 900)

    vx = random.uniform(-1.5, 1.5)
    vy = random.uniform(-1.5, 1.5)

    size = random.randint(2, 5)

    particle = bg_canvas.create_oval(
        x,
        y,
        x + size,
        y + size,
        fill="white",
        outline=""
    )

    bg_particles.append([
        particle,
        vx,
        vy
    ])

# ---------------- BACKGROUND ANIMATION ----------------

def animate_background():

    for p in bg_particles:

        particle, vx, vy = p

        bg_canvas.move(
            particle,
            vx,
            vy
        )

        coords = bg_canvas.coords(particle)

        x1, y1, x2, y2 = coords

        if x1 <= 0 or x2 >= 1400:
            p[1] *= -1

        if y1 <= 0 or y2 >= 900:
            p[2] *= -1

    # ultra smooth refresh
    root.after(4, animate_background)

animate_background()

# ---------------- KEEP HEADER ABOVE FRAME ----------------

title.lift()
creator.lift()

# ---------------- MAIN LOOP ----------------

root.mainloop()
