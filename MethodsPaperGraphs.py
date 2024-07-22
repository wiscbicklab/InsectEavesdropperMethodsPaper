import matplotlib.pyplot as plt
import librosa
import librosa.display
import os

# Create plots directory if it doesn't exist
plots_dir = "plots"
if not os.path.exists(plots_dir):
    os.makedirs(plots_dir)

# Load the sound files
y, sr = librosa.load("/home/pc/Paper/Lab/Manduca/I5_leaf5_I1_leaf6_03_29_2023_22_43_240.wav")
y1, sr1 = librosa.load("/home/pc/Paper/Lab/Manduca/I5_leaf5_I1_leaf6_03_29_2023_22_43_241.wav")
y2, sr2 = librosa.load("/home/pc/Paper/Lab/CPB/CPB3_04_04_2023_22_05_471hour0.wav")
y3, sr3 = librosa.load("/home/pc/Paper/Lab/CPB/CPB3_04_04_2023_22_05_472hour0.wav")
y4, sr4 = librosa.load("/home/pc/Paper/Lab/ECB/ECB15_36_04_03_2023_22_38_521hour0.wav")
y5, sr5 = librosa.load("/home/pc/Paper/Lab/ECB/ECB15_36_04_03_2023_22_38_522hour0.wav")
y6, sr6 = librosa.load("/home/pc/Paper/Lab/Cornworm/RW37_32_04_08_2023_19_30_491hour0.wav")
y7, sr7 = librosa.load("/home/pc/Paper/Lab/Cornworm/RW37_32_04_08_2023_19_30_492hour0.wav")

# Function to save the plots
def save_plot(y, sr, title, filename):
    plt.figure(figsize=(8, 4))
    plt.title(title)
    librosa.display.waveshow(y, sr=sr, color='black')
    plt.ylim(-0.003, 0.003)
    plt.xticks([0, 30*60, 60*60])
    plt.xlabel('Time (mins)')
    plt.ylabel('Amplitude')
    plt.savefig(os.path.join(plots_dir, filename))
    plt.close()

# Save each plot
save_plot(y, sr, 'Manduca - I5_leaf5_I1_leaf6_03_29_2023_22_43_240', 'Manduca_240.png')
save_plot(y1, sr1, 'Manduca - I5_leaf5_I1_leaf6_03_29_2023_22_43_241', 'Manduca_241.png')
save_plot(y2, sr2, 'Colorado Potato Beetle - CPB3_04_04_2023_22_05_471hour0', 'CPB_471.png')
save_plot(y3, sr3, 'Colorado Potato Beetle - CPB3_04_04_2023_22_05_472hour0', 'CPB_472.png')
save_plot(y4, sr4, 'European Corn Borer - ECB15_36_04_03_2023_22_38_521hour0', 'ECB_521.png')
save_plot(y5, sr5, 'European Corn Borer - ECB15_36_04_03_2023_22_38_522hour0', 'ECB_522.png')
save_plot(y6, sr6, 'Corn Rootworm - RW37_32_04_08_2023_19_30_491hour0', 'Cornworm_491.png')
save_plot(y7, sr7, 'Corn Rootworm - RW37_32_04_08_2023_19_30_492hour0', 'Cornworm_492.png')
