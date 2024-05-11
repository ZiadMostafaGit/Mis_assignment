import java.util.ArrayList;
import java.util.Scanner;



public class project{


    public  abstract class Product {
        protected int productId;
        protected String name;
        protected double price;

        public Product(int productId, String name, double price) {
            this.productId = Math.abs(productId);
            this.name = name;
            this.price = Math.abs(price);
        }

        public int getProductId() {
            return productId;
        }

        public String getName() {
            return name;
        }

        public double getPrice() {
            return price;
        }
    }

    public  class ElectronicProduct extends Product {
        private String brand;
        private int warrantyPeriod;

        public ElectronicProduct(int productId, String name, double price, String brand, int warrantyPeriod) {
            super(productId, name, price);
            this.brand = brand;
            this.warrantyPeriod = Math.abs(warrantyPeriod);
        }

        public String getBrand() {
            return brand;
        }

        public int getWarrantyPeriod() {
            return warrantyPeriod;
        }
    }

    public  class ClothingProduct extends Product {
        private String size;
        private String fabric;

        public ClothingProduct(int productId, String name, double price, String size, String fabric) {
            super(productId, name, price);
            this.size = size;
            this.fabric = fabric;
        }

        public String getSize() {
            return size;
        }

        public String getFabric() {
            return fabric;
        }
    }

    public  class BookProduct extends Product {
        private String author;
        private String publisher;

        public BookProduct(int productId, String name, double price, String author, String publisher) {
            super(productId, name, price);
            this.author = author;
            this.publisher = publisher;
        }

        public String getAuthor() {
            return author;
        }

        public String getPublisher() {
            return publisher;
        }
    }

    public  class Customer {
        private int customerId;
        private String name;
        private String address;

        public Customer(int customerId, String name, String address) {
            this.customerId = Math.abs(customerId);
            this.name = name;
            this.address = address;
        }

        public int getCustomerId() {
            return customerId;
        }

        public String getName() {
            return name;
        }

        public String getAddress() {
            return address;
        }
    }

    public  class Cart {
        private int customerId;
        private int nProducts;
        private ArrayList<Product> products;

        public Cart(int customerId) {
            this.customerId = Math.abs(customerId);
            this.nProducts = 0;
            this.products = new ArrayList<>();
        }

        public void addProduct(Product product) {
            products.add(product);
            nProducts++;
        }

        public void removeProduct(int index) {
            if (index >= 0 && index < nProducts) {
                products.remove(index);
                nProducts--;
            }
        }

        public double calculatePrice() {
            double totalPrice = 0;
            for (Product product : products) {
                totalPrice += product.getPrice();
            }
            return totalPrice;
        }

        public void placeOrder() {
            double totalPrice = calculatePrice();
            int orderId = 1; 
            Order order = new Order(customerId, orderId, products, totalPrice);
            order.printOrderInfo();
        }
    }

    public  class Order {
        private int customerId;
        private int orderId;
        private ArrayList<Product> products;
        private double totalPrice;

        public Order(int customerId, int orderId, ArrayList<Product> products, double totalPrice) {
            this.customerId = Math.abs(customerId);
            this.orderId = Math.abs(orderId);
            this.products = new ArrayList<>(products);
            this.totalPrice = Math.abs(totalPrice);
        }

        public void printOrderInfo() {
            System.out.println("Here's your order's summary:");
            System.out.println("Order ID: " + orderId);
            System.out.println("Customer ID: " + customerId);
            System.out.println("Products:");
            for (Product product : products) {
                System.out.println(product.getName() + " - $" + product.getPrice());
            }
            System.out.println("Total Price: $" + totalPrice);
        }
    }


    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        project ecommerceSystem = new project(); // Create an instance of the outer class

        System.out.println("Welcome to the E-Commerce System!");

        System.out.print("Please enter your id: ");
        int customerId = scanner.nextInt();
        scanner.nextLine(); // Consume newline character

        System.out.print("Please enter your name: ");
        String customerName = scanner.nextLine();

        System.out.print("Please enter your address: ");
        String customerAddress = scanner.nextLine();

        Customer customer = ecommerceSystem.new Customer(customerId, customerName, customerAddress);
        Cart cart = ecommerceSystem.new Cart(customer.getCustomerId());

        // Create products
        ElectronicProduct smartphone = ecommerceSystem.new ElectronicProduct(1, "Smartphone", 599.99, "Samsung", 1);
        ClothingProduct tShirt = ecommerceSystem.new ClothingProduct(2, "T-Shirt", 19.99, "Medium", "Cotton");
        BookProduct oopBook = ecommerceSystem.new BookProduct(3, "OOP", 39.99, "O'Reilly", "X Publications");


                System.out.print("How many products you want to add to your cart? ");
                int numProducts = scanner.nextInt();

                for (int i = 0; i < numProducts; i++) {
                    System.out.println("Which product would you like to add? 1- Smartphone 2- T-Shirt 3- OOP");
                    int choice = scanner.nextInt();
                    switch (choice) {
                        case 1:
                            cart.addProduct(smartphone);
                            break;
                        case 2:
                            cart.addProduct(tShirt);
                            break;
                        case 3:
                            cart.addProduct(oopBook);
                            break;
                        default:
                            System.out.println("Invalid choice!");
                            i--;
                            break;
                    }
                }

                double totalPrice = cart.calculatePrice();
                System.out.println("Your total is $" + totalPrice + ". Would you like to place the order? 1- Yes 2- No");
                int placeOrder = scanner.nextInt();
                if (placeOrder == 1) {
                    cart.placeOrder();
                } else {
                    System.out.println("Order cancelled.");
                }

                scanner.close();
    }


}   
