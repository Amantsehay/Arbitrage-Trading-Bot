from docplex.mp.model import Model 
from itertools import combinations
from .utils import MultiThreads 
from collections import OrderedDict
import numpy as np 


class AmtOptimizer(Model):
    path = None 
    path_n = None 
    orderbook_n = None 
    x = None
    y = None 
    z = None 
    PathOptimizer = None 
    precision_matrix = None 
    amt_matrix = None 
    price_matrix = None 
    big_m = None 
    order_book = None 
    trade_solution = None 
    profit_unit = None 
    trade_amt_ptc = None 
    print_content = None 
    amplifier = None 
    default_precision = None 
    
    def __init__(self, PathOptimizer, orderbook_n):
        super().__init__()
        self.PathOptimizer = PathOptimizer
        self.get_pair_info()
        self.get_precision()
        self.orderbook_n = orderbook_n
        self.big_m = 1e+10
        self.trade_amt_ptc = 1
        self.amplifier = 1e-10
        self.default_precision = 3
        
        
    def get_solution(self):
        self._update_path_params()
        self._update_model()
        self._get_solution()
        
    def _update_path_params(self):
        self.path = self.PathOptimizer.path 
        self.path_n = len(self.path)
        self.set_path_commision()
        self.path_order_book()
        self.get_reverse_list()
        self.set_precision_matrix()
        self.set_amt_and_price_matrix()
        self.balance_constraint()
    
    def _update_model(self):
        self.clear()
        self._init_decision_vars()
        self._set_constraints()
        self._update_objective()
    
    def _init_decision_vars(self):
        self.int_var = self.integer_var_list(self.path_n * self.orderbook_n, name = 'x')
        self.x = np.array(self.int_var).reshape(self.path_n, self.orderbook_n)
        self.bi_var = self.binary_var_list(self.path_n * self.orderbook_n, name = 'y')
        self.y = np.array(self.bi_var).reshape(self.path_n, self.orderbook_n)
        self.z = self.x * self.precision_matrix
        
        
    def _set_constraints(self):
        self.add_constraint(self.sum(self.y) == self.path_n)
        # 2. you can only choose one price level from each step's order book
        self.add_constraints(self.sum(self.y[i, :]) <= 1 for i in range(self.path_n))
        # only the amount at the chosen price level could be larger than 0
        self.add_constraints(
            self.x[i, j] <= self.big_m * self.y[i, j] for i in range(self.path_n) for j in range(self.orderbook_n))
        # 3. amount for order should be smaller than given order book amount
        self.add_constraints(
            self.z[i, j] <= self.trade_amt_ptc * self.amt_matrix[i, j] for i in range(self.path_n) for j in
            range(self.orderbook_n))
        
        
        first_coin_bal = self.balance_vol[self.path[0]][self.path[0][0]]
        
        if not self.reverse_list:
            self.add_constraint(self.sum(self.z))
        
        
        
        
        

        