from console import *
from logic import *

def main():
    ascii_logo()

    welcome_message()

    pause()

    model = select_model()

    user_inputs = get_user_inputs()

    pause("Calculating forward padding...Press Enter to continue...")

    install_message()

    while True:
        if user_inputs.low_input > user_inputs.high_input:
            result = calculate_equalizer_with_pad(model, user_inputs)
        elif user_inputs.high_input > user_inputs.low_input:
            result = calculate_simulator_with_pad(model, user_inputs)
        else:
            print("Tilt already flat, proceed to padding")
            exit()

        print(
            f"{result['device']} -> {result['key']}, "
            f"Pad -> {result['pad']}, "
        )
        print(
            f"Raw Outputs: ('Ch.98 output: {result['low_final']:.1f}, "
            f"Ch.110 output: {result['high_final']:.1f}')"
        )
        break

    short_pause()

    balance_forward_message()

    short_pause()

    manual_message()

    short_pause()

    adu_message()

    pause("Calculating reverse padding...Press Enter to continue...")

    balance_return_message()

    return_pad, return_output = select_return_pad(
        user_inputs.reverse_input,
        model.gain_reverse
    )

    print(f"Return Pad -> {return_pad} dB")
    print(f"Raw Outputs: ('Return output: {return_output:.1f}')")

    sre_message()


if __name__ == "__main__":
    main()












