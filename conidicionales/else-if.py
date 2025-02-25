ingreso_mensual=1000000
gasto=506789780
if ingreso_mensual>10000:
    print("Estas bien en cualquier parte del mundo")
    if ingreso_mensual-gasto>100:
        print("Muerte")
    elif ingreso_mensual-gasto<100:
        print("Vida")
elif ingreso_mensual>1000:
    print("Estas bien en latam")
else:
    print("Sos pobre")