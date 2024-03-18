##r w >
import numpy as np

numpy_2 = print
numpy_2(np)
array1 = np.arange(0, 10)
numpy_2(array1 + 5)
numpy_2(array1 + 10)
numpy_2(array1 / array1)
numpy_2(1 / array1)
numpy_2(np.sqrt(array1))
numpy_2("The sum of aarray1 is", array1.sum())
numpy_2("The Mean of the Varray1 is", array1.mean())
numpy_2("The maximum of the array1 is", array1.max())
numpy_2("The var of the array1 is", array1.var())
numpy_2("The std of the array1 is is", array1.std())
array2 = np.arange(0, 25).reshape(5, 5)
numpy_2("array2.sum()=", array2.sum())
numpy_2("array2.sum(axis=0)", array2.sum(axis=0))
numpy_2("array2.sum(axis=1)", array2.sum(axis=1))

numpy_2("--------------------------------------------\n")
numpy_2("np-ones", np.ones(10))
numpy_2("np-arange",np.arange(10,51));
numpy_2(np.arange(9).reshape(3,3));
numpy_2(np.random.randn(1));
numpy_2("25 Random Numbers",np.random.randn(25));
numpy_2("sum of 25 Random Numbers",np.random.randn(25).sum());

numpy_2("-----------------------------------------------")
numpy_2('np.arange=',np.arange(1,101)/100);
arrrr=np.arange(1,101)/100
numpy_2("Reshape",arrrr.reshape(10,10))
numpy_2('linspace',np.linspace(0,1,20));

numpy_2(arrrr[2:15])
numpy_2(arrrr[4]);

numpy_2('np-random-seed',np.random.seed(101));
numpy_2('np-random-rand',np.random.rand(1));