#match case - use match case to avoid ladder or if else in case of multiple choise
d= int ( input ( " enter day number "))


match d :
         case 1 : print ( " monday ")
         case 2: print ( " tuesday ")
         case 3 :print ( " wedday ")
         case 4 :print ( " thuday ")
         case 5 :print ( " friday ")
         case 6 :print ( " saturday ")
         case 7 :print ( " sunday ")

# input any alphbate and displya vovel /  consotant
alpha = input ( " enter any vovel ")
match alpha :
    case "a" : print ( " vovel ")
    case "e" : print ( "vovel ")
    case "i" : print ( "vovel ")
    case "o" : print ( "vovel ")
    case "u" : print ( "vovel ")
    case _ : print ( " constant ")

# second mthord 
match alpha :
    case 'a' | 'e'| 'i'| 'o'| 'u' : print ( " vovel ")

    case '1'| '2'| '3'| '4'|'5'|'6'|'7'|'8'|'9'|'0': print (" diget ")
    case _ : print ( " constant ")






















    
