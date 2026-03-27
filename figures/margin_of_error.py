import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, axes = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [2, 1.3]})
fig.suptitle("Margin of Error", fontsize=16, fontweight='bold', y=0.97)

# --- Panel 1: Bell curve with shaded 95% region ---
ax1 = axes[0]
mean = 1161
se = 120  # illustrative standard error
x = np.linspace(mean - 4*se, mean + 4*se, 500)
y = (1 / (se * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / se) ** 2)

# Full curve in light gray
ax1.fill_between(x, y, color='#e0e0e0', alpha=0.8)
ax1.plot(x, y, color='#666666', linewidth=1.5)

# 95% region
low = mean - 1.96 * se
high = mean + 1.96 * se
mask_95 = (x >= low) & (x <= high)
ax1.fill_between(x[mask_95], y[mask_95], color='#4a90d9', alpha=0.5)

# Vertical lines
ax1.axvline(mean, color='#c0392b', linewidth=2.5, linestyle='-', zorder=5)
ax1.axvline(low, color='#2c3e50', linewidth=1.5, linestyle='--')
ax1.axvline(high, color='#2c3e50', linewidth=1.5, linestyle='--')

# Minimal labels — just the dollar values
ax1.text(mean, max(y) * 1.06, f'${mean:,}', ha='center', fontsize=12,
         fontweight='bold', color='#c0392b')
ax1.text(low, max(y) * 1.06, f'${low:,.0f}', ha='center', fontsize=11,
         fontweight='bold', color='#2c3e50')
ax1.text(high, max(y) * 1.06, f'${high:,.0f}', ha='center', fontsize=11,
         fontweight='bold', color='#2c3e50')

# Arrow spanning the 95% CI
ax1.annotate('', xy=(high, max(y) * 0.45), xytext=(low, max(y) * 0.45),
             arrowprops=dict(arrowstyle='<->', color='#2c3e50', lw=2))
ax1.text(mean, max(y) * 0.50, '95% confidence interval', ha='center', fontsize=10,
         color='#2c3e50', fontstyle='italic')

ax1.set_xlim(mean - 4*se, mean + 4*se)
ax1.set_ylim(0, max(y) * 1.20)
ax1.set_xlabel('Cost per cardiovascular ER visit (2015$)', fontsize=11)
ax1.set_ylabel('')
ax1.set_yticks([])
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)

# --- Panel 2: "Imagine 20 samples" visual ---
ax2 = axes[1]

rng = np.random.default_rng(42)
sample_means = rng.normal(mean, se, 20)
colors = ['#4a90d9' if (low <= m <= high) else '#e74c3c' for m in sample_means]

# Shaded band for the 95% CI region
ax2.axvspan(low, high, color='#4a90d9', alpha=0.08, zorder=0)

for i, (m, c) in enumerate(sorted(zip(sample_means, colors))):
    ax2.plot(m, i, 'o', color=c, markersize=9, zorder=5)

ax2.axvline(mean, color='#c0392b', linewidth=2, linestyle='-', alpha=0.4, zorder=1)
ax2.axvline(low, color='#2c3e50', linewidth=1, linestyle='--', alpha=0.4)
ax2.axvline(high, color='#2c3e50', linewidth=1, linestyle='--', alpha=0.4)

ax2.set_xlim(mean - 4*se, mean + 4*se)
ax2.set_yticks([])
ax2.set_ylabel('20 hypothetical\nrepeat studies', fontsize=10, rotation=0, labelpad=80, va='center')
ax2.set_xlabel('Cost per visit (2015$)', fontsize=11)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)

blue_patch = mpatches.Patch(color='#4a90d9', label='Within 95% CI')
red_patch = mpatches.Patch(color='#e74c3c', label='Outside 95% CI')
ax2.legend(handles=[blue_patch, red_patch], loc='lower right', fontsize=9, framealpha=0.9)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(r'C:\Users\chris\OneDrive\Desktop\capstone\figures\margin_of_error.png',
            dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("Figure saved.")
