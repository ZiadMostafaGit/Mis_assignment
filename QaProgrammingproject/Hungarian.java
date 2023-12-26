public class Hungarian{
    

public int[][] RowReduction(int [][]Matrix){

int[][]Solved=new int[Matrix.length][Matrix[0].length];

for(int i=0;i<3;i++){
    int Min=1000000000;
    for(int j=0;j<3;j++){
        if(Matrix[i][j]<Min){
            Min=Matrix[i][j];
        }




    }

    for(int k=0;k<3;k++){
        Solved[i][k]=Matrix[i][k]-Min;
    }




}

return Solved;


}










public void ColReduction(int [][]Matrix){


    for(int i=0;i<3;i++){
        int min=100000000;
        for(int j=0;j<3;j++){
            if(Matrix[j][i]<min){
                min=Matrix[j][i];
            }

          
        }

        for(int k=0;k<3;k++){

            Matrix[k][i]-=min;

         }  


    }


}



















public static void  Print2dMatrix(int[][] Matrix)    

{

    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            System.out.print(Matrix[i][j]+" ");
        }
        System.out.println();
    }

}    































}
