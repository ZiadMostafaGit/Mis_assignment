// Product.java

import java.util.ArrayList;
import java.util.Scanner;


public class project{


    abstract public static class Product {
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

        public void setProductId(int productId) {
            this.productId = Math.abs(productId);
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public double getPrice() {
            return price;
        }

        public void setPrice(double price) {
            this.price = Math.abs(price);
        }
    }

    // ElectronicProduct.java
    public static class ElectronicProduct extends Product {
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

        public void setBrand(String brand) {
            this.brand = brand;
        }

        public int getWarrantyPeriod() {
            return warrantyPeriod;
        }

        public void setWarrantyPeriod(int warrantyPeriod) {
            this.warrantyPeriod = Math.abs(warrantyPeriod);
        }
    }

    // ClothingProduct.java
    public static class ClothingProduct extends Product {
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

        public void setSize(String size) {
            this.size = size;
        }

        public String getFabric() {
            return fabric;
        }

        public void setFabric(String fabric) {
            this.fabric = fabric;
        }
    }

    // BookProduct.java
    public static class BookProduct extends Product {
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

        public void setAuthor(String author) {
            this.author = author;
        }

        public String getPublisher() {
            return publisher;
        }

        public void setPublisher(String publisher) {
            this.publisher = publisher;
        }
    }

    // Customer.java
    public static class Customer {
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

        public void setCustomerId(int customerId) {
            this.customerId = Math.abs(customerId);
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getAddress() {
            return address;
        }

        public void setAddress(String address) {
            this.address = address;
        }
    }


    public static class Cart {
        private int customerId;
        private int nProducts;
        private ArrayList<Product> products;

        public Cart(int customerId) {
            this.customerId = Math.abs(customerId);
            this.nProducts = 0;
            this.products = new ArrayList<>();
        }

        public int getCustomerId() {
            return customerId;
        }

        public void setCustomerId(int customerId) {
            this.customerId = Math.abs(customerId);
        }

        public int getnProducts() {
            return nProducts;
        }

        public ArrayList<Product> getProducts() {
            return products;
        }

        public void addProduct(Product product) {
            products.add(product);
            nProducts++;
        }

        public void removeProduct(int productId) {
            for (int i = 0; i < products.size(); i++) {
                if (products.get(i).getProductId() == productId) {
                    products.remove(i);
                    nProducts--;
                    break;
                }
            }
        }

        public double calculatePrice() {
            double totalPrice = 0.0;
            for (Product product : products) {
                totalPrice += product.getPrice();
            }
            return totalPrice;
        }

        public Order placeOrder() {
            Order order = new Order(customerId, products, calculatePrice());
            products.clear();
            nProducts = 0;
            return order;
        }

        public void displayProducts() {
            System.out.println("Current products in the cart:");
            for (Product product : products) {
                System.out.println("- " + product.getName() + " (ID: " + product.getProductId() + ", Price: $" + product.getPrice() + ")");
            }
        }








        public void addProductsToCart() {
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter the number of products you want to add: ");
            int numProducts = scanner.nextInt();
            scanner.nextLine(); // Consume the newline character

            for (int i = 0; i < numProducts; i++) {
                System.out.println("\nEnter details for product " + (i + 1) + ":");
                System.out.print("Product type (1: Electronic, 2: Clothing, 3: Book): ");
                int productType = scanner.nextInt();
                scanner.nextLine(); // Consume the newline character

                System.out.print("Product ID: ");
                int productId = scanner.nextInt();
                scanner.nextLine(); // Consume the newline character

                System.out.print("Product name: ");
                String productName = scanner.nextLine();

                System.out.print("Product price: ");
                double productPrice = scanner.nextDouble();
                scanner.nextLine(); // Consume the newline character

                Product product;
                switch (productType) {
                    case 1:
                        System.out.print("Brand: ");
                        String brand = scanner.nextLine();
                        System.out.print("Warranty period (months): ");
                        int warrantyPeriod = scanner.nextInt();
                        scanner.nextLine(); // Consume the newline character
                        product = new ElectronicProduct(productId, productName, productPrice, brand, warrantyPeriod);
                        break;
                    case 2:
                        System.out.print("Size: ");
                        String size = scanner.nextLine();
                        System.out.print("Fabric: ");
                        String fabric = scanner.nextLine();
                        product = new ClothingProduct(productId, productName, productPrice, size, fabric);
                        break;
                    case 3:
                        System.out.print("Author: ");
                        String author = scanner.nextLine();
                        System.out.print("Publisher: ");
                        String publisher = scanner.nextLine();
                        product = new BookProduct(productId, productName, productPrice, author, publisher);
                        break;
                    default:
                        System.out.println("Invalid product type. Skipping this product.");
                        continue;
                }

                addProduct(product);
            }
        }
    }

    public static class Order {
        private int customerId;
        private static int orderIdCounter = 1;
        private int orderId;
        private ArrayList<Product> products;
        private double totalPrice;

        public Order(int customerId, ArrayList<Product> products, double totalPrice) {
            this.customerId = Math.abs(customerId);
            this.orderId = orderIdCounter++;
            this.products = new ArrayList<>(products);
            this.totalPrice = Math.abs(totalPrice);
        }

        public void printOrderInfo() {
            System.out.println("\nOrder Information:");
            System.out.println("Customer ID: " + customerId);
            System.out.println("Order ID: " + orderId);
            System.out.println("Products:");
            for (Product product : products) {
                System.out.println("- " + product.getName() + " (ID: " + product.getProductId() + ", Price: $" + product.getPrice() + ")");
            }
            System.out.println("Total Price: $" + totalPrice);
        }
    }



    public static void main(String[] args) {
        // Test case 1
        ElectronicProduct smartphone = new ElectronicProduct(1, "smartphone", 599.9, "Samsung", 1);

        // Test case 2
        ClothingProduct tshirt = new ClothingProduct(2, "T-shirt", 19.99, "Medium", "Cotton");

        // Test case 3
        BookProduct book = new BookProduct(3, "OOP", 39.99, "O'Reilly", "X Publications");

        // Test case 4
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your customer ID: ");
        int customerId = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character

        System.out.print("Enter your name: ");
        String customerName = scanner.nextLine();

        System.out.print("Enter your address: ");
        String customerAddress = scanner.nextLine();

        Customer customer = new Customer(customerId, customerName, customerAddress);

        // Test case 5
        Cart cart = new Cart(customer.getCustomerId());
        cart.addProductsToCart();
        cart.displayProducts();

        // Test case 6
        System.out.print("\nDo you want to place an order? (Y/N): ");
        String placeOrder = scanner.nextLine();

        if (placeOrder.equalsIgnoreCase("Y")) {
            Order order = cart.placeOrder();
            order.printOrderInfo();
        } else {
            System.out.println("Order not placed.");
        }
    }








}
