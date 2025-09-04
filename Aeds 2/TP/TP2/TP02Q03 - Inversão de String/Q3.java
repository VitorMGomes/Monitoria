import java.util.*;


class Q3 {

    public static boolean stop(String input)
    {
        boolean stop = false;
        int len = input.length(); 

        if(len == 3 && input.charAt(0) == 'F' && input.charAt(1) == 'I' && input.charAt(2) == 'M')
        {
            stop = true;
        }

        return !stop;
    }

    public static String inverter(String input)
    {
        String output = "";
        int len = input.length();

        for(int i = 0; i < len; i++)
        {
            output += input.charAt(len - 1 - i);
        }


        return output;
    }
    
    public static void main(String[] args) {
        
        Scanner scanf = new Scanner(System.in);

        String input;

        do
        {
            input = scanf.nextLine();

            if(stop(input))
            System.out.println(inverter(input));


        }while(stop(input));


        scanf.close();
    }

}
