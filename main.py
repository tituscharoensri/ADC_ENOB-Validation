import numpy as np
import matplotlib.pyplot as plt

# Function to read ADC values from a text file
def read_adc_values(filename):
    with open(filename, 'r') as file:
        adc_values = [int(line.strip()) for line in file]
    return np.array(adc_values)

# Function to perform FFT analysis
def perform_fft(adc_values, sampling_rate):
    n = len(adc_values)
    #  This line computes the FFT of the adc_values.
    #  FT transforms the time-domain signal (adc_values) into the frequency domain.
    #  fft_values contains complex numbers representing the amplitudes and phases of the frequency components.
    fft_values = np.fft.fft(adc_values)

    # Computes the frequency bins for the FFT output.
    # fft_freqs contains frequencies corresponding to each element in fft_values.
    # The d parameter specifies the spacing between frequency bins, which is 1 / sampling_rate.
    fft_freqs = np.fft.fftfreq(n, d=1 / sampling_rate)

    # Take only the positive frequencies
    # Selects only the positive frequencies from fft_freqs.
    # FFT output is symmetric with respect to the Nyquist frequency (sampling_rate / 2).
    # Therefore, positive_freqs contains frequencies from 0 to sampling_rate / 2.
    positive_freqs = fft_freqs[:n // 2]

    # Computes the magnitudes of FFT values corresponding to positive_freqs.
    # np.abs() calculates the absolute value of complex FFT coefficients, giving the amplitude.
    # Division by n normalizes the FFT amplitude by the number of samples, providing a proper amplitude representation.
    positive_fft_values = np.abs(fft_values[:n // 2]) / n

    return positive_freqs, positive_fft_values

# Function to calculate ENOB
def calculate_enob(positive_fft_values):
    # Signal power is at the fundamental frequency
    # The maximum value of positive_fft_values typically corresponds to the fundamental frequency of the signal.
    # By squaring this value, we obtain an estimate of the total power of the signal component.
    signal_power = np.max(positive_fft_values) ** 2

    # Noise power is the sum of the squares of all other bins
    # In FFT analysis, each bin (or 'frequency component') represents a contribution to the overall signal.
    # The noise power is computed as the sum of squares of all FFT coefficients minus the signal power.
    # This approach assumes that the remaining power after accounting for the signal (in 'signal_power') constitutes the noise across all frequency components.
    noise_power = np.sum(positive_fft_values ** 2) - signal_power

    # Calculate SNR (Signal-to-Noise Ratio)
    # note: I am using magnitudes NOT RMS, you might see different formulas online
    snr = (signal_power / noise_power) * 1e20
    print(f"snr: {snr:.2f} ")
    # Calculate ENOB (Effective Number of Bits)
    enob = (np.log2(snr) - 1.76) / 6.02
    return enob

# Main function
def main():
    filename = 'adc_values.txt'
    sampling_rate = 31250 # 31.25 kSPS (samples per second)

    # Read ADC values from file
    adc_values = read_adc_values(filename)

    # Perform FFT analysis
    positive_freqs, positive_fft_values = perform_fft(adc_values, sampling_rate)

    # Calculate ENOB
    enob = calculate_enob(positive_fft_values)

    # Print ENOB value
    print(f"ENOB: {enob:.2f} bits")

    # Plot the FFT results
    plt.plot(positive_freqs, positive_fft_values)
    plt.title('FFT Analysis')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()

# Execute main function if script is run directly
if __name__ == '__main__':
    main()
