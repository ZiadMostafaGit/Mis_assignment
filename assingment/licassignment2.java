import java.util.*;



public class licassignment2 {
    

public static void main(){


    Scanner KB=new Scanner(System.in);
    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 
    String dayString1 = null, dayString2 = null, dayString3 = null;
    int day = KB.nextInt();
    
    if (day == 1) dayString1 = "Saturday";
    if (day == 2) dayString2 = "Sunday";
    if (day == 3) dayString3 = "Monday";
    if (day == 4) dayString1 = "Tuesday";
    if (day == 5) dayString2 = "Wednesday";
    
    if (day < 1 || day > 5) dayString3 = "Invalid day";
}



}



