import numpy as np
import matplotlib.pyplot as plt


def draw_speedometer(working_percentage):
    fig, ax = plt.subplots(figsize=(2.25, 1.8), subplot_kw=dict(polar=True))
    theta = np.linspace(0, np.pi, 40)
    _ = np.linspace(1, 1, 2)
    ax.fill_between(theta, 0, 1, color="#cccccc", alpha=0.5)
    fill_angle = (working_percentage / 100) * np.pi
    ax.fill_between(theta[:100], 0, 1, where=(theta < fill_angle),
                    color="#4CAF50", alpha=0.8)
    arrow_angle = fill_angle
    arrow_length = 0.85
    ax.annotate('', xy=(arrow_angle, arrow_length), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', lw=1, color='red'))
    ax.text(0, 0.8, f'{int(working_percentage)}%', ha='center', va='center',
            fontsize=6, color='black', fontweight='bold')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_ylim(0, 1)
    return fig


# root = tk.Tk()
# root.title("Спидометр эффективности сети")
# working_vending_machines = 75
# total_vending_machines = 100
# working_percentage =
#  (working_vending_machines / total_vending_machines) * 100
# fig = draw_speedometer(working_percentage)
# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.draw()
# canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
# root.mainloop()
