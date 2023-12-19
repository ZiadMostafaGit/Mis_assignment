import java.util.Scanner;
public class MainFile {



    public static void main(String[] args) {
        int[][]Matix=new int[3][3];
        int[] req=new int[3];
        int[]cap=new int[3];
        Scanner input=new Scanner(System.in);    
        for(int i=0;i<3;i++){
            System.out.println("Enter the capacity["+i+"] and Requirements["+i+"]");
            cap[i]=input.nextInt();
            req[i]=input.nextInt();
            for(int j=0;j<3;j++){
                System.out.println("enter Matrix["+i+"]["+j+"]");
                Matix[i][j]=input.nextInt();

            }
        }
        Methods methods=new Methods();

        // int first_solution=methods.NorthwestCorner(Matix,cap,req);
        // System.out.println("The First Solution:"+first_solution);

        // int [][]arr=new int[3][3];
        // arr=Methods.IsSqare(Matix);
        // Methods.Print2dMatrix(arr);
        
    
    
    
    
    
    
    }
    
}
