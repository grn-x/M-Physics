import matplotlib.pyplot as plt
import numpy as np

def lighten_color(color, amount=0.5):
    """
    From https://stackoverflow.com/questions/37765197/darken-or-lighten-a-color-in-matplotlib
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB tuple.

    Examples:
    >> lighten_color('g', 0.3)
    >> lighten_color('#F034A3', 0.6)
    >> lighten_color((.3,.55,.1), 0.5)
    """
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])


# abstraction method for lightening a list of colors and return it
def lighten_colors(colors, amount=0.5):
    return [lighten_color(color, amount) for color in colors]

# Constants
overlap_factor = 0.6
parties = ["CDU", "SPD", "GRÜNE", "FDP", "LINKE", "AFD", "BSW", "OTHERS"]
colors = ["black", "r", "g", "y", "m", "b", "purple", "k"]

europe19 = [22.6, 15.8, 20.5, 5.4, 5.5, 11.0, 0, 13.7]
opacity_e19 = 1#0.5
lighten_e19 = 0.2#0.6

general21 = [18.9, 25.7, 14.8, 11.5, 4.9, 10.4, 0, 13.8]
opacity_g21 = 1#0.99
lighten_g21 = 0.7#0.7

europe24 = [30.0, 13.9, 11.9, 5.2, 2.7, 15.9, 6.2, 5.5]
opacity_e24 = 1#0.5
lighten_e24 = 0.5#0.8

general25 = [28.5, 16.4, 11.6, 4.3, 8.8, 20.8, 4.8, 3.0]
opacity_g25 = 1
lighten_g25 = 1


n = len(parties)

bar_width = 0.3

r1 = np.arange(n)
r2 = [x + bar_width * overlap_factor for x in r1]
r3 = [x + bar_width * overlap_factor for x in r2]
r4 = [x + bar_width * overlap_factor for x in r3]

plt.bar(r1, europe19, color=lighten_colors(colors, lighten_e19), width=bar_width, edgecolor='grey', label='Europe 19', alpha=opacity_e19)
plt.bar(r2, general21, color=lighten_colors(colors, lighten_g21), width=bar_width, edgecolor='grey', label='Federal 21', alpha=opacity_g21)
plt.bar(r3, europe24, color=lighten_colors(colors, lighten_e24), width=bar_width, edgecolor='grey', label='Europe 24', alpha=opacity_e24)
plt.bar(r4, general25, color=colors, width=bar_width, edgecolor='grey', label='Federal 25', alpha=opacity_g25)


plt.axhline(y=5, color='red', linestyle='--', linewidth=1, label='5% Threshold')


plt.xlabel('Parties', fontweight='bold')
plt.ylabel('Percentage', fontweight='bold')
plt.xticks([r + bar_width * 1.5 for r in range(n)], parties)

plt.legend()
plt.show()