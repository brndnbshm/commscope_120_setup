# Dictionaries to store attenuation values (high and low) for CE-120 and CS-120 forward simulators and equalizers
# Forward attenuators (JXP) have flat loss that is equal to their nominal value, as are the SRE style return equalizers
# Datasheet --> https://webresources.commscope.com/download/assets/CE-120%2C+CS-120+1.2+GHz+Cable+Equalizers+and+Simulators+Data+Sheet/495de5663bd511f097831adcaa92e24e

equalizer_lowband = {
    '2': 2.5, '3': 3.4, '4': 4.3, '5': 5.2, '6': 6.1, '7': 7.0,
    '8': 8.0, '9': 8.9, '10': 9.8, '11': 10.7, '12': 11.6, '13': 12.5,
    '14': 13.4, '15': 14.3, '16': 15.2, '17': 16.1, '18': 17.0, '19': 17.9,
    '20': 18.8, '21': 19.8
}

equalizer_highband = {
    '2': 1.1, '3': 1.4, '4': 1.6, '5': 1.8, '6': 2, '7': 2.2,
    '8': 2.4, '9': 2.7, '10': 2.9, '11': 3.1, '12': 3.3, '13': 3.5,
    '14': 3.7, '15': 4.0, '16': 4.2, '17': 4.4, '18': 4.6, '19': 4.8,
    '20': 5.0, '21': 5.3
}

simulator_lowband = {
    '1': 0.8, '2': 0.9, '3': 1.0, '4': 1.1, '5': 1.2, '6':1.3,
    '7': 1.3, '8': 1.4, '9': 1.5, '10': 1.6
}

simulator_highband = {
    '1': 1.5, '2': 2.3, '3': 3.0, '4': 3.8, '5': 4.6, '6': 5.4,
    '7': 6.2, '8': 7.0, '9': 7.7, '10': 8.5
}

