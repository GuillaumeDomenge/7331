import sys
import numpy as np
import random



def main():
    print("-------------Output------------------")
    # print(type(sys.argv[2]))
    # print(len(sys.argv))
    # for i in sys.argv:
    #     print(i)
    if len(sys.argv) != 4:
        print("Wrong number of arguments. Expecting 3 (c, A, b)")
    else:
        a_mat = eval("np.array("+sys.argv[2]+")")
        c_vec = eval("np.array("+sys.argv[1]+")")
        b_vec = eval("np.array("+sys.argv[3]+")")
        shape_a = np.shape(a_mat)
        shape_b = np.shape(b_vec)
        shape_c = np.shape(c_vec)
        if (shape_a[1] != shape_c[0]) or (shape_a[0] != shape_b[0]):
            print("Wrong dimensions...")
        else:
            #                            <----------------------------Generatin the starting tableau
            tableau = np.zeros([np.shape(a_mat)[0]+1, np.shape(a_mat)[1]+np.shape(b_vec)[0]+2])
            tableau[0][0] = 1
            tableau[1:,1:shape_a[1]+1] = a_mat
            tableau[0,1:shape_c[0]+1] = c_vec
            for i in range(shape_b[0]):
                tableau[i+1,i+2+shape_a[0]] = 1
            tableau[1:,-1] = np.transpose(b_vec)
            #                                      <---------------------------Starting pivot choice
            # print(tableau)
            counter = 0
            while np.any(tableau[0,1:-1] > 0):
                pivot_in = np.random.choice(np.where(tableau[0,1:-1] > 0)[0])
                random_value = tableau[0,1:-1][pivot_in]
                tval = 1000000
                pivot_out = 0
                for i in range(shape_b[0]):
                    if tableau[1:,-1][i]/random_value < tval:
                        tval = tableau[1:,-1][i]
                        pivot_out = i+1
                tableau[pivot_out,1:] = tableau[pivot_out,1:]/tableau[pivot_out,pivot_in+1]
                for i in range(np.shape(tableau)[0]):
                    if i != pivot_out:
                        tableau[i,1:] -= tableau[i,pivot_in+1]*tableau[pivot_out,1:]     
                    
                counter +=1
                print("The last tableau is : ...")
                print(tableau)
                print("And the optimal value is z="+str(tableau[0,-1]))
                print("Reached at : ")
                print(tableau[0,1:shape_c[0]+1])
    


if __name__ == "__main__":
    main()
