import cherrypy
import matplotlib.pyplot as plt
import io
import base64

class PlotServer:
    @cherrypy.expose
    def index(self):
        return """
        <html>
            <head><title>Welcome</title></head>
            <body>
                <h2>Welcome to the Plot Server</h2>
                <a href="plot">Go to Plot Page</a>
            </body>
        </html>
        """

    @cherrypy.expose
    def plot(self):
        return """
        <html>
            <head><title>Plot Page</title></head>
            <body>
                <h2>Enter X and Y values to plot</h2>
                <form method="get" action="generate_plot">
                    <label for="x">X values (comma separated):</label>
                    <input type="text" id="x" name="x" />
                    <br>
                    <label for="y">Y values (comma separated):</label>
                    <input type="text" id="y" name="y" />
                    <br>
                    <button type="submit">Plot</button>
                </form>
            </body>
        </html>
        """

    @cherrypy.expose
    def generate_plot(self, x, y):
        x_values = list(map(int, x.split(',')))
        y_values = list(map(int, y.split(',')))

        plt.figure()
        plt.plot(x_values, y_values, marker='o')
        plt.title('X vs Y Plot')
        plt.xlabel('X values')
        plt.ylabel('Y values')

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        return f"""
        <html>
            <head><title>Plot Result</title></head>
            <body>
                <h2>Plot Result</h2>
                <img src="data:image/png;base64,{plot_url}" />
                <br>
                <a href="plot">Go back</a>
            </body>
        </html>
        """

if __name__ == "__main__":
    cherrypy.quickstart(PlotServer())