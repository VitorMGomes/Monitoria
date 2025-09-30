import java.time.*;
import java.util.*;
import java.io.*;
import java.text.*;


class Game
{
    private int id;
    private String name;
    private String releaseDate;
    private int estimatedOwners;
    private float price;
    private ArrayList<String> supportedLanguages;
    private int metacriticScore;
    private float userScore;
    private int achievements;
    private ArrayList<String> publishers;
    private ArrayList<String> developers;
    private ArrayList<String> categories;
    private ArrayList<String> genres;
    private ArrayList<String> tags;



    //? -------------------------------------------------------------- Construtor Vazio -------------------------------------------------------------- ?//    
    public Game()
    {
        this.id = 0;
        this.name = "";
        this.releaseDate = "";
        this.estimatedOwners = 0;
        this.price = 0;
        this.supportedLanguages = new ArrayList<>();
        this.metacriticScore = 0;
        this.userScore = 0;
        this.achievements = 0;
        this.publishers = new ArrayList<>();
        this.developers = new ArrayList<>();
        this.categories = new ArrayList<>();
        this.genres = new ArrayList<>();
        this.tags = new ArrayList<>();
    }
    //? -------------------------------------------------------------- Construtor -------------------------------------------------------------- ?//   
    public Game(int id, String name, String releaseDate, int estimatedOwners, float price,
            ArrayList<String> supportedLanguages, int metacriticScore, float userScore, int achievements,
            ArrayList<String> publishers, ArrayList<String> developers, ArrayList<String> categories,
            ArrayList<String> genres, ArrayList<String> tags) {
        this.id = id;
        this.name = name;
        this.releaseDate = releaseDate;
        this.estimatedOwners = estimatedOwners;
        this.price = price;
        this.supportedLanguages = supportedLanguages;
        this.metacriticScore = metacriticScore;
        this.userScore = userScore;
        this.achievements = achievements;
        this.publishers = publishers;
        this.developers = developers;
        this.categories = categories;
        this.genres = genres;
        this.tags = tags;
    }
    //! -------------------------------------------------------------- Getters & Setters -------------------------------------------------------------- !//
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getReleaseDate() { return releaseDate; }
    public void setReleaseDate(String releaseDate) { this.releaseDate = releaseDate; }
    public int getEstimatedOwners() { return estimatedOwners; }
    public void setEstimatedOwners(int estimatedOwners) { this.estimatedOwners = estimatedOwners; }
    public float getPrice() { return price; }
    public void setPrice(float price) { this.price = price; }
    public ArrayList<String> getSupportedLanguages() { return supportedLanguages; }
    public void setSupportedLanguages(ArrayList<String> supportedLanguages) { this.supportedLanguages = supportedLanguages; }
    public int getMetacriticScore() { return metacriticScore; }
    public void setMetacriticScore(int metacriticScore) { this.metacriticScore = metacriticScore; }
    public float getUserScore() { return userScore; }
    public void setUserScore(float userScore) { this.userScore = userScore; }
    public int getAchievements() { return achievements; }
    public void setAchievements(int achievements) { this.achievements = achievements; }
    public ArrayList<String> getPublishers() { return publishers; }
    public void setPublishers(ArrayList<String> publishers) { this.publishers = publishers; }
    public ArrayList<String> getDevelopers() { return developers; }
    public void setDevelopers(ArrayList<String> developers) { this.developers = developers; }
    public ArrayList<String> getCategories() { return categories; }
    public void setCategories(ArrayList<String> categories) { this.categories = categories; }
    public ArrayList<String> getGenres() { return genres; }
    public void setGenres(ArrayList<String> genres) { this.genres = genres; }
    public ArrayList<String> getTags() { return tags; }
    public void setTags(ArrayList<String> tags) { this.tags = tags; }

    
    //? -------------------------------------------------------------- Clone -------------------------------------------------------------- ?//
    @Override
    public Game clone()
    {
        return new Game(id, name, releaseDate, estimatedOwners, price, supportedLanguages, metacriticScore, userScore, achievements,publishers, developers, categories, genres, tags);
    }

    










    public void ler(String line) {
        String newLine = "";
        boolean insideQuotes = false;
        int tam = line.length();

        //substituindo as virgulas que separam o as colunas do csv por ";"
        for (int i = 0; i < tam; i++) {
            char currentChar = line.charAt(i);

            if (currentChar == '"') {
                insideQuotes = !insideQuotes;
            }

            if (!insideQuotes) {

                if (currentChar == ',') {
                    newLine += ';';
                } else if (currentChar != '\"') {
                    newLine += currentChar;
                }
            } else {

                if (currentChar != '"' && currentChar != '[' && currentChar != ']') {
                    newLine += currentChar;
                }
            }
        }

        line = newLine;

        String splitted[] = line.split(";");

        try {
            setId(Integer.parseInt(splitted[0]));
            
        
        } catch (NumberFormatException e) {
            System.err.println("Erro ao converter número: " + e.getMessage());
        } catch (ArrayIndexOutOfBoundsException e) {
            System.err.println("Erro: dados insuficientes. Verifique o número de campos.");
        } catch (NullPointerException e) {
            System.err.println("Erro: dado nulo encontrado.");
        } catch (Exception e) {
            System.err.println("Erro inesperado: " + e.getMessage());
        }

    }

    public static Game[] readDb() {

        Game games[] = new Game[1850];
        Scanner reader = null;
    
        try {
            reader = new Scanner(new FileReader("/tmp/games.csv"));
    
            reader.nextLine();
    
            for (int i = 0; reader.hasNextLine(); i++) {
                String line = reader.nextLine();
                Game game = new Game();
    
                try {
                    game.ler(line);
                    games[i] = game;
                } catch (Exception e) {
                    System.err.println("Erro ao processar linha " + (i + 1) + ": " + e.getMessage());
                }
            }
    
        } catch (FileNotFoundException e) {
            System.err.println("Arquivo não encontrado: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Erro inesperado: " + e.getMessage());
        } finally {
            if (reader != null) {
                reader.close();
            }
        }
    
        return games;
    }

}   








public class Q1
{
    public static Game fullDB[] = new Game[1850];

    public static void Main(String args[])
    {
        fullDB = Game.readDb();

        Scanner scanf = new Scanner(System.in);


        scanf.close();
    }
}