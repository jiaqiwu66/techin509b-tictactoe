import csv
from prettytable import PrettyTable
import matplotlib.pyplot as plt

PATH = "./logs/log_two_player.csv"

x_win = 0
o_win = 0
draw = 0
total = 0

horizontal = 0
vertical = 0
diagonal = 0
total_winner = 0

win_step_5 = 0
win_step_6 = 0
win_step_7 = 0
win_step_8 = 0

corner = 0
side = 0
center = 0

CORNER = ['1', '3', '7', '9']
SIDE = ['2', '4', '6', '8']

with open(PATH, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[9] == 'X':
            x_win += 1
            if row[0] in CORNER:
                corner += 1
            elif row[0] == '5':
                center += 1
            elif row[0] in SIDE:
                side += 1
        elif row[9] == 'O':
            o_win += 1
        else:
            draw += 1

        pattern = row[10]
        if pattern != '':
            if pattern == 'H':
                horizontal += 1
            elif pattern == 'V':
                vertical += 1
            elif pattern == 'D':
                diagonal += 1
            total_winner += 1

            win_step = row[11]
            if win_step == '5':
                win_step_5 += 1
            elif win_step == '6':
                win_step_6 += 1
            elif win_step == '7':
                win_step_7 += 1
            elif win_step == '8':
                win_step_8 += 1
        total += 1


labels_1 = ["X Wins", "O Wins", "Draw"]
data_1 = [x_win, o_win, draw]
rates_1 = [round(x_win / total * 100, 2), round(o_win / total * 100, 2), round(draw / total * 100, 2)]

table_1 = PrettyTable(["Results", "Times", "Rate"])
for i in range(0, 3):
    table_1.add_row([labels_1[i], data_1[i], rates_1[i]])
table_1.add_row(["Total", total, 100.0])
print(table_1)
plt.pie(data_1, explode=(0, 0, 0.1), labels=labels_1, autopct='%1.2f%%', shadow=True, startangle=90, colors=['lightskyblue', 'yellowgreen', 'gold'])
plt.title("Results of TicTacToe")
plt.show()

labels_2 = ["Horizontal", "Vertical", "Diagonal"]
data_2 = [horizontal, vertical, diagonal]
rates_2 = [
    round(horizontal / total_winner * 100, 2),
    round(vertical / total_winner * 100, 2),
    round(diagonal / total_winner * 100, 2)
]

table_2 = PrettyTable(["Winner Pattern", "Times", "Rate"])
for i in range(0, 3):
    table_2.add_row([labels_2[i], data_2[i], rates_2[i]])
table_2.add_row(["Total", total_winner, 100.0])
print(table_2)
plt.pie(data_2, explode=(0.05, 0.05, 0.05), labels=labels_2, autopct='%1.2f%%', shadow=True, startangle=90, colors=['lightskyblue', 'yellowgreen', 'gold'])
plt.title("Results of Winning Patterns")
plt.show()

labels_3 = ["Step 5", "Step 6", "Step 7", "Step 8"]
data_3 = [win_step_5, win_step_6, win_step_7, win_step_8]
rates_3 = [
    round(win_step_5 / total_winner * 100, 2),
    round(win_step_6 / total_winner * 100, 2),
    round(win_step_7 / total_winner * 100, 2),
    round(win_step_8 / total_winner * 100, 2)
]

table_3 = PrettyTable(["Win Step", "Times", "Rate"])
for i in range(0, 4):
    table_3.add_row([labels_3[i], data_3[i], rates_3[i]])
table_3.add_row(["Total", total_winner, 100.0])
print(table_3)

plt.bar(labels_3, data_3, width=0.5)
plt.xlabel('winning steps')
plt.ylabel('times')
for a, b, i in zip(labels_3, data_3, range(len(labels_3))):
    plt.text(a, b+0.3, data_3[i], ha='center', fontsize=10)
plt.title("Results of Winning Steps")
plt.show()

labels_4 = ["Corner_position", "Side_position", "Center_position"]
data_4 = [corner, side, center]
rates_4 = [
    round(corner / x_win * 100, 2),
    round(side / x_win * 100, 2),
    round(center / x_win * 100, 2),
]
table_4 = PrettyTable(["First_step_position", "Times", "Rate"])
for i in range(0, 3):
    table_4.add_row([labels_4[i], data_4[i], rates_4[i]])
table_4.add_row(["Total", x_win, 100.0])
print(table_4)

plt.pie(data_4, explode=(0.05, 0.05, 0.05), labels=labels_4, autopct='%1.2f%%', shadow=True, startangle=90, colors=['lightskyblue', 'yellowgreen', 'gold'])
plt.title("First Step of X_Winner")
plt.show()