import numpy as np
import matplotlib.pyplot as plt
import os

class PlotDrawer:
    def __init__(self, data):
        self.data = data
    
    def draw_plots(self, save_dir="plots"):
        os.makedirs(save_dir, exist_ok=True)
        paths = []
        
        for column in self.data.columns:
            if column != 'name' and column != 'gt_corners':
                plt.figure(figsize=(10, 6))
                plt.plot(self.data['gt_corners'], self.data[column], 'o', label=column)
                plt.xlabel('Ground Truth Corners')
                plt.ylabel('Deviation (degrees)')
                plt.title(f'{column} vs Ground Truth Corners')
                plt.legend()
                save_path = os.path.join(save_dir, f'{column}_vs_Gt_corners.png')
                plt.savefig(save_path)
                plt.show()
                plt.close()
                paths.append(save_path)
        
        return paths

def calculate_statistics(data):
    statistics = {}
    for column in data.columns:
        if column != 'name' and column != 'gt_corners':
            mean_deviation = np.mean(np.abs(data[column]))
            max_deviation = np.max(np.abs(data[column]))
            min_deviation = np.min(np.abs(data[column]))
            statistics[column] = {'Mean Deviation': mean_deviation,
                                  'Max Deviation': max_deviation,
                                  'Min Deviation': min_deviation}
    return statistics

