# Vendor Supply Management (VSM) System

A comprehensive Django-based platform that facilitates seamless interaction between suppliers and vendors, featuring advanced inventory management, intelligent demand forecasting, and robust order processing capabilities.

## 🚀 Features

### For Suppliers
- **Inventory Management**: Add, update, and delete commodity listings with detailed specifications
- **Order Processing**: Accept/reject vendor orders with delivery scheduling
- **Demand Forecasting**: AI-powered demand prediction using Facebook Prophet
- **Analytics Dashboard**: Visual insights into demand trends and business metrics
- **Rating System**: View and manage customer feedback and ratings
- **Custom Commodities**: Create and manage custom product listings

### For Vendors
- **Product Search**: Advanced search and filtering across supplier inventories
- **Order Placement**: Streamlined ordering process with real-time stock validation
- **Order Tracking**: Monitor order status from placement to delivery
- **Rating System**: Rate suppliers and view community feedback
- **Supplier Analytics**: View supplier ratings and performance metrics

### Core System Features
- **Role-Based Access Control**: Separate dashboards for suppliers and vendors
- **Real-Time Inventory Updates**: Automatic stock adjustments on order acceptance
- **Time-Based Filtering**: Filter orders and data by week, month, quarter, or year
- **Responsive Design**: Mobile-friendly interface
- **Secure Authentication**: Django's built-in authentication with custom user models

## 🛠️ Technology Stack

- **Backend**: Django 5.1.6, Django REST Framework
- **Database**: PostgreSQL
- **Machine Learning**: Facebook Prophet for demand forecasting
- **Data Analysis**: Pandas, Matplotlib
- **Authentication**: Django Auth with SimpleJWT
- **Frontend**: HTML, CSS, JavaScript (Django Templates)

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip (Python package manager)
- Virtual environment (recommended)

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/vsm-system.git
cd vsm-system
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install django
pip install psycopg2-binary
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install prophet
pip install pandas
pip install matplotlib
```

### 4. Database Setup
1. Create a PostgreSQL database:
```sql
CREATE DATABASE vsm_db;
CREATE USER vsm_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE vsm_db TO vsm_user;
```

2. Update `settings.py` with your database credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vsm_db',
        'USER': 'vsm_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Load Initial Data (Optional)
```bash
python manage.py loaddata initial_commodities.json  # If you have fixture data
```

### 8. Start Development Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to access the application.

## 🎯 Usage

### Getting Started
1. **Sign Up**: Create an account as either a Supplier or Vendor
2. **For Suppliers**: 
   - Add your commodity inventory
   - Set prices and availability
   - Manage incoming orders
3. **For Vendors**: 
   - Browse available commodities
   - Place orders with suppliers
   - Track order status and provide ratings

### Key Workflows

#### Supplier Workflow
```
Add Commodities → Receive Orders → Accept/Reject → Schedule Delivery → Mark as Delivered
```

#### Vendor Workflow
```
Search Products → Place Order → Track Status → Receive Delivery → Rate Supplier
```

## 📊 Demand Forecasting

The system includes advanced demand forecasting using Facebook Prophet:

- **Historical Analysis**: Analyzes past order data to identify trends
- **7-Day Predictions**: Provides weekly demand forecasts
- **Trend Insights**: Generates actionable insights about demand patterns
- **Visual Analytics**: Interactive charts and graphs for data visualization

## 🔐 Security Features

- **Role-Based Access**: Strict separation between supplier and vendor functionalities
- **Order Validation**: Prevents unauthorized order modifications
- **CSRF Protection**: Built-in Django CSRF protection
- **Input Sanitization**: Secure form handling and data validation

## 📁 Project Structure

```
vsm/
├── manage.py
├── db.sqlite3
├── vsm/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── inventory/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    ├── forecast_utils.py
    ├── tests.py
    └── templates/
        └── inventory/
            ├── home.html
            ├── login.html
            ├── signup.html
            ├── supplier_dashboard.html
            ├── vendor_dashboard.html
            ├── orders.html
            └── forecast.html
```

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

## 🔄 API Endpoints

The system provides RESTful APIs for:
- User authentication and management
- Inventory operations
- Order processing
- Demand forecasting
- Rating management

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- Demand forecasting requires minimum 5 historical orders for accurate predictions
- Custom commodities are case-sensitive
- Time zone handling may need adjustment for global deployment

## 🚀 Future Enhancements

- [ ] Real-time notifications system
- [ ] Advanced analytics dashboard
- [ ] Mobile app development
- [ ] Integration with payment gateways
- [ ] Multi-language support
- [ ] Export functionality for reports
- [ ] Advanced ML models for better forecasting



## 🙏 Acknowledgments

- Facebook Prophet team for the forecasting library
- Django community for the excellent framework
- Contributors and beta testers

---
