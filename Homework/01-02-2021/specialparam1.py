def standard_arg(arg) :
    print(arg)
standard_arg(arg=1)
    

def pos_only_arg(arg,/) :
    print(arg)
#pos_only_arg(arg=1)

def kwd_only_arg(*,arg) :
    print(arg)
kwd_only_arg(arg=3)

def combined_example(pos_only,/,standard,*,kwd_only) :
    print(pos_only,standard,kwd_only)
    
combined_example(1,2,kwd_only=3)
