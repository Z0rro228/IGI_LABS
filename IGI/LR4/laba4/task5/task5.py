from MatrixOperator import MatrixOperator

def task5():
    mop = MatrixOperator()
    mop.generateMatrix(3, 5)
    print("matrix:")
    print(mop.__str__())
    print(f"New matrix:{mop.insertRowAfterMin()}")
    print(f"Median:{mop.calculateMedian()}")
    print(f"Median(numpy method):{mop.calculateMedianNumpy()}")
    print()

task5()