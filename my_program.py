import os
import numpy
import sys
import datetime

FREQUENCIES = [
    940000000,
    1800000000,
    2600000000
]

FFT_SIZE = 2048

def average_fft(fft_samples):
    avg = []
    for i in range(FFT_SIZE):
        avg_i = 0
        for j in fft_samples:
            avg_i += j[i]
        avg_i /= len(fft_samples)
        avg.append(avg_i)
    
    return avg

def split_fft_file(fft_samples):
    samples = []
    for i in range(0, len(fft_samples), FFT_SIZE):
        samples.append(fft_samples[i:i+FFT_SIZE])
    
    return samples

def get_current_time():
    return datetime.datetime.now().strftime('%Y-%m-%d:%H:%M')

def round_samples(samples):
    new_samples = []
    for s in samples:
        new_samples.append(round(s, 2))
    return new_samples

def main():    
    while True:
        for fr in FREQUENCIES:
            try:
                os.system(f"python3.10 ./msa.py ./gnubbe.bin {fr}")
                
                freq_file = numpy.fromfile(open("gnubbe.bin"), dtype=numpy.float32)
                samples = split_fft_file(freq_file)
                average = average_fft(samples)
                good_avg = round_samples(average)
                
                with open(f"{fr}_Hz.csv", "a") as file:
                    file.write(f"{get_current_time()} {str(good_avg)[1:len(str(good_avg))-1]}\n")
            except KeyboardInterrupt:
                os.system(f"git add . && git commit -m \"automatic data commit {get_current_time()}\" && git push")
                sys.exit()            
            except:
                print("fail, try again")
    

if __name__ == "__main__":
    main()