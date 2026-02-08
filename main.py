from console import *
from logic import *

def main():
    ascii_logo()
    welcome_message()

    model = select_model()
    user_inputs = get_user_inputs()

    print(f'Raw Outputs: {raw_output(model, user_inputs)}')

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
            f"Ch.98 {result['low_final']:.1f}, "
            f"Ch.110 {result['high_final']:.1f}"
        )
        break

    balance_message()
    adu_message()
    balance_return_message()

if __name__ == "__main__":
    main()












