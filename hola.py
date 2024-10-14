paises=[["españa",47000000],
        ["Alemania",77000000],
        ["Italia",40000000]]

for pais in paises:
    for datos in pais:
        if isinstance(datos,int):
            print(datos)


