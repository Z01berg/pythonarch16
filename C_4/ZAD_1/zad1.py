
def panel_calc(dl_pod, sz_pod, dl_panel, sz_panel, ilosc_paneli_w_opakowaniu):
    p_pomiesz = dl_pod * sz_pod * 1.1

    p_panel = dl_panel * sz_panel

    ilosc_panel = p_pomiesz / p_panel

    ilosc_opakowan = ilosc_panel / ilosc_paneli_w_opakowaniu * 1.1
    return round(ilosc_opakowan)

print("Potrzeba : " + str(panel_calc(4, 4, 0.20, 1, 10)))