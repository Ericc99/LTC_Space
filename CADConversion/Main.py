import pandas as pd
import matplotlib.pyplot as plt

def draw_all_lines():
    f = pd.read_csv('./CADConversion/Map.csv', on_bad_lines='skip')
    matrix_len = f.shape[0]
    line_list = []
    for i in range(matrix_len):
        if str(f['名称'][i]) == '直线':
            plt.plot([f['端点 X'][i], f['起点 X'][i]], [f['起点 Y'][i], f['端点 Y'][i]])
    plt.show()
    

if __name__ == '__main__':
    draw_all_lines()