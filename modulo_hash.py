
import matplotlib.pyplot as plt 

class mod_hash_family():

    def __init__(self, p: int, m: int):
        self.p = p
        self.m = m
        
    def h_func(self, a: int, b: int, x: int):
        res = ((a*x+b) % self.p) % self.m
        return res
    
    def h_func_before_m(self, a: int, b: int, x: int):
        res = ((a*x+b) % self.p)
        return res
    
    def scatter_ys(self, a: int, b: int, x_lst, y_lst):
        plt.figure()
        plt.title(f'm = {m}, p = {p}, a={a}, b={b}')
        plt.scatter(x_lst, y_lst, marker='.')
        plt.show()
    
    def plot_ys(self, a: int, b: int, x_lst, y_lst):
        plt.figure()
        plt.title(f'm = {m}, p = {p}, a={a}, b={b}')
        plt.plot(y_lst)
        plt.show()
    

def list_has_dups(lst: list):
    dups_count = len(lst)-len(set(lst))
    if dups_count:
        return True
    return False


if __name__=='__main__':
    p = 661
    m = 53
    func = mod_hash_family(p,m)

    x_lst = list(range(p))
    a=3
    b=0
    y_lst = [func.h_func(a,b,x) for x in x_lst]

    y_lst_before = [func.h_func_before_m(a,b,x) for x in x_lst]

    func.view_ys(a,b,x_lst,y_lst_before)

    if not list_has_dups(y_lst_before):
        print('no duplicates')






