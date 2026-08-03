"""
pressure of gas calculator using ideal gas law and van der Waals correction

This script prompts for mass, molar mass, temperature, volume, and van der Waals
constants to compute the pressure of a gas using both the ideal gas law and the
van der Waals equation (real gas). It includes input validation and clearer
prompts and messages.

Units expected:
 - mass: grams (g)
 - molar mass: grams per mole (g/mol)
 - temperature: degrees Celsius (°C) (converted to Kelvin internally)
 - volume: litres (L)
 - R: ideal gas constant in atm·L/(mol·K). Default: 0.082057 (press Enter to use default)
 - a: van der Waals constant a (units consistent with atm·L^2/mol^2)
 - b: van der Waals constant b (L/mol)

Example defaults for common gases can be looked up if needed.
"""

from typing import Optional

DEFAULT_R = 0.082057  # atm·L/(mol·K)


def prompt_float(prompt: str, default: Optional[float] = None, min_value: Optional[float] = None) -> float:
    """Prompt until a valid float is given. If default is provided, pressing Enter returns it."""
    while True:
        if default is None:
            value = input(prompt).strip()
        else:
            value = input(f"{prompt} [default: {default}] ").strip()
            if value == "":
                return default
        try:
            f = float(value)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if min_value is not None and f < min_value:
            print(f"Value must be >= {min_value}.")
            continue
        return f


def prompt_yes_no(prompt: str) -> bool:
    """Prompt until user enters yes or no. Returns True for yes."""
    while True:
        r = input(prompt + " (yes/no): ").strip().lower()
        if r in ("yes", "y"):
            return True
        if r in ("no", "n"):
            return False
        print("Please answer 'yes' or 'no'.")


def compute_ideal_pressure(n_moles: float, R: float, T_kelvin: float, V_liters: float) -> float:
    return (n_moles * R * T_kelvin) / V_liters


def compute_vdw_pressure(n: float, R: float, T: float, V: float, a: float, b: float) -> Optional[float]:
    """Compute van der Waals pressure. Returns None if volume correction invalid."""
    denom = V - n * b
    if denom <= 0:
        return None
    return (n * R * T) / denom - (a * n ** 2) / (V ** 2)


def main():
    print("Pressure of Gas Calculator (Ideal gas law and van der Waals correction)")
    user = input("What is your name? ").strip()
    gas = input("Which gas are you calculating for? ").strip()

    mass = prompt_float("Mass (g): ", min_value=0.0)
    molar_mass = prompt_float("Molar mass (g/mol): ", min_value=1e-12)
    n = mass / molar_mass
    print(f"Moles of {gas}: {n:.6g} mol")

    R = prompt_float("Ideal gas constant R in atm·L/(mol·K) — press Enter for default", default=DEFAULT_R)
    temp_c = prompt_float("Temperature (°C): ")
    T = temp_c + 273.15
    if T <= 0:
        print("Warning: temperature in Kelvin <= 0 — results may be invalid.")

    V = prompt_float("Volume (L): ", min_value=1e-12)

    P_ideal = compute_ideal_pressure(n, R, T, V)
    print(f"Ideal gas pressure for {gas}: {P_ideal:.6g} atm")

    print("Now enter van der Waals constants a and b (or press Enter for 0)")
    a = prompt_float("a (units: atm·L^2/mol^2): ", default=0.0)
    b = prompt_float("b (units: L/mol): ", default=0.0)

    P_vdw = compute_vdw_pressure(n, R, T, V, a, b)
    if P_vdw is None:
        print("Real (van der Waals) pressure could not be computed because V - n*b <= 0.")
    else:
        print(f"Real (van der Waals) pressure for {gas}: {P_vdw:.6g} atm")

    if P_vdw is not None:
        if prompt_yes_no("Do you want to calculate the percentage difference between ideal and real pressure?"):
            abs_diff = abs(P_ideal - P_vdw)
            # relative to ideal and to real (avoid division by zero)
            rel_to_ideal = abs_diff / abs(P_ideal) * 100 if abs(P_ideal) > 0 else float('inf')
            rel_to_real = abs_diff / abs(P_vdw) * 100 if abs(P_vdw) > 0 else float('inf')
            print(f"Absolute difference: {abs_diff:.6g} atm")
            if rel_to_ideal != float('inf'):
                print(f"Percentage difference relative to ideal pressure: {rel_to_ideal:.6g}%")
            else:
                print("Ideal pressure is zero, cannot compute percentage relative to ideal.")
            if rel_to_real != float('inf'):
                print(f"Percentage difference relative to real pressure: {rel_to_real:.6g}%")
            else:
                print("Real pressure is zero, cannot compute percentage relative to real.")

    print(f"Thank you, {user}! Goodbye.")


if __name__ == "__main__":
    main()
