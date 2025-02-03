class OutFormat:
    def __init__(self,lin,code,name,uxe,cost_neto):
        self.lin = lin
        self.code = code
        self.name = name
        self.uxe = uxe
        self.cost_neto = cost_neto 

    def __str__(self):
        return f"Format(lin={self.lin}, code={self.code}, name={self.name}, uxe={self.uxe}, costo_neto={self.cost_neto})"    
