import unittest
import s2_rut_algo
import numpy as np


class S2RutAlgoTest(unittest.TestCase):
    def test_simple_case_B8(self):
        rut_algo = s2_rut_algo.S2RutAlgo()
        rut_algo.a = 6.22865527455779  
        rut_algo.e_sun = 1036.39  
        rut_algo.u_sun = 1.03418574554466  
        rut_algo.tecta = 63.5552301619033  
        rut_algo.quant = 10000.0  
        rut_algo.alpha = 0.571  
        rut_algo.beta = 0.04447  
        rut_algo.u_diff_temp = 1  

        band_data = [100,500,1000,2000,5000,10000,15000.]
        rut_result = rut_algo.unc_calculation(np.array(band_data), 7)

        self.assertEqual([250, 92, 64, 42, 28, 24, 23], rut_result)

    def test_simple_case_B2(self):
        rut_algo = s2_rut_algo.S2RutAlgo()
        rut_algo.a = 6.22865527455779
        rut_algo.e_sun = 1036.39
        rut_algo.u_sun = 1.03418574554466
        rut_algo.tecta = 63.5552301619033
        rut_algo.quant = 10000.0
        rut_algo.alpha = 0.571
        rut_algo.beta = 0.04447
        rut_algo.u_diff_temp = 1

        band_data = [100,500,1000,2000,5000,10000,15000.]
        rut_result = rut_algo.unc_calculation(np.array(band_data), 1)

        self.assertEqual([250, 92, 64, 42, 28, 24, 23], rut_result)



