from typing import Union
from data import *
from models import *

#function for selecting amplifier model

def select_model() -> Union[LineExtender, MiniBridger]:
    choice = input('Enter 1 for BLE120, 2 for MB120: ').strip()
    if choice == '1':
        return LineExtender()
    elif choice =='2':
        return MiniBridger()
    else:
        return LineExtender()

#function for collecting user inputs

def get_user_inputs() -> UserInputs:
    user_low = float(input("Enter level @ Ch.98: "))
    user_high = float(input("Enter level @ Ch.110: "))
    user_reverse = float(input("Enter TX level: "))

    return UserInputs(
        low_input = user_low,
        high_input = user_high,
        reverse_input = user_reverse
    )

#function for calculating raw outputs - before padding or equalization

def raw_output(model: Union[LineExtender, MiniBridger], user: UserInputs) -> tuple:
    low_out_raw = user.low_input + model.gain_low
    high_out_raw = user.high_input + model.gain_high
    reverse_out_raw = user.reverse_input - model.gain_reverse

    return (
        f'Ch.98 output: {low_out_raw}',
        f'Ch.110 output: {high_out_raw}',
        f'Return output: {reverse_out_raw}'
    )

#functions for "flattening" inputs and padding as close as possible

def calculate_equalizer_with_pad(
    model: Union[LineExtender, MiniBridger],
    user: UserInputs
) -> dict:
    """
    Selects equalizer AND pad to hit target outputs.
    """

    # Step 1: pick EQ key that best flattens
    best_key = min(
        equalizer_lowband,
        key=lambda k: abs(
            (user.high_input - equalizer_highband[k]) -
            (user.low_input - equalizer_lowband[k])
        )
    )

    # Step 2: apply EQ
    low_after_eq = user.low_input - equalizer_lowband[best_key]
    high_after_eq = user.high_input - equalizer_highband[best_key]

    # Step 3: apply amplifier gain
    low_raw = low_after_eq + model.gain_low
    high_raw = high_after_eq + model.gain_high

    # Step 4: select pad
    pad_result = select_pad(low_raw, high_raw)
    if pad_result is None:
        return {"device": "Equalizer", "key": best_key, "message": "No valid pad"}

    pad, low_final, high_final = pad_result

    return {
        "device": "Equalizer",
        "key": best_key,
        "pad": pad,
        "low_final": low_final,
        "high_final": high_final
    }

def calculate_simulator_with_pad(
    model: Union[LineExtender, MiniBridger],
    user: UserInputs
) -> dict:
    """
    Selects simulator AND pad to hit target outputs.
    """

    # Step 1: pick SIM key that best flattens
    best_key = min(
        simulator_highband,
        key=lambda k: abs(
            (user.high_input - simulator_highband[k]) -
            (user.low_input - simulator_lowband[k])
        )
    )

    # Step 2: apply simulator
    low_after_sim = user.low_input - simulator_lowband[best_key]
    high_after_sim = user.high_input - simulator_highband[best_key]

    # Step 3: apply amplifier gain
    low_raw = low_after_sim + model.gain_low
    high_raw = high_after_sim + model.gain_high

    # Step 4: select pad
    pad_result = select_pad(low_raw, high_raw)
    if pad_result is None:
        return {"device": "Simulator", "key": best_key, "message": "No valid pad"}

    pad, low_final, high_final = pad_result

    return {
        "device": "Simulator",
        "key": best_key,
        "pad": pad,
        "low_final": low_final,
        "high_final": high_final
    }

#function for padding
def select_pad(
    low_raw: float,
    high_raw: float,
    low_target: float = 33.0,
    high_target: float = 43.0,
    low_tolerance: float = 3.0,
    pad_range=range(0, 24)
) -> tuple | None:
    """
    Selects flat pad prioritizing HIGH channel accuracy.
    Low must be within tolerance.
    """

    candidates = []

    for pad in pad_range:
        low_final = low_raw - pad
        high_final = high_raw - pad

        low_err = abs(low_final - low_target)
        high_err = abs(high_final - high_target)

        if low_err <= low_tolerance:
            candidates.append((high_err, low_err, pad, low_final, high_final))

    if not candidates:
        return None

    _, _, pad, low_final, high_final = min(candidates)
    return pad - 4, low_final, high_final

#function for return equalization and padding

def select_return_pad(
    user_reverse: float,
    reverse_gain: float,
    target_reverse: float = 38.0
) -> tuple[int, float]:
    reverse_raw = user_reverse - reverse_gain
    pad = max(0, int(round(target_reverse - reverse_raw)))
    reverse_final = reverse_raw + pad

    return pad, reverse_final


















