# Cloud Architecture Visualization

A Python script that creates interactive visualizations of cloud architecture components and their relationships.

## 🌐 Live Demo

View the interactive visualization here: [GitHub Pages](https://evepavliy.github.io/cloud-architecture-visualization/)

## 📋 Features

- **Interactive Visualization**: Click and drag nodes to explore the architecture
- **Static Diagram**: High-resolution PNG export for documentation
- **Web-Ready**: Automatically generates HTML for GitHub Pages deployment
- **Professional Styling**: Clean, modern interface with component descriptions

## 🏗️ Architecture Components

The visualization includes common cloud infrastructure components:

- **Users**: External clients accessing the system
- **CDN**: Content Delivery Network for static assets
- **Load Balancer**: Distributes incoming requests
- **Web Servers**: Handle HTTP requests (redundant setup)
- **App Server**: Business logic processing
- **Database**: Persistent data storage
- **Redis Cache**: Fast data retrieval
- **File Storage**: File storage system
- **API Gateway**: API management and routing

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/evepavliy/cloud-architecture-visualization.git
cd cloud-architecture-visualization
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

Run the script to generate both static and interactive visualizations:

```bash
python cloud_architecture_viz.py
```

The script will:
- Generate a static PNG diagram
- Create an interactive HTML visualization in the `docs/` folder
- Automatically open the visualization in your browser

## 📁 Project Structure

```
.
├── cloud_architecture_viz.py  # Main visualization script
├── requirements.txt           # Python dependencies
├── docs/                     # GitHub Pages content
│   └── index.html            # Interactive visualization
└── README.md                 # This file
```

## 🔧 Customization

You can modify the architecture by editing the `nodes` and `edges` dictionaries in the `create_interactive_visualization()` function:

```python
# Add new components
nodes = {
    'new_component': {'pos': (x, y), 'color': '#color', 'size': 25},
    # ... existing nodes
}

# Add new connections
edges = [
    ('source', 'destination'),
    # ... existing edges
]
```

## 📊 Output Files

- **Static PNG**: High-resolution diagram saved to temp directory
- **Interactive HTML**: Web-ready visualization in `docs/index.html`

## 🌐 GitHub Pages Deployment

The repository is configured for GitHub Pages deployment:

1. Push your changes to the `main` branch
2. Go to repository Settings → Pages
3. Select "Deploy from a branch"
4. Choose `main` branch and `/docs` folder
5. Your visualization will be available at `https://evepavliy.github.io/cloud-architecture-visualization/`

## 🛠️ Dependencies

- `matplotlib` >= 3.5.0 - Static diagram generation
- `networkx` >= 2.8.0 - Graph structure and algorithms
- `plotly` >= 5.0.0 - Interactive web visualizations

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📧 Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/your-repo-name](https://github.com/yourusername/your-repo-name)
