import javax.swing.*;
import java.awt.*;
import java.awt.event.*;


public class EcommerceGUI extends JFrame {
    private JTextField idField, nameField, addressField;
    private JComboBox<String> productComboBox;
    private JButton addButton, placeOrderButton;
    private JTextArea cartArea;
    private project ecommerceSystem;
    private project.Cart cart; // Change this line


    public EcommerceGUI() {
        setTitle("E-Commerce System");
        setLayout(new BorderLayout());
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Create components
        idField = new JTextField(10);
        nameField = new JTextField(10);
        addressField = new JTextField(20);
        productComboBox = new JComboBox<>(new String[]{"Smartphone", "T-Shirt", "OOP"});
        addButton = new JButton("Add to Cart");
        placeOrderButton = new JButton("Place Order");
        cartArea = new JTextArea(10, 20);
        cartArea.setEditable(false);

        // Create panels
        JPanel customerPanel = new JPanel(new GridLayout(3, 2));
        customerPanel.add(new JLabel("Customer ID:"));
        customerPanel.add(idField);
        customerPanel.add(new JLabel("Customer Name:"));
        customerPanel.add(nameField);
        customerPanel.add(new JLabel("Customer Address:"));
        customerPanel.add(addressField);

        JPanel productPanel = new JPanel(new BorderLayout());
        productPanel.add(new JLabel("Select Product:"), BorderLayout.WEST);
        productPanel.add(productComboBox, BorderLayout.CENTER);
        productPanel.add(addButton, BorderLayout.EAST);

        JPanel cartPanel = new JPanel(new BorderLayout());
        cartPanel.add(new JLabel("Cart:"), BorderLayout.NORTH);
        cartPanel.add(new JScrollPane(cartArea), BorderLayout.CENTER);
        cartPanel.add(placeOrderButton, BorderLayout.SOUTH);

        // Add panels to the frame
        add(customerPanel, BorderLayout.NORTH);
        add(productPanel, BorderLayout.CENTER);
        add(cartPanel, BorderLayout.SOUTH);

        // Add event listeners
        addButton.addActionListener(new AddToCartListener());
        placeOrderButton.addActionListener(new PlaceOrderListener());

        pack();
        setVisible(true);
    }

     private class AddToCartListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            int customerId = Integer.parseInt(idField.getText());
            String customerName = nameField.getText();
            String customerAddress = addressField.getText();
            String productName = (String) productComboBox.getSelectedItem();

            if (ecommerceSystem == null) {
                ecommerceSystem = new project();
                project.Customer customer = ecommerceSystem.new Customer(customerId, customerName, customerAddress); // Change this line
                cart = ecommerceSystem.new Cart(customer.getCustomerId()); // Change this line
            }

            project.Product product; // Change this line
            switch (productName) {
                case "Smartphone":
                    product = ecommerceSystem.new ElectronicProduct(1, "Smartphone", 599.99, "Samsung", 1); // Change this line
                    break;
                case "T-Shirt":
                    product = ecommerceSystem.new ClothingProduct(2, "T-Shirt", 19.99, "Medium", "Cotton"); // Change this line
                    break;
                case "OOP":
                    product = ecommerceSystem.new BookProduct(3, "OOP", 39.99, "O'Reilly", "X Publications"); // Change this line
                    break;
                default:
                    return;
            }

            cart.addProduct(product);
            cartArea.append(product.getName() + " - $" + product.getPrice() + "\n");
        }
    }

     private class PlaceOrderListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            if (cart != null) {
                cart.placeOrder();
                cartArea.setText("");
            }
        }
    }
    public static void main(String[] args) {
        new EcommerceGUI();
    }
}