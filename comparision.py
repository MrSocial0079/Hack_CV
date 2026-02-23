import pandas as pd
import matplotlib.pyplot as plt

# Load logs
reading = pd.read_csv("logs/reading.csv")
movie = pd.read_csv("logs/movie.csv")

reading_blinks = len(reading)
movie_blinks = len(movie)

print("\n--- Blink Comparison ---")
print("Reading Total Blinks:", reading_blinks)
print("Watching Movie Total Blinks:", movie_blinks)

# ---- Create Figure ----
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,8))

# ---- Line Graph (Blink Progression) ----
ax1.plot(reading["Frame"], reading["BlinkCount"],
         label="Reading", linewidth=2)

ax1.plot(movie["Frame"], movie["BlinkCount"],
         label="Watching", linewidth=2)

ax1.set_title("Blink Progression Over Time")
ax1.set_xlabel("Frame (Time)")
ax1.set_ylabel("Cumulative Blinks")
ax1.legend()

# ---- Bar Graph (Total Blinks) ----
ax2.bar(["Reading", "Watching"],
        [reading_blinks, movie_blinks])

ax2.set_title("Total Blink Count Comparison")
ax2.set_ylabel("Number of Blinks")

plt.tight_layout()
plt.show()

# ---- Research Note ----
print("\nNote:")
print("Under conditions of burning eye sensation, increased blinking frequency may occur as a normal physiological response.")