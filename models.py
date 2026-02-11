from dataclasses import dataclass

#dataclasses for amplifier models
#BLE --> https://webresources.commscope.com/download/assets/STARLINE+BLE120+1.2+GHz+Line+Extender+Data+Sheet/4f6f75863bd611f08ac4faa31792deb3
#MB --> https://webresources.commscope.com/download/assets/STARLINE+MB120+1.2+GHz+Mini-Bridger+Amplifier+Data+Sheet/a1e0519e3bd811f0b9411adcaa92e24e
@dataclass
class LineExtender:
    gain_low: float = 32.30
    gain_high: float = 38.90
    gain_reverse: float = 17.30
    adu_backoff: float = 4.50
    name: str = 'BLE120'
    target_input: float = 12.00

@dataclass
class MiniBridger:
    gain_low: float = 36.00
    gain_high: float = 46.30
    gain_reverse: float = 17.50
    adu_backoff: float = 4.50
    name: str = "MB120"
    target_input: float = 6.00


#dataclass for system inputs, from user
@dataclass
class UserInputs:
    low_input: float
    high_input: float
    reverse_input: float
    low_pilot: int = 98
    high_pilot: int = 110

