
package programming.project;

/**
 *
 * @author ziad
 */
public class ProgrammingProject {


    public static void main(String[] args) {
        int[][] Matrix = new int[][]{
            {30, 25, 10},
            {15, 10, 20},
            {25, 20, 15}
        };
        
       
        Logic hungarian=new Logic(Matrix);
        int res=hungarian.TheHungarianAlgorihtm(Matrix);
    
        System.out.println("resulte is:"+res);
    }

}
