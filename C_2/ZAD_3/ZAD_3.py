print("ZAD_3▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")

iloscODP = 0
print()
print("\nOdpowiadamy '+' lub '-' jeżeli dochodzisz do pytania '- Moja odpowiedz' piszesz wszystko co chcesz")
with open("TEST.txt") as f:
    with open("answer.txt", "w") as f_out:
        for line in f:
            if line.startswith("    -*"):

                if iloscODP == 0:
                    print("- Moja odpowiedz")
                    answer = input("> ")
                    f_out.write("   - Moja odpowiedz: " + answer + "\n")
                else:
                    continue

            elif line.startswith("    -"):
                print("- " + line.strip()[2:])
                answer = input("> ")

                if iloscODP == 0 and answer == "+":
                    f_out.write("   - " + line.strip()[2:] + "\n")
                    iloscODP += 1
                elif iloscODP != 0 and answer == "+":
                    f_out.write("   - " + line.strip()[2:] + "\n")
                else:
                    continue
            elif line.startswith("     "):
                iloscODP = 0
                continue
            else:
                f_out.write(line.strip() + "\n")
                print("\n▓▓▓▓▒▒▒░░  " + line.strip() + "  ░░▒▒▒▓▓▓▓")
                print()

