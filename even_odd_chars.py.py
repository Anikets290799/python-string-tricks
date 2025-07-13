st = str(input("Enter a string: "))
even = "even"
odd = "odd"
st2 = None
st3 = None
st4 = (input("Enter if you want to fetch the even or odd characters (even/odd): ")).lower()
if(st4 == "even"):
    st2=st[::2]
    st5=st2.replace(" ","")
    print("the even characters are:", st5, ":the no of even charaters are: ", len(st5))
elif(st4 == "odd"):
        st3=st[1::2]
        st6=st3.replace(" ","")
        print("the odd characters are:", st6, ":the no of odd charaters are: ", len(st6))
else:
    print("enter a valid option (even/odd).")