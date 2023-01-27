# Collatz Conjecture Data Visualization Program
# Developed by Hunter Mailloux, January 27th 2023
import plotly.express as px
import pandas as pd

def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        sequence.append(n)
    return sequence

number = int(input("Enter a number: "))
result = collatz(number)

xArray = []
iteration = 1

for i in result:
    xArray.append(iteration)
    iteration += 1

df = pd.DataFrame(dict(
    NodeNumber = xArray,
    Value = result
))

fig = px.line(df, x="NodeNumber", y="Value", title="Visual Representation of the Collatz Conjecture by Hunter Mailloux", markers=True).update_layout(xaxis_title="Number of Nodes", yaxis_title="Value of Node")
fig.show()