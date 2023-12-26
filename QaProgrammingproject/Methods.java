
public class Methods
{
   
      public int TransportaionModiul(int[][]Matrix,int[]cap,int[]req)
         {


        
    
    
            int [][]cost=new int[3][3];
            cost=GetCost(Matrix,cap,req);
            int intitial_sel=InitialSolution(cost, Matrix);
            int [][]final_res=new int[3][3];
            final_res=OptimalSolution(cost,Matrix);
            int optimal=InitialSolution(final_res, Matrix);

            return 0;
        
    
        }
    

        // cant find algo to get the close path for the zeros cells 
        public int[][] OptimalSolution(int[][]cost,int[][]Matrix){

         
                    return cost;

                    }

      public int[][] GetCost(int[][]Matrix,int[]cap,int[]req)
      {
            int [][]cost=new int[3][3];    
           for(int i=0;i<3;i++){
      
                  for(int j=0;j<3;j++){
                      if(cap[i]==0||req[j]==0){
                          cost[i][j]=0;
                      }
      
                      else if(cap[i]>req[j])
                      {
                          cost[i][j]=req[j];
                          cap[i]-=req[j];
                          req[j]=0;
                      }
                      else if(req[j]>cap[i])
                      {
                          cost[i][j]=cap[i];
                          req[j]-=cap[i];
                          cap[i]=0;
                      }
                      else if(req[j]==cap[i])
                      {
                          cost[i][j]=req[j];
                          cap[i]=req[j]=0;
      
                      }
                      else{
      
                      }
                  }
              }
      
             
          return cost;
      
      }
      
      
      public int InitialSolution(int[][]cost,int[][]Matrix){
           int first_solution=0;
                  for(int i=0;i<3;i++){
                      for(int j=0;j<3;j++){
                          first_solution+=cost[i][j]*Matrix[i][j];
                      }
                  }
                  return first_solution;
      
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



/*   // int row,col,i,j;
            // row=col=0;
            // for( i=0;i<=2;i++){


            //     for(j=0;j<=2;j++){


            //         if(cost[i][j]==0)
            //         {

            //         }
            //         else
            //         {

            //             row=i;
            //             col=j;

            //             if(row==0)
            //             {
            //                 while(row<=2)
            //                 {
            //                     if(cost[row][col]!=0)
            //                     {
            //                         break;
            //                     }else
            //                     {
            //                         row++;
            //                     }

            //                 }


            //             }
            //             else if(row==2)
            //             {
            //                 while(row>=0)
            //                 {

            //                     if(cost[row][col]!=0)
            //                     {
            //                         break;
            //                     }
            //                     else
            //                     {
            //                         row--;
            //                     }


            //                 }
            //             }
            //             if(col==0)
            //             {

            //                 while (col<=2)
            //                 {
            //                     if(cost[row][col]!=0)
            //                     {

            //                         break;
            //                     }else
            //                     {
            //                         col++;
            //                     }
                                
            //                 }


            //             }
            //             else if(col==2)
            //             {
            //                 while(col>=0)
            //                 {

            //                     if(cost[row][col]!=0)
            //                     {
            //                         break;
            //                     }
            //                     else
            //                     {

            //                         col--;
            //                     }
            //                 }
            //             }*/



