import java.util.*;
public class Hungarian{
    private int[][]TheMatrix;
    private int[]rows;
    private int[]colmns;
    private int FinalAnswer;
    public Hungarian(int[][]Matrix){
        this.TheMatrix=new int[3][3];
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                this.TheMatrix[i][j]=Matrix[i][j];
            }
        }        
        
        this.rows=new int[3];
        this.colmns=new int[3];
        this.FinalAnswer=0;
    }

public void RowReduction(int [][]Matrix){


for(int i=0;i<3;i++){
    int Min=Integer.MAX_VALUE;
    for(int j=0;j<3;j++){
        if(Matrix[i][j]<Min){
            Min=Matrix[i][j];
        }




    }

    for(int k=0;k<3;k++){
        Matrix[i][k]-=Min;
    }




}

Print2dMatrix(Matrix);

}


public void ColReduction(int [][]Matrix){


    for(int i=0;i<3;i++){
        int min=Integer.MAX_VALUE;
        for(int j=0;j<3;j++){
            if(Matrix[j][i]<min){
                min=Matrix[j][i];
            }

          
        }

        for(int k=0;k<3;k++){

            Matrix[k][i]-=min;

         }  


    }
Print2dMatrix(Matrix);

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

public void NumberOfZerosInRow(int [][]Matrix){


int index=0;
for(int i=0;i<3;i++){
    for(int j=0;j<3;j++){
        if(Matrix[i][j]==0){

            index++;
        
        
        
        }
       
    }
     this.rows[i]=index;
        index=0;
}

for(int i=0;i<3;i++){
        System.out.print(this.rows[i]+" ");

}
System.out.println();

}


public void NumberOfZerosInColmn(int [][]Matrix){

int index=0;

for(int i=0;i<3;i++){
    for(int j=0;j<3;j++){
        if(Matrix[j][i]==0){

            index++;
        
        
        
        }
        
    }
    this.colmns[i]=index;
        index=0;
}



for(int i=0;i<3;i++){
        System.out.print(this.colmns[i]+" ");

}
System.out.println();


}

public boolean TestForAnOptimalAssigment(int [][]Matrix){

    this.NumberOfZerosInRow(Matrix);
    this.NumberOfZerosInColmn(Matrix);

    int number_of_zeros=0;


for(int i= 0;i<3;i++){

number_of_zeros+=this.rows[i];

}

boolean flag=false;
for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
            {
                if(this.rows[i]+this.colmns[j]==number_of_zeros)
                {
                    flag=true;
                    return flag;
                }
            }
    }


    return flag;

}

public void  ChangeTheMatrix(int[][]Matrix){

  int intersect_row=0;
  int temp=this.rows[0];

        for(int i=1;i<3;i++)
        {
            if(this.rows[i]>temp)
            {   
                intersect_row=i;

            }

        }


        int intersect_col=0;
        int temp2=this.colmns[0];

        for(int j=1;j<3;j++)
        {
            if(this.colmns[j]>temp2)
            {   
                intersect_col=j;

            }

        }

        int min_of_unlined_cells=Integer.MAX_VALUE;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (Matrix[i][j] == 0)
                {

                }
               else if(i==intersect_row&&j==intersect_col) 
                {

                }
                else
                {
                    min_of_unlined_cells = Math.min(Matrix[i][j], min_of_unlined_cells);
                }
            }
        }

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (Matrix[i][j] == 0)
                {

                }
               else if(i==intersect_row&&j==intersect_col) 
                {

                }
                else
                {
                    Matrix[i][j]-=min_of_unlined_cells;

                }
            }
        }
        Matrix[intersect_row][intersect_col] += min_of_unlined_cells;
        System.out.println("from the change the matrix method");
        System.out.println(min_of_unlined_cells+" "+intersect_row+" "+intersect_col);
        Print2dMatrix(Matrix);


}

public void PrebareMatrixToFinalStep(int[][]Matrix)
{
   
    boolean flag=TestForAnOptimalAssigment(Matrix);

    if(flag==false){
        return ;

    }
    else
    {

            ChangeTheMatrix(Matrix);
            PrebareMatrixToFinalStep(Matrix);

    }

}

public void MakingTheFinalAssignment(int[][]Matrix){

    int[] index=new int[3];
    for(int i=0;i<3;i++){
        index[i]=0;
    }
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){

            if(Matrix[i][j]!=0)
            {
                Matrix[i][j]=0;
            }
            else
            {
               if(index[j]==0)
               {
                    Matrix[i][j]=this.TheMatrix[i][j];
                    index[j]=1;
                   
                   
                   
                   
                    while(j<2){
                        Matrix[i][j+1]=0;
                        j++;
                    }
               }              

            }
            System.out.print(Matrix[i][j]+" ");


        }
    System.out.println();

}

Print2dMatrix(Matrix);

}
public void CountTheFinalAssignment(int[][]Matrix){

    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            this.FinalAnswer+=Matrix[i][j];
        }
    }


}
public int  TheHungarianAlgorihtm(int [][]Matrix){
Print2dMatrix(this.TheMatrix);
this.RowReduction(Matrix);
this.ColReduction(Matrix);
this.PrebareMatrixToFinalStep(Matrix);
System.out.println("==============================");
Print2dMatrix(Matrix);
this.MakingTheFinalAssignment(Matrix);
this.CountTheFinalAssignment(Matrix);
return this.FinalAnswer;

}



public static void main(String[] args) {
    int[][] Matrix = new int[][]{
        {30, 25, 10},
        {15, 10, 20},
        {25, 20, 15}
    };
    
   
    Hungarian hungarian=new Hungarian(Matrix);
    int res=hungarian.TheHungarianAlgorihtm(Matrix);

    System.out.println("resulte is:"+res);
}
}