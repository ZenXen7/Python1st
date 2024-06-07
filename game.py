import tkinter as tk

storage = tk.Tk()
storage.geometry('900x600')
storage.title("Tic Tac Toe - Gay Sex Game")

tk.Label(storage, text="Gay Sex Game", font=('ariel', 45, ), fg='red').pack()
tk.Label(storage, text="Tic-Tac-Toe", font=('Ariel', 25)).pack()
status_label = tk.Label(storage, text="X's turn", font=('Ariel', 15), bg='blue', fg='snow')
status_label.pack(fill=tk.X)
def playAgain():
    global currentChar
    currentChar = 'X'
    for point in xoPointCountr:
        point.button.configure(state=tk.NORMAL)
        point.reset()
    status_label.configure(text="X's turn")
    playAgain.pack_forget()
playAgain = tk.Button(storage, text='Play again', font=('Ariel', 15), fg='red', command=playAgain)

currentChar = "X"

play_area = tk.Frame(storage, width=500, height=300, bg='white')
xoPointCountr = []
xPointCountr = []
oPointCountr = []
class XOPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = tk.Button(play_area, text="", width=10, height=5, command=self.set)
        self.button.grid(row=x, column=y)

    def set(self):
        global currentChar
        if not self.value:
            self.button.configure(text=currentChar, bg='snow', fg='black')
            self.value = currentChar
            if currentChar == "X":
                xPointCountr.append(self)
                currentChar = "O"
                status_label.configure(text="O's turn")
            elif currentChar == "O":
                oPointCountr.append(self)
                currentChar = "X"
                status_label.configure(text="X's turn")
        check_win()

    def reset(self):
        self.button.configure(text="", bg='lightgray')
        if self.value == "X":
            xPointCountr.remove(self)
        elif self.value == "O":
            oPointCountr.remove(self)
        self.value = None
for x in range(1, 4):
    for y in range(1, 4):
        xoPointCountr.append(XOPoint(x, y))
class WinningPossibility:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def check(self, for_chr):
        p1_satisfied = False
        p2_satisfied = False
        p3_satisfied = False
        if for_chr == 'X':
            for point in xPointCountr:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        elif for_chr == 'O':
            for point in oPointCountr:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        return all([p1_satisfied, p2_satisfied, p3_satisfied])
winning_possibilities = [
    WinningPossibility(1, 1, 1, 2, 1, 3),
    WinningPossibility(2, 1, 2, 2, 2, 3),
    WinningPossibility(3, 1, 3, 2, 3, 3),
    WinningPossibility(1, 1, 2, 1, 3, 1),
    WinningPossibility(1, 2, 2, 2, 3, 2),
    WinningPossibility(1, 3, 2, 3, 3, 3),
    WinningPossibility(1, 1, 2, 2, 3, 3),
    WinningPossibility(3, 1, 2, 2, 1, 3)
]
def disable_game():
    for point in xoPointCountr:
        point.button.configure(state=tk.DISABLED)
    playAgain.pack()
def check_win():
    for possibility in winning_possibilities:
        if possibility.check('X'):
            status_label.configure(text="Result: X won!")
            disable_game()
            return
        elif possibility.check('O'):
            status_label.configure(text="Result: O won!")
            disable_game()
            return
    if len(xPointCountr) + len(oPointCountr) == 9:
        status_label.configure(text="Result: Draw!")
        disable_game()
play_area.pack(pady=10, padx=10)

storage.mainloop()