
public class Methods
{
   
      public int TransportaionModiul(int[][]Matrix,int[]cap,int[]req)
         {


        
    
    
            int [][]cost=new int[3][3];
            cost=GetCost(Matrix,cap,req);
            int intitial_sel=InitialSolution(cost, Matrix);







            return 0;
    
    
    
        
    
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




