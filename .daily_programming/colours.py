#day 4

colours = ["red"]
for i in colours[:]: #eine Kopie der Liste colours wird durch Slicing erstellt (colours[:])
    if i == "red":
        colours += ["black"]
    if i == "black":
        colours += ["white"]
print(colours)
# ---> die Schleife wird nicht von den Änderungen beeinflusst ,die während der Iteration vorgenommen werden, da nur die Kopie der Liste betrachtet wird.
# die Ausgabe ist somit ['red', 'black'], da das Element "black" während der Iteration nicht zur Liste hinzugefügt wird und somit die Bedingung nicht gegeben ist, um "white" zur Liste anzuhängen

#VS

colours = ["red"]
for i in colours:
    if i == "red":
        colours += ["black"]
    if i == "black":
        colours += ["white"]
print(colours)
# ---> die Schleife wird von den Änderungen beeinflusst, die während der Iteration vorgenommen werden, da die originale Liste betrachtet wird 
# Die Schleife durchläuft jedes Element in der Liste, einschließlich derjenigen, die während der Iteration hinzugefügt wurden. Dies führt dazu, dass auch das Element "white" zur Liste hinzugefügt wird. Daher lautet die endgültige Ausgabe ['red', 'black', 'white'].