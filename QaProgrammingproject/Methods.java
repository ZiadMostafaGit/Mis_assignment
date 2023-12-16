
public class Methods {
   public Methods(){
    System.out.println("Hello from Methods class");
   }
    public int NorthwestCorner(int[][]Matrix,int[]cap,int[]req){


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

        int first_solution=0;
            for(int i=0;i<3;i++){
                for(int j=0;j<3;j++){
                    first_solution+=cost[i][j]*Matrix[i][j];
                }
            }


            return first_solution;
    }
}
