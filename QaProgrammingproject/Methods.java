
public class Methods {






    public static int[][] IsSqare(int[][]arr){


        int[][]Sqare=new int[3][3];
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){

                if(arr[i][j]>0)
                {
                    Sqare[i][j]=0;

                }
                else
                {
                    int col=0;
                    int row=0;
                    for(int k=0;k<3;k++)
                    {
                        if(arr[i][k]>0){
                            col+=1;

                        }

                    }

                    for(int z=0;z<3;z++)
                    {
                        if(arr[z][j]>0)
                        {
                            row+=1;
                        }
                    }


                    Sqare[i][j]=row+col;

                    


                }






            }
        }
        return Sqare;




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



           int[][]sqare=IsSqare(cost);
           int [][]FirstDrevetive=new int[3][3];

            int MinmumValue=90000000;
            int MinmumDrev=0;
            int []minval=new int[4];
            int []mindrev=new int[4];
            int index=0;

            

            for(int i=0;i<3;i++)
            {
                for(int j=0;j<3;j++)
                   {
                       if(sqare[i][j]==0)
                       {
   
   
                       }
                       else if(sqare[i][j]==2)
                       {
                           int counter=1;    
   
                           for(int k=0;k<3;k++)
                           {
                               for(int z=0;z<3;z++)
                                   {
                                       if(cost[k][z]>0)
                                       {
                                            if(counter%2==0)
                                            {
                                                MinmumDrev+=Matrix[k][z];
                                                MinmumValue=Math.min(MinmumValue, Matrix[k][z]);
                                            }
                                            else
                                            {
                                                MinmumDrev-=Matrix[k][z];
                                                MinmumValue=Math.min(MinmumValue, -Matrix[k][z]);
            
                                            }
                                            counter++;
                                   }
   
                               }
                           }



                    }
                    else if(sqare[i][j]>=3)
                    {










                        









                    }




                        mindrev[index]=MinmumDrev;
                        minval[index]=MinmumValue;
                        index++;


                }



            }




















            return first_solution;
    }

    
    
    
    
    
    
    
    
    
    public static void  Print2dMatrix(int[][] Matrix){

        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                System.out.print(Matrix[i][j]+" ");
            }
            System.out.println();
        }





    }








































}
