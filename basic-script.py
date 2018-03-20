print("\n################################################");
print("######## hello World #################");
print("################################################\n");

number_list = [0,1,2,3,4,5,6,7];
print("number_list[4] : " , number_list[4]);
print("number_list : " , number_list);
print("number_list[2:5] : ",number_list[2:5]);
print("number_list[-1] : " , number_list[-1]);
number_list[4]=100;
print("number_list[4] : " , number_list[4]);

print("\n################################################\n");

name='Apurv';
last_name='Mathur';
print("name[2] : " , name[2]);
print("len(name) : " , len(name));
print("name  + last_name : "+(name  + last_name))

print("\n################################################\n");

my_tupule = 0,1,2,3,4;
print("my_tupule[4] : " , my_tupule[4]);
# my_tupule[4]=100;  -- gives error 

print("\n################################################\n");

my_dictionary = {   'key1':'value1' , 
                    'key2': 23,
                    'key3': 22/7,
                    'key4': 23.0808402384092384093284093284092384098234098234J
                    
                    };
print("my_dictionary : ", my_dictionary);
print("my_dictionary.keys() : ",my_dictionary.keys());

my_dictionary['key5'] = 'extra value' ; 
print("my_dictionary : ", my_dictionary);

print("\n################################################\n");
print('print the number')
for i in number_list : 
    print( ">> ", i );
print('outside the loop ')
# to end the code block inside the loop , change indentaion 

print("\n################################################\n");

for j in my_tupule :
    if j%2 == 0 :
        print('even>> ',j)
    else : 
        print('odd>> ',j)

print("\n################################################\n");

