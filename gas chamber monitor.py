"""Gas chamber pressure monitor

Fixed issues from original script:
- Input validation for numeric values
- Avoid shadowing built-ins (no variable named `list`)
- Handle V - n*b <= 0 safely for van der Waals
- Clear, formatted output with units
- Optional plot of Pressure vs Temperature using matplotlib (if available)
- Better variable names and messages
"""

import sys

try:
    import matplotlib.pyplot as plt
    _HAS_MPL = True
except Exception:
    _HAS_MPL = False


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid input — please enter a numeric value.")


def get_choice(prompt, choices):
    choices = [c.lower() for c in choices]
    while True:
        choice = input(prompt).strip().lower()
        if choice in choices:
            return choice
        print(f"Please choose one of: {', '.join(choices)}")


def monitor_pressure(n_moles, volume_l, gas_type, a=3.592, b=0.04267):
    """Compute pressure (atm) for temperatures 0..100 °C in steps of 10 °C.

    Returns a list of (T_C, pressure_atm) tuples. Stops early if a critical pressure is detected
    or if van der Waals denominator becomes non-positive.
    """
    R = 0.082057366  # L·atm·K⁻1·mol⁻1
    temps_C = list(range(0, 101, 10))
    results = []

    for T_C in temps_C:
        T_K = T_C + 273.15
        if gas_type == 'ideal':
            pressure = (n_moles * R * T_K) / volume_l
        else:  # real gas (van der Waals)
            denom = volume_l - (n_moles * b)
            if denom <= 0:
                print(f"At {T_C} °C: invalid volume for van der Waals correction (V - n*b = {denom:.6f} L). Aborting calculation.")
                break
            pressure = ((n_moles * R * T_K) / denom) - ((a * (n_moles ** 2)) / (volume_l ** 2))

        results.append((T_C, pressure))

        # Messages and thresholds (pressures in atm)
        if pressure < 1.0:
            print(f"{T_C:3d} °C: {pressure:8.4f} atm — Low vacuum pressure detected")
        elif 1.0 <= pressure <= 12.0:
            print(f"{T_C:3d} °C: {pressure:8.4f} atm")
        else:  # pressure > 12.0
            print(f"{T_C:3d} °C: {pressure:8.4f} atm — HIGH CRITICAL PRESSURE detected. Stopping monitor.")
            break

    return results


def main():
    print("Gas chamber pressure monitor — pressures are computed in atm (R = 0.08206 L·atm·mol⁻1·K⁻1)")

    n_moles = get_positive_float("Enter the initial number of moles: ")
    volume_l = get_positive_float("Enter the volume in litres: ")
    gas_type = get_choice("Choose the target gas model ('ideal' or 'real'): ", ['ideal', 'real'])

    # Optionally allow user to override a and b for real gas
    if gas_type == 'real':
        use_defaults = get_choice("Use default van der Waals constants a=3.592, b=0.04267? (yes/no): ", ['yes', 'no'])
        if use_defaults == 'no':
            a_val = get_positive_float("Enter van der Waals constant a (L^2·atm·mol^-2): ")
            b_val = get_positive_float("Enter van der Waals constant b (L·mol^-1): ")
        else:
            a_val, b_val = 3.592, 0.04267
    else:
        a_val, b_val = None, None

    results = monitor_pressure(n_moles, volume_l, gas_type, a=a_val if a_val is not None else 0.0, b=b_val if b_val is not None else 0.0)

    # Plot results if matplotlib is available
    if _HAS_MPL and results:
        temps, pressures = zip(*results)
        plt.figure()
        plt.plot(temps, pressures, marker='o')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Pressure (atm)')
        plt.title(f'Pressure vs Temperature ({gas_type} gas)')
        plt.grid(True)
        plt.tight_layout()
        try:
            plt.show()
        except Exception:
            # In some headless environments showing may fail — save to file instead
            out_file = 'pressure_vs_temperature.png'
            plt.savefig(out_file)
            print(f'Plot saved to {out_file}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nAborted by user')
        sys.exit(1)
