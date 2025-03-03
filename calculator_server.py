import cherrypy

class Calculator:
    @cherrypy.expose
    def index(self):
        return """
        <html>
            <head><title>Calculator</title></head>
            <body>
                <h2>Simple Integer Calculator</h2>
                <form method="get" action="calculate">
                    <input type="text" name="a" />
                    <select name="operation">
                        <option value="add">+</option>
                        <option value="subtract">-</option>
                        <option value="multiply">*</option>
                        <option value="divide">/</option>
                    </select>
                    <input type="text" name="b" />
                    <button type="submit">Calculate</button>
                </form>
                <br>
                <a href="greet">Go to Greeting Page</a>
            </body>
        </html>
        """

    @cherrypy.expose
    def calculate(self, a, b, operation):
        try:
            a = int(a)
            b = int(b)
            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b
            elif operation == "multiply":
                result = a * b
            elif operation == "divide":
                result = a / b
            else:
                result = "Invalid operation"
        except ValueError:
            result = "Invalid input"
        except ZeroDivisionError:
            result = "Division by zero error"

        return f"The result is: {result}"

    @cherrypy.expose
    def greet(self):
        return """
        <html>
            <head><title>Greeting Page</title></head>
            <body>
                <h2>Greeting Page</h2>
                <form method="get" action="greet_user">
                    <input type="text" name="name" placeholder="Enter your name" />
                    <button type="submit">Greet</button>
                </form>
            </body>
        </html>
        """

    @cherrypy.expose
    def greet_user(self, name):
        return f"Hello, {name}!"

if __name__ == "__main__":
    cherrypy.quickstart(Calculator())