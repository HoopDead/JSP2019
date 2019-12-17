import matplotlib.pyplot as plt
import numpy as np
label = ['Java', 'C', 'Python', 'C++', 'C#', 'Visual Basic .NET', 'JavaScript', 'PHP',
         'SQL', 'Swift']
no_movies = [
    17.253,
    16.086,
    10.309,
    6.196,
    4.801,
    4.743,
    2.090,
    2.048,
    1.843,
    1.490
]

def plot_bar_x():
    # this is for plotting purpose
    index = np.arange(len(label))
    plt.bar(index, no_movies)
    plt.xlabel('Procent', fontsize=9)
    plt.ylabel('Jezyk', fontsize=9)
    plt.xticks(index, label, fontsize=9, rotation=30)
    plt.title('Popularnosc jezykow programowania')
    plt.show()

plot_bar_x()