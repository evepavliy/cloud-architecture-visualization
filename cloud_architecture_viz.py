#!/usr/bin/env python3
"""
Cloud Architecture Visualization Script

This script creates a simple cloud architecture diagram showing common
cloud components and their relationships, then displays it in a web browser.

Requirements:
- matplotlib
- networkx
- plotly (for interactive web visualization)

Usage:
    python cloud_architecture_viz.py
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import networkx as nx
import plotly.graph_objects as go
import plotly.offline as pyo
import webbrowser
import tempfile
import os
from datetime import datetime

def create_matplotlib_visualization():
    """Create a static visualization using matplotlib"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    
    # Colors for different components
    colors = {
        'user': '#4CAF50',
        'web': '#2196F3',
        'app': '#FF9800',
        'db': '#9C27B0',
        'cache': '#F44336',
        'storage': '#795548',
        'network': '#607D8B'
    }
    
    # Draw cloud boundary
    cloud_rect = patches.Rectangle((0.5, 1), 9, 6, linewidth=2, 
                                 edgecolor='lightblue', facecolor='lightcyan', 
                                 alpha=0.3, linestyle='--')
    ax.add_patch(cloud_rect)
    ax.text(5, 7.5, 'Cloud Infrastructure', fontsize=16, ha='center', 
            weight='bold', color='darkblue')
    
    # Components definition
    components = [
        # (x, y, width, height, label, color_key)
        (1, 0.2, 1.2, 0.6, 'Users', 'user'),
        (1, 5.5, 1.5, 0.8, 'Load Balancer', 'network'),
        (3.5, 6, 1.5, 0.6, 'Web Server 1', 'web'),
        (3.5, 5, 1.5, 0.6, 'Web Server 2', 'web'),
        (6, 5.5, 1.5, 0.8, 'App Server', 'app'),
        (8, 6, 1.2, 0.6, 'Database', 'db'),
        (8, 4.5, 1.2, 0.6, 'Redis Cache', 'cache'),
        (6, 3, 1.5, 0.8, 'File Storage', 'storage'),
        (3.5, 2, 1.5, 0.6, 'API Gateway', 'network'),
        (1, 2.5, 1.5, 0.6, 'CDN', 'network')
    ]
    
    # Draw components
    for x, y, w, h, label, color_key in components:
        rect = patches.Rectangle((x, y), w, h, linewidth=2, 
                               edgecolor='black', facecolor=colors[color_key], 
                               alpha=0.7)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, label, ha='center', va='center', 
                fontsize=9, weight='bold', color='white')
    
    # Draw connections
    connections = [
        # (start_x, start_y, end_x, end_y)
        (1.6, 0.8, 1.7, 5.5),  # Users to Load Balancer
        (2.5, 5.9, 3.5, 6.2),  # Load Balancer to Web Server 1
        (2.5, 5.7, 3.5, 5.2),  # Load Balancer to Web Server 2
        (5, 6.2, 6, 5.9),      # Web Server 1 to App Server
        (5, 5.2, 6, 5.7),      # Web Server 2 to App Server
        (7.5, 5.9, 8, 6.2),    # App Server to Database
        (7.5, 5.7, 8, 4.9),    # App Server to Redis
        (6.7, 5.5, 6.7, 3.8),  # App Server to File Storage
        (1.6, 0.8, 3.5, 2.2),  # Users to API Gateway
        (1.6, 0.8, 1.7, 2.5),  # Users to CDN
        (2.5, 2.8, 3.5, 2.4),  # CDN to API Gateway
        (5, 2.2, 6, 3.2),      # API Gateway to File Storage
    ]
    
    for start_x, start_y, end_x, end_y in connections:
        ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                   arrowprops=dict(arrowstyle='->', lw=1.5, color='darkgray'))
    
    # Add title and labels
    ax.set_title('Simple Cloud Architecture Diagram', fontsize=18, weight='bold', pad=20)
    ax.set_xlabel('Components and Data Flow', fontsize=12)
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Add legend
    legend_elements = [patches.Patch(color=colors[key], label=key.title()) 
                      for key in colors.keys()]
    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.15, 1))
    
    plt.tight_layout()
    return fig

def create_interactive_visualization():
    """Create an interactive visualization using Plotly"""
    
    # Create network graph
    G = nx.DiGraph()
    
    # Add nodes with positions
    nodes = {
        'users': {'pos': (1, 1), 'color': '#4CAF50', 'size': 30},
        'cdn': {'pos': (1, 3), 'color': '#607D8B', 'size': 25},
        'load_balancer': {'pos': (2, 5), 'color': '#607D8B', 'size': 25},
        'web_server_1': {'pos': (4, 6), 'color': '#2196F3', 'size': 25},
        'web_server_2': {'pos': (4, 4), 'color': '#2196F3', 'size': 25},
        'api_gateway': {'pos': (4, 2), 'color': '#607D8B', 'size': 25},
        'app_server': {'pos': (6, 5), 'color': '#FF9800', 'size': 30},
        'database': {'pos': (8, 6), 'color': '#9C27B0', 'size': 30},
        'cache': {'pos': (8, 4), 'color': '#F44336', 'size': 25},
        'storage': {'pos': (6, 2), 'color': '#795548', 'size': 25}
    }
    
    # Add nodes to graph
    for node, attrs in nodes.items():
        G.add_node(node, **attrs)
    
    # Add edges (connections)
    edges = [
        ('users', 'cdn'),
        ('users', 'load_balancer'),
        ('users', 'api_gateway'),
        ('cdn', 'load_balancer'),
        ('load_balancer', 'web_server_1'),
        ('load_balancer', 'web_server_2'),
        ('web_server_1', 'app_server'),
        ('web_server_2', 'app_server'),
        ('app_server', 'database'),
        ('app_server', 'cache'),
        ('app_server', 'storage'),
        ('api_gateway', 'storage'),
        ('api_gateway', 'app_server')
    ]
    
    G.add_edges_from(edges)
    
    # Extract positions and colors
    pos = nx.get_node_attributes(G, 'pos')
    colors = [nodes[node]['color'] for node in G.nodes()]
    sizes = [nodes[node]['size'] for node in G.nodes()]
    
    # Create edge traces
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
    
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='#888'),
        hoverinfo='none',
        mode='lines'
    )
    
    # Create node traces
    node_x = [pos[node][0] for node in G.nodes()]
    node_y = [pos[node][1] for node in G.nodes()]
    
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        text=[node.replace('_', ' ').title() for node in G.nodes()],
        textposition="middle center",
        textfont=dict(size=10, color='white'),
        marker=dict(
            size=sizes,
            color=colors,
            line=dict(width=2, color='black')
        )
    )
    
    # Create the figure
    fig = go.Figure(data=[edge_trace, node_trace],
                   layout=go.Layout(
                       title=dict(
                           text='Interactive Cloud Architecture Visualization',
                           x=0.5,
                           font=dict(size=20)
                       ),
                       showlegend=False,
                       hovermode='closest',
                       margin=dict(b=20,l=5,r=5,t=40),
                       annotations=[
                           dict(
                               text="Click and drag to explore the architecture",
                               showarrow=False,
                               xref="paper", yref="paper",
                               x=0.005, y=-0.002,
                               xanchor="left", yanchor="bottom",
                               font=dict(color="gray", size=12)
                           )
                       ],
                       xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       plot_bgcolor='white'
                   ))
    
    return fig

def main():
    """Main function to create and display the visualization"""
    print("🚀 Creating Cloud Architecture Visualization...")
    
    try:
        # Create matplotlib version
        print("📊 Generating static diagram...")
        fig_static = create_matplotlib_visualization()
        
        # Save static version
        static_file = os.path.join(tempfile.gettempdir(), 'cloud_architecture_static.png')
        fig_static.savefig(static_file, dpi=300, bbox_inches='tight')
        print(f"💾 Static diagram saved to: {static_file}")
        
        # Create interactive version
        print("🌐 Generating interactive diagram...")
        fig_interactive = create_interactive_visualization()
        
        # Save interactive version as HTML for GitHub Pages
        html_file = os.path.join(os.getcwd(), 'docs', 'index.html')
        
        # Ensure docs directory exists
        os.makedirs(os.path.dirname(html_file), exist_ok=True)
        
        # Add custom HTML styling
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Cloud Architecture Visualization</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                    background-color: #f5f5f5;
                }}
                .header {{
                    text-align: center;
                    color: #333;
                    margin-bottom: 20px;
                }}
                .info {{
                    background-color: white;
                    padding: 15px;
                    border-radius: 5px;
                    margin-bottom: 20px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                }}
                .chart-container {{
                    background-color: white;
                    border-radius: 5px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                    padding: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>☁️ Cloud Architecture Visualization</h1>
                <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
            
            <div class="info">
                <h3>📋 Architecture Components:</h3>
                <ul>
                    <li><strong>Users:</strong> External clients accessing the system</li>
                    <li><strong>CDN:</strong> Content Delivery Network for static assets</li>
                    <li><strong>Load Balancer:</strong> Distributes incoming requests</li>
                    <li><strong>Web Servers:</strong> Handle HTTP requests</li>
                    <li><strong>App Server:</strong> Business logic processing</li>
                    <li><strong>Database:</strong> Persistent data storage</li>
                    <li><strong>Cache:</strong> Redis for fast data retrieval</li>
                    <li><strong>Storage:</strong> File storage system</li>
                    <li><strong>API Gateway:</strong> API management and routing</li>
                </ul>
            </div>
            
            <div class="chart-container">
                {pyo.plot(fig_interactive, output_type='div', include_plotlyjs=True)}
            </div>
        </body>
        </html>
        """
        
        with open(html_file, 'w') as f:
            f.write(html_content)
        
        print(f"💾 Interactive diagram saved to: {html_file}")
        
        # Open in browser
        print("🌐 Opening visualization in browser...")
        webbrowser.open(f'file://{html_file}')
        
        print("✅ Visualization created successfully!")
        print(f"📁 Files created:")
        print(f"   - Static PNG: {static_file}")
        print(f"   - Interactive HTML: {html_file}")
        
    except ImportError as e:
        print(f"❌ Missing required library: {e}")
        print("📦 Please install required packages:")
        print("   pip install matplotlib networkx plotly")
    except Exception as e:
        print(f"❌ Error creating visualization: {e}")

if __name__ == "__main__":
    main()
