#####
#Solo una bozza per la struttura generale della classe e  cosa mi serve per procedere a definire la classe#
####

import abc
from abc import ABC
#import jax
class importData(ABC):
    def __init__(self,patients):
        self.patients_dict=patients #sarà dizionario di pazienti
    #metodi da aggiungere
    
    
class import_segm(importData):
    def __init__(self, patients):
        super().__init__(patients)
    
    def read_segm_geom():
        pass

class import_img(importData):
    def __init__(self, patients):
        super().__init__(patients)
    def read_img():
        pass
