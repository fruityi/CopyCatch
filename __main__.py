__debugflag__ = False

import copycatch as cc

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 5:
        ccObj = cc.CopyCatch(int(sys.argv[1]), int(sys.argv[2]),\
        float(sys.argv[3]), float(sys.argv[4]))
        #still need to check if arguments are integers or not
        
        c, P_, U_ = ccObj.RunCopyCatch()
        print("c:")
        print(c)
        print("\nP_:")
        print(P_)
        print("\nU_:")
        print(U_)
    else:
        if __debugflag__ == True:
            print('Debugging')
            cc.CopyCatch()
        else:
            print('You need to learn how to use this code')

#input("\nPress Enter to continue...")
