import java.util.Scanner;


public class MainFile {


    public static void main(String[] args) {
        int[][]Matix=new int[3][3];
        
        Scanner input=new Scanner(System.in);    
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                System.out.println("enter Matrix["+i+"]["+j+"]");
                Matix[i][j]=input.nextInt();

            }
        }

        Hungarian hungarian=new Hungarian();
        int[][]reducted_matrix=hungarian.RowReduction(Matix);
        Hungarian.Print2dMatrix(reducted_matrix);
        System.out.println("=============================================================");
        hungarian.ColReduction(reducted_matrix);
        Hungarian.Print2dMatrix(reducted_matrix);





        // Methods methods=new Methods();

        // int first_solution=methods.NorthwestCorner(Matix,cap,req);
        // System.out.println("The First Solution:"+first_solution);

        // int [][]arr=new int[3][3];
        // arr=Methods.IsSqare(Matix);
        // Methods.Print2dMatrix(arr);
        
    
    // int[] req=new int[3];
        // int[]cap=new int[3];
    
    /*cap[i]=input.nextInt();
            req[i]=input.nextInt();
            */
    
    
    }
    
}
