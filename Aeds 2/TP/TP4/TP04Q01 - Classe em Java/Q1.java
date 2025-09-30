import java.util.*;

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


}   








public class Q1
{
    public static void Main(String args[])
    {

    }
}