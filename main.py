from titanic_eu.eu import eu
from titanic_ru.ru import ru

if __name__ != "__main__":
    pass
else:

    dev = False

    print("╔═══════════════════════════════════════════╗")
    print("╠═══════════════════ EU ════════════════════╣")
    print("╚═══════════════════════════════════════════╝")
    eu(dev)

    if dev:
        print("(・_・) (・_・) (・_・) (・_・) (・_・) (・_・) (・_・) (・_・)")
        print("(・_・) (・_・) (・_・) (・_・) (・_・) (・_・) (・_・) (・_・)")
        print("(・_・) (・_・) (・_・) (・_・) (・_・) (・_・) (・_・) (・_・)")

    print("╔═══════════════════════════════════════════╗")
    print("╠═══════════════════ RU ════════════════════╣")
    print("╚═══════════════════════════════════════════╝")
    ru(dev)

    if dev:
        print("(・_・) (・_・) (・_・) (・_・) (・_・) (・_・) (・_・) (・_・)")
        print("(・_・) (・_・) (・_・) (・_・) (・_・) (・_・) (・_・) (・_・)")
        print("(・_・) (・_・) (・_・) (・_・) (・_・) (・_・) (・_・) (・_・)")
