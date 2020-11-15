#Se importó la libreria de MANIM
from manimlib.imports import *


# Clase para el método de la bisección
class Biseccion(GraphScene):

    # Se realiza la configuración de la gráfica
    CONFIG = {
    # Valor máximo de y en la gráfica
    "y_max" : 6,
    # Valor mínimo de y en la gráfica
    "y_min" : -6,
    # Valor máximo de x en la gráfica
    "x_max" : 6,
    # Valor mínimo de x en la gráfica
    "x_min" : -6,
    # Se define el color de los ejes
    "axes_color" : BLUE,
    # Se define nombre para el eje horizontal
    "x_axis_label" : "$x$",
    # Se define nombre para el eje vertical
    "y_axis_label" : "$f(x)$",
    # Se define la posición en la que quiere que se genere la gráfica
    "graph_origin" : np.array((0,0,0))
}

    # Bloque de construcción de la animación
    def construct(self):
        # Título correspondiente al método presente
        titulo = TextMobject("Método de la bisección")
        # Ecuación correspondiente al método presente
        ecuacion = TexMobject(
            r"\frac{b+a}{2}"
        )
        # Misma ecuación que la anterior pero que se posicionará en una esquina
        ecuaesq = TexMobject(
            r"\frac{b+a}{2}"
        )
        # Se coloca la ecuaión en la esquina derecha superior
        ecuaesq.to_corner(UP+RIGHT)
        # Se escribe el título
        self.play(Write(titulo))
        # Se espera un tiempo con esta animación
        self.wait()
        # Se transforma el título en la ecuación
        self.play(Transform(titulo,ecuacion))
        # Se espera un tiempo con esta animación
        self.wait()
        # Se transforma la euación en la ecuación esquinera
        self.play(Transform(titulo,ecuaesq))

        # Se llama a la función que define los ejes
        self.setup_axes()
        # Se define la gráfica que se desea mostrar y de color verde
        graph = self.get_graph(lambda x : np.cos(x) - x, color = GREEN)
        # Se muestra la gráfica
        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        # Se espera un tiempo con esta animación
        self.wait()


        #Se define el nombre que se le quiere poner a este punto
        puntoa1 = TexMobject("x_{a_{1}}")
        # Se define la coordenada en el gráfico
        label_coord = self.input_to_graph_point(-3,graph)
        # Se indica la coordnada donde debe colocarse el nombre
        puntoa1.next_to(label_coord,RIGHT+DOWN)
        # Se define el nombre que se le quiere poner a este punto
        puntob1 = TexMobject("x_{b_{1}}")
        # Se define la coordenada en el gráfico
        label_coord2 = self.input_to_graph_point(3,graph)
        # Se indica la coordnada donde debe colocarse el nombre
        puntob1.next_to(label_coord2,RIGHT+UP)

        # Se definen las coordenadas para el punto
        dota1 = Dot(self.coords_to_point(-3,2.01))
        # Se definen las coordenadas para el punto
        dotb1 = Dot(self.coords_to_point(3,-3.989992))

        # Se añaden los puntos
        self.add(dota1,dotb1)
        # Se añaden los nombres que se le dieron a los puntos
        self.play(ShowCreation(puntoa1) ,ShowCreation(puntob1))

        # Se define la ecuación que se realiza en ese instante
        res1 = TexMobject(
            r"\frac{3+(-3)}{2}=0"
        )
        # Se le da de ubicación de la esquina derecha superior a la ecuación
        res1.to_corner(UP+RIGHT)
        # Se transforma la ecuación anterior en la deseada
        self.play(Transform(titulo,res1))

        # Se espera un tiempo con esta animación
        self.wait()

        # Se define el nombre que se le quiere poner a este punto
        puntoa2 = TexMobject("x_{a_{2}}")
        # Se define la coordenada en el gráfico
        label_coord = self.input_to_graph_point(0,graph)
        # Se indica la coordnada donde debe colocarse el nombre
        puntoa2.next_to(label_coord,RIGHT+UP)
        # Se define el nombre que se le quiere poner a este punto
        puntob2 = TexMobject("x_{b_{2}}")
        # Se define la coordenada en el gráfico
        label_coord2 = self.input_to_graph_point(3,graph)
        # Se indica la coordnada donde debe colocarse el nombre
        puntob2.next_to(label_coord2,RIGHT+UP)

        # Se definen las coordenadas para el punto
        dota2 = Dot(self.coords_to_point(0,1))
        # Se definen las coordenadas para el punto
        dotb2 = Dot(self.coords_to_point(3,-3.989992))

        # Se remueven los puntos
        self.remove(dota1,dotb1)
        # Se añaden los puntos
        self.add(dota2,dotb2)
        # Se cambia el nombre de los puntos anteriores por los que corresponden
        self.play(Transform(puntoa1,puntoa2), Transform(puntob1,puntob2))

        # Se define la ecuación que se realiza en ese instante
        res2 = TexMobject(
            r"\frac{3+0}{2}=1.5"
        )
        # Se le da de ubicación de la esquina derecha superior a la ecuación
        res2.to_corner(UP+RIGHT)
        # Se transforma la ecuación anterior en la deseada
        self.play(Transform(titulo,res2))

        # Se espera un tiempo con esta animación
        self.wait()

        # Se define el nombre que se le quiere poner a este punto
        puntoa3 = TexMobject("x_{a_{3}}")
        # Se define la coordenada en el gráfico
        label_coord = self.input_to_graph_point(0,graph)
        # Se indica la coordnada donde debe colocarse el nombre
        puntoa3.next_to(label_coord,RIGHT+UP)
        # Se define el nombre que se le quiere poner a este punto
        puntob3 = TexMobject("x_{b_{3}}")
        # Se define la coordenada en el gráfico
        label_coord2 = self.input_to_graph_point(1.5,graph)
        # Se indica la coordnada donde debe colocarse el nombre
        puntob3.next_to(label_coord2,RIGHT+DOWN)

        # Se definen las coordenadas para el punto
        dota3 = Dot(self.coords_to_point(0,1))
        # Se definen las coordenadas para el punto
        dotb3 = Dot(self.coords_to_point(1.5,-1.429262))

        # Se remueven los puntos
        self.remove(dota2,dotb2)
        # Se añaden los puntos
        self.add(dota3,dotb3)
        # Se cambia el nombre de los puntos anteriores por los que corresponden
        self.play(Transform(puntoa1,puntoa3), Transform(puntob1,puntob3))

        # Se define la ecuación que se realiza en ese instante
        res3 = TexMobject(
            r"\frac{1.5+0}{2}=0.75"
        )
        # Se le da de ubicación de la esquina derecha superior a la ecuación
        res3.to_corner(UP+RIGHT)
        # Se transforma la ecuación anterior en la deseada
        self.play(Transform(titulo,res3))

        # Se espera un tiempo con esta animación
        self.wait()

        # Se define el nombre que se le quiere poner a este punto
        puntoa4 = TexMobject("x_{a_{4}}")
        # Se define la coordenada en el gráfico
        label_coord = self.input_to_graph_point(0,graph)
        # Se indica la coordnada donde debe colocarse el nombre
        puntoa4.next_to(label_coord,RIGHT+UP)
        # Se define el nombre que se le quiere poner a este punto
        puntob4 = TexMobject("x_{b_{4}}")
        # Se define la coordenada en el gráfico
        label_coord2 = self.input_to_graph_point(0.75,graph)
        # Se indica la coordnada donde debe colocarse el nombre
        puntob4.next_to(label_coord2,RIGHT+UP)

        # Se definen las coordenadas para el punto
        dota4 = Dot(self.coords_to_point(0,1))
        # Se definen las coordenadas para el punto
        dotb4 = Dot(self.coords_to_point(0.75,-0.0183111))

        self.remove(dota3,dotb3)
        # Se añaden los puntos
        self.add(dota4,dotb4)
        # Se cambia el nombre de los puntos anteriores por los que corresponden
        self.play(Transform(puntoa1,puntoa4), Transform(puntob1,puntob4))

        # Se define la ecuación que se realiza en ese instante
        res4 = TexMobject(
            r"\frac{0.75+0}{2}=0.375"
        )
        # Se le da de ubicación de la esquina derecha superior a la ecuación
        res4.to_corner(UP+RIGHT)
        # Se transforma la ecuación anterior en la deseada
        self.play(Transform(titulo,res4))

        # Se espera un tiempo con esta animación
        self.wait()

        # Se define el nombre que se le quiere poner a este punto
        puntoa5 = TexMobject("x_{a_{5}}")
        # Se define la coordenada en el gráfico
        label_coord = self.input_to_graph_point(0.375,graph)
        # Se indica la coordnada donde debe colocarse el nombre
        puntoa5.next_to(label_coord,RIGHT+UP)
        # Se define el nombre que se le quiere poner a este punto
        puntob5 = TexMobject("x_{b_{5}}")
        # Se define la coordenada en el gráfico
        label_coord2 = self.input_to_graph_point(0.75,graph)
        # Se indica la coordnada donde debe colocarse el nombre
        puntob5.next_to(label_coord2,RIGHT+UP)

        # Se definen las coordenadas para el punto
        dota5 = Dot(self.coords_to_point(0.375,0.5555076))
        # Se definen las coordenadas para el punto
        dotb5 = Dot(self.coords_to_point(0.75,-0.0183111))

        # Se remueven los puntos
        self.remove(dota4,dotb4)
        # Se añaden los puntos
        self.add(dota5,dotb5)
        # Se cambia el nombre de los puntos anteriores por los que corresponden
        self.play(Transform(puntoa1,puntoa5), Transform(puntob1,puntob5))

        # Se define la ecuación que se realiza en ese instante
        res5 = TexMobject(
            r"\frac{0.375+0.75}{2}=0.5625"
        )
        # Se le da de ubicación de la esquina derecha superior a la ecuación
        res5.to_corner(UP+RIGHT)
        # Se transforma la ecuación anterior en la deseada
        self.play(Transform(titulo,res5))

        # Se espera un tiempo con esta animación
        self.wait(3)

        # Se define el nombre que se le quiere poner a este punto
        puntoan = TexMobject("x_{a_{n}}")
        # Se define la coordenada en el gráfico
        label_coord = self.input_to_graph_point(0.739,graph)
        # Se indica la coordnada donde debe colocarse el nombre
        puntoan.next_to(label_coord,RIGHT+UP)
        # Se le asigna un tamaño menor al punto
        puntoan.scale(0.75)
        # Se define el nombre que se le quiere poner a este punto
        puntobn = TexMobject("x_{b_{n}}")
        # Se define la coordenada en el gráfico
        label_coord2 = self.input_to_graph_point(0.739,graph)
        # Se indica la coordnada donde debe colocarse el nombre
        puntobn.next_to(label_coord2,RIGHT+DOWN)
        # Se le asigna un tamaño menor al punto
        puntobn.scale(0.75)
        # Se definfe las coordenadas para el punto y se le define color amarillo
        dotan = Dot(self.coords_to_point(0.739,0.000142477), color=YELLOW)

        # Se remueven los puntos
        self.remove(dota5,dotb5)
        # Se añaden el punto
        self.add(dotan)
        # Se cambia el nombre de los puntos anteriores por los que corresponden
        self.play(Transform(puntoa1,puntoan), Transform(puntob1,puntobn))

        # Se define la ecuación que se realiza en ese instante
        resn = TexMobject(
            r"\frac{0.739+0.739}{2}=0.739 ; n=19"
        )
        # Se le asigna un tamaño menor a la ecuación
        resn.scale(0.75)
        # Se coloca la ecuación en la esquina derecha superior
        resn.to_corner(UP+RIGHT)
        # Se transforma la ecuación anterior en la deseada
        self.play(Transform(titulo,resn))

        # Se espera un tiempo con esta animación
        self.wait()

    # Función en la que se definen los ejes
    def setup_axes(self):
        # Agregar estos ejes a la gráfica
        GraphScene.setup_axes(self)
        # Parametros para las etiquetas
        #   Para x
        init_label_x = -6
        end_label_x = 6
        step_x = 1
        #   Para y
        init_label_y = 6
        end_label_y = -6
        step_y = 1
        # Posiciones para las etiquetas
        #   Para x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   Para y
        self.y_axis.label_direction = LEFT
        # Agregar etiquetas a la gráfica
        #   Para x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   Para y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #   Se agrega la animación
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )

# Clase para el método de la regla falsa
class Reglaf(GraphScene):

    # Se realiza la configuración de la gráfica
    CONFIG = {
    # Se establece el valor máximo del eje y
    "y_max" : 4,
    # Se establece el valor mínimo del eje y
    "y_min" : -4,
    # Se establece el valor máximo del eje x
    "x_max" : 1.5,
    # Se establece el valor mínimo del eje x
    "x_min" : -1.5,
    # Se establece el clor de los ejes
    "axes_color" : BLUE,
    # Se le da nombre al eje horizontal
    "x_axis_label" : "$x$",
    # Se le da nombre al eje vertical
    "y_axis_label" : "$f(x)$",
    # Se define la posición en la que quiere que se genere la gráfica
    "graph_origin" : np.array((-2.5,-0.5,0))
}
    # Bloque de construcción de la máquina
    def construct(self):
        # Título correspondiente al método presente
        titulo = TextMobject("Método de la regla falsa")
        # Ecuación correspondiente al método presente
        ecuacion = TexMobject(
            r"x_{a}= x_{b}-\frac{f(x_{b})(x_{a}-x_{b})}{f(x_a)-f(x_{b})}"
        )
        # Condición extra del método
        cond = TexMobject(
            r"f(x_a)\cdot f(x_{b})<0"
        )
        # Se mueve dos espacios hacia arriba la ecuación para que no se
        #sobrepongan
        ecuacion.move_to(UP*2)
        # Misma ecuación que la anterior pero que se posicionará en una esquina
        ecuaesq=TexMobject(
            r"x_{a}= x_{b}-\frac{f(x_{b})(x_{a}-x_{b})}{f(x_a)-f(x_{b})}"
        )
        # Se coloca la ecuaión en la esquina derecha superior
        ecuaesq.to_corner(UP+RIGHT)

        # Se escribe el título
        self.play(Write(titulo))
        # Se espera un tiempo con esta animación
        self.wait()
        # Se define como un grupo el título y la condición con cierto espacio
        VGroup(titulo, cond).arrange(DOWN*5)
        # Se transforma el título en la ecuación y aparece la condición
        self.play(Transform(titulo,ecuacion),FadeInFrom(cond, UP),)
        # Se espera un tiempo con esta animación
        self.wait()
        # Se transforma la ecuación en la ecuación esquinera y se quita la condición
        self.play(Transform(titulo,ecuaesq),LaggedStart(*map(FadeOutAndShiftDown, cond)),)

        # Se llama a la función que define los ejes
        self.setup_axes()
        #Se define la curva que se desea mostrar y el color
        graph = self.get_graph(lambda x : 3*(x**3) + 2*x + 2, color = GREEN)

        # Se define los nombre para los puntos y las ubicaciones
        puntoa1 = TexMobject("x_{a_{1}}")
        label_coord = self.input_to_graph_point(-1,graph)
        puntoa1.next_to(label_coord,RIGHT+DOWN)
        puntob1 = TexMobject("x_{b_{1}}")
        label_coord2 = self.input_to_graph_point(-0.5,graph)
        puntob1.next_to(label_coord2,RIGHT+UP)
        puntom1 = TexMobject("x_{M_{1}}", color=RED)
        label_coord = self.input_to_graph_point(-0.58621,graph)
        puntom1.next_to(label_coord,RIGHT+DOWN)

        # Se le da las ubicaciones a los puntos
        dota1 = Dot(self.coords_to_point(-1,-3))
        dotb1 = Dot(self.coords_to_point(-0.5,0.625))
        dotm1 = Dot(self.coords_to_point(-0.5862068966,0.223256361), color=RED)

        # Se define la recta que pasa por los puntos
        recta1 = self.get_graph(lambda x : 7.25*x + 4.25, color = RED)

        # Se muestra la curva en la gráfica
        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        # Se añaden los puntos
        self.add(dota1,dotb1)
        # Se muestran los nombres de los puntos
        self.play(ShowCreation(puntoa1) ,ShowCreation(puntob1))
        # Se muestra la recta en la gráfica
        self.play(ShowCreation(recta1), run_time=2)
        # Se añaden los puntos
        self.add(dotm1)
        # Se muestra el nombre del punto correspondiente
        self.play(ShowCreation(puntom1))

        # Se espera un tiempo con esta animación
        self.wait()

        # Se define los nombre para los puntos y las ubicaciones
        puntoa2 = TexMobject("x_{a_{2}}")
        label_coord = self.input_to_graph_point(-1,graph)
        puntoa2.next_to(label_coord,RIGHT+DOWN)
        puntob2 = TexMobject("x_{b_{2}}")
        label_coord2 = self.input_to_graph_point(-0.586206966,graph)
        puntob2.next_to(label_coord2,LEFT+UP)
        puntom2 = TexMobject("x_{M_{2}}", color=RED)
        label_coord = self.input_to_graph_point(-0.58621,graph)
        puntom2.next_to(label_coord,RIGHT+UP)

        # Se le da las ubicaciones a los puntos
        dota2 = Dot(self.coords_to_point(-1,-3))
        dotb2 = Dot(self.coords_to_point(-0.5862068966,0.2232563861))
        dotm2 = Dot(self.coords_to_point(-0.61488,0.072823), color=RED)

        # Se define la recta que pasa por los puntos
        recta2 = self.get_graph(lambda x : (7.78959)*x + (4.78959) , color = RED)

        # Se remueven los puntos
        self.remove(dota1,dotb1,dotm1)
        # Se añaden los puntos
        self.add(dota2,dotb2)
        #  Se tranforma los nombres de los puntos por los que se desea
        self.play(Transform(puntoa1,puntoa2), Transform(puntob1,puntob2))
        # Se transforma la recta pasada en la necesaria
        self.play(Transform(recta1,recta2))
        # Se añaden los puntos
        self.add(dotm2)
        # Se tranforma los nombres de los puntos por los que se desea
        self.play(Transform(puntom1,puntom2))

        # Se espera un tiempo con esta animación
        self.wait()

        # Se define los nombre para los puntos y las ubicaciones
        puntoa3 = TexMobject("x_{a_{3}}")
        label_coord = self.input_to_graph_point(-1,graph)
        puntoa3.next_to(label_coord,RIGHT+DOWN)
        puntob3 = TexMobject("x_{b_{3}}")
        label_coord3 = self.input_to_graph_point(-0.61488,graph)
        puntob3.next_to(label_coord2,LEFT+UP)
        puntom3 = TexMobject("x_{M_{3}}", color=RED)
        label_coord = self.input_to_graph_point(-0.62400,graph)
        puntom3.next_to(label_coord,RIGHT+UP)

        # Se le da las ubicaciones a los puntos
        dota3 = Dot(self.coords_to_point(-1,-3))
        dotb3 = Dot(self.coords_to_point(-0.61488,0.072823))
        dotm3 = Dot(self.coords_to_point(-0.62400,0.02307), color=RED)

        # Se define la recta que pasa por los puntos
        recta3 = self.get_graph(lambda x : (7.97887)*x + (4.97887) , color = RED)

        # Se remueven los puntos
        self.remove(dota2,dotb2,dotm2)
        # Se añaden los puntos
        self.add(dota3,dotb3)
        # Se tranforma los nombres de los puntos por los que se desea
        self.play(Transform(puntoa1,puntoa3), Transform(puntob1,puntob3))
        # Se transforma la recta pasada en la necesaria
        self.play(Transform(recta1,recta3))
        # Se añaden los puntos
        self.add(dotm3)
        # Se tranforma los nombres de los puntos por los que se desea
        self.play(Transform(puntom1,puntom3))

        # Se espera un tiempo con esta animación
        self.wait()

        # Se define los nombre para los puntos y las ubicaciones
        puntoa4 = TexMobject("x_{a_{4}}")
        label_coord = self.input_to_graph_point(-1,graph)
        puntoa4.next_to(label_coord,RIGHT+DOWN)
        puntob4 = TexMobject("x_{b_{4}}")
        label_coord2 = self.input_to_graph_point(-0.62400,graph)
        puntob4.next_to(label_coord2,LEFT+UP)
        puntom4 = TexMobject("x_{M_{4}}", color=RED)
        label_coord = self.input_to_graph_point(-0.62687,graph)
        puntom4.next_to(label_coord,RIGHT+UP)

        # Se le da las ubicaciones a los puntos
        dota4 = Dot(self.coords_to_point(-1,-3))
        dotb4 = Dot(self.coords_to_point(-0.62400,0.02307))
        dotm4 = Dot(self.coords_to_point(-0.62687,0.00722), color=RED)

        # Se define la recta que pasa por los puntos
        recta4 = self.get_graph(lambda x : (8.04007)*x + (5.04007) , color = RED)

        # Se remueven los puntos
        self.remove(dota3,dotb3,dotm3)
        # Se añaden los puntos
        self.add(dota4,dotb4)
        # Se tranforma los nombres de los puntos por los que se desea
        self.play(Transform(puntoa1,puntoa4), Transform(puntob1,puntob4))
        # Se transforma la recta pasada en la necesaria
        self.play(Transform(recta1,recta4))
        # Se añaden los puntos
        self.add(dotm4)
        # Se tranforma los nombres de los puntos por los que se desea
        self.play(Transform(puntom1,puntom4))

        # Se espera un tiempo con esta animación
        self.wait()

        # Se define los nombre para los puntos y las ubicaciones
        puntoa5 = TexMobject("x_{a_{5}}")
        label_coord = self.input_to_graph_point(-1,graph)
        puntoa5.next_to(label_coord,RIGHT+DOWN)
        puntob5 = TexMobject("x_{b_{5}}")
        label_coord2 = self.input_to_graph_point(-0.62687,graph)
        puntob5.next_to(label_coord2,LEFT+UP)
        puntom5 = TexMobject("x_{M_{5}}", color=RED)
        label_coord = self.input_to_graph_point(-0.62777,graph)
        puntom5.next_to(label_coord,RIGHT+UP)

        # Se le da las ubicaciones a los puntos
        dota5 = Dot(self.coords_to_point(-1,-3))
        dotb5 = Dot(self.coords_to_point(-0.62687,0.00722))
        dotm5 = Dot(self.coords_to_point(-0.62777,0.00225), color=RED)

        # Se define la recta que pasa por los puntos
        recta5 = self.get_graph(lambda x : (8.05944)*x + (5.05944) , color = RED)

        # Se remueven los puntos
        self.remove(dota4,dotb4,dotm4)
        # Se añaden los puntos
        self.add(dota5,dotb5)
        # Se tranforma los nombres de los puntos por los que se desea
        self.play(Transform(puntoa1,puntoa5), Transform(puntob1,puntob5))
        # Se transforma la recta pasada en la necesaria
        self.play(Transform(recta1,recta5))
        # Se añaden los puntos
        self.add(dotm5)
        # Se tranforma los nombres de los puntos por los que se desea
        self.play(Transform(puntom1,puntom5))

        # Se espera un tiempo con esta animación
        self.wait()

        # Se define los nombre para los puntos y las ubicaciones
        puntoa6 = TexMobject("x_{a_{6}}")
        label_coord = self.input_to_graph_point(-1,graph)
        puntoa6.next_to(label_coord,RIGHT+DOWN)
        puntob6 = TexMobject("x_{b_{6}}")
        label_coord2 = self.input_to_graph_point(-0.62777,graph)
        puntob6.next_to(label_coord2,LEFT+UP)
        puntom6 = TexMobject("x_{M_{6}}", color=RED)
        label_coord = self.input_to_graph_point(-0.62805,graph)
        puntom6.next_to(label_coord,RIGHT+UP)

        # Se le da las ubicaciones a los puntos
        dota6 = Dot(self.coords_to_point(-1,-3))
        dotb6 = Dot(self.coords_to_point(-0.62777,0.00225))
        dotm6 = Dot(self.coords_to_point(-0.62805,0.000703), color=RED)

        # Se define la recta que pasa por los puntos
        recta6 = self.get_graph(lambda x : (8.06557)*x + (5.06557) , color = RED)

        # Se remueven los puntos
        self.remove(dota5,dotb5,dotm5)
        # Se añaden los puntos
        self.add(dota6,dotb6)
        # Se tranforma los nombres de los puntos por los que se desea
        self.play(Transform(puntoa1,puntoa6), Transform(puntob1,puntob6))
        # Se transforma la recta pasada en la necesaria
        self.play(Transform(recta1,recta6))
        # Se añaden los puntos
        self.add(dotm6)
        # Se tranforma los nombres de los puntos por los que se desea
        self.play(Transform(puntom1,puntom6))

        # Se espera un tiempo con esta animación
        self.wait()

    # Función en la que se definen los ejes
    def setup_axes(self):
        # Agregar estos ejes a la gráfica
        GraphScene.setup_axes(self)
        # Parametros para las etiquetas
        #   Para x
        init_label_x = -1
        end_label_x = 1
        step_x = 1
        #   Para y
        init_label_y = -4
        end_label_y = 4
        step_y = 1
         # Posiciones para las etiquetas
        #   Para x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   Para y
        self.y_axis.label_direction = LEFT
        # Agregar etiquetas a la gráfica
        #   Para x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
         #   Para y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #   Se agrega la animación
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )

# Clase para el método de Newton Raphson
class NewtonR(GraphScene,MovingCameraScene):

    # Se realiza la configuración de la gráfica
    CONFIG = {
    # Valor máximo de y en la gráfica
    "y_max" : 16,
    # Valor mínimo de y en la gráfica
    "y_min" : -2,
    # Valor máximo de x en la gráfica
    "x_max" : 5,
    # Valor mínimo de x en la gráfica
    "x_min" : -1,
    # Se define el color de los ejes
    "axes_color" : BLUE,
    # Se define nombre para el eje horizontal
    "x_axis_label" : "$x$",
    # Se define nombre para el eje vertical
    "y_axis_label" : "$f(x)$",
    # Se define la posición en la que quiere que se genere la gráfica
    "graph_origin" : np.array((-4.5,-2.5,0))
}
    # Bloque que servirá para lograr el zoom
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    # Bloque de construcción de la animación
    def construct(self):
        # Título correspondiente al método presente
        titulo = TextMobject("Método de Newton-Raphson")
        # Ecuación correspondiente al método presente
        ecuacion = TexMobject(
            r"x_{i+1}= x_{i}-\frac{f(x_{i})}{f'(x_{i})}}"
        )
        # Misma ecuación que la anterior pero que se posicionará en una esquina
        ecuaesq=TexMobject(
            r"x_{i+1}= x_{i}-\frac{f(x_{i})}{f'(x_{i})}}"
        )
        # Se coloca la ecuaión en la esquina derecha superior
        ecuaesq.to_corner(UP+RIGHT)

        # Se escribe el título
        self.play(Write(titulo))
        # Se espera un tiempo con esta animación
        self.wait()
        # Se transforma el título en la ecuación
        self.play(Transform(titulo,ecuacion))
        # Se espera un tiempo con esta animación
        self.wait()
        # Se transforma la euación en la ecuación esquinera
        self.play(Transform(titulo,ecuaesq))

        # Se llama a la función que define los ejes
        self.setup_axes()
        # Se define la curva que se desea mostra en la gráfica
        graph = self.get_graph(lambda x : x**2 - 1 , color = GREEN)

        # Se muestra la gráfica
        self.play(ShowCreation(graph))
        # Se espera un tiempo con esta animación
        self.wait()

        # Se define un punto y una línea punteada a él
        dot1 = Dot(self.coords_to_point(4,0))
        vert1 = self.get_vertical_line_to_graph(4,graph, color = WHITE)
        punteada1= DashedVMobject(vert1)


        # Se agrega el punto
        self.add(dot1)
        # Se muestra la línea punteada
        self.play(ShowCreation(punteada1))

        # Se define la recta que pasa por los puntos
        recta1 = self.get_graph(lambda x : 8*x -17 , color = RED)
        # Se muestra la recta
        self.play(ShowCreation(recta1))

        # Se define un punto y una línea punteada a él
        dot2 = Dot(self.coords_to_point(2.125,0))
        # Se agrega el punto
        self.add(dot2)
        # Se espera un tiempo con esta animación
        self.wait()

        # Se define una línea punteada al punto deseado
        vert2 = self.get_vertical_line_to_graph(2.125,graph, color = WHITE)
        punteada2= DashedVMobject(vert2)

        # Se muestra la línea punteada
        self.play(ShowCreation(punteada2))

        # Se define la recta que pasa por los puntos
        recta2 = self.get_graph(lambda x : 4.25*x -5.515625 , color = RED)
        # Se muestra la recta
        self.play(ShowCreation(recta2))

        # Se define en que punto se desea hacer el enfoque
        enfoque = Dot(self.coords_to_point(0.85,0.5))
        # se realiza el enfoque con cierta escala definida
        self.play(
            self.camera_frame.scale,.35,
            self.camera_frame.move_to,enfoque
        )

        # Se define la posción del punto
        dot3 = Dot(self.coords_to_point(1.297794118,0))
        # Se  define el tamaño del punto con cierta escala
        dot3.scale(0.45)
        # Se agrega el punto
        self.add(dot3)
        # Se espera un tiempo con esta animación
        self.wait()

        # Se define una línea punteada al punto deseado
        vert3 = self.get_vertical_line_to_graph(1.297794118,graph, color = WHITE)
        punteada3 = DashedVMobject(vert3)

        # Se muestra la línea punteada
        self.play(ShowCreation(punteada3))

        # Se define la recta que pasa por los puntos
        recta3 = self.get_graph(lambda x : 2.595588*x -2.684269266 , color = RED)
        # Se muestra la recta
        self.play(ShowCreation(recta3))

        # Se define en que punto se desea hacer el enfoque
        enfoque2 = Dot(self.coords_to_point(1.034166157,0))
        # se realiza el enfoque con cierta escala definida
        self.play(
            self.camera_frame.scale,.1,
            self.camera_frame.move_to,enfoque2
        )

        # Se define la posción del punto
        dot4 = Dot(self.coords_to_point(1.034166157,0))
        # Se  define el tamaño del punto con cierta escala
        dot4.scale(0.1)
        # Se agrega el punto
        self.add(dot4)
        # Se espera un tiempo con esta animación
        self.wait()

        # Se define una línea punteada al punto deseado
        vert4 = self.get_vertical_line_to_graph(1.034166157,graph , color = WHITE)
        punteada4 = DashedVMobject(vert4)

        # Se muestra la línea punteada
        self.play(ShowCreation(punteada4))

        # Se crean dos líneas para delimitar
        linea1 = self.get_graph(lambda x : 0.06989 , color = YELLOW)
        linea2 = self.get_graph(lambda x : -0.06989 , color = YELLOW)

        # Se muestran las líneas
        self.play(ShowCreation(linea1),ShowCreation(linea2))

        # Se definen las áreas
        area1 = self.get_area(linea1,0,2)
        area2 = self.get_area(linea2,0,2)

        # Se muestran las áreas definidas
        self.play(ShowCreation(area1),ShowCreation(area2))

        # Se espera un tiempo con esta animación
        self.wait()

    # Función en la que se definen los ejes
    def setup_axes(self):
        # Agregar estos ejes a la gráfica
        GraphScene.setup_axes(self)
        # Parametros para las etiquetas
        #   Para x
        init_label_x = -1
        end_label_x = 5
        step_x = 1
        #   Para y
        init_label_y = 2
        end_label_y = 16
        step_y = 2
        # Posiciones para las etiquetas
        #   Para x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   Para y
        self.y_axis.label_direction = LEFT
        # Agregar etiquetas a la gráfica
        #   Para x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   Para y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #  Se agrega la animación
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )

# Clase para el método de la secante
class Secante(GraphScene,MovingCameraScene):

    # Se realiza la configuración de la gráfica
    CONFIG = {
    # Valor máximo de y en la gráfica
    "y_max" : 16,
    # Valor mínimo de y en la gráfica
    "y_min" : -4,
    # Valor máximo de x en la gráfica
    "x_max" : 5,
    # Valor mínimo de x en la gráfica
    "x_min" : -2,
    # Se define el color de los ejes
    "axes_color" : BLUE,
    # Se define frecuencia de línea en el eje y
    "y_tick_frequency" : 2,
    # Se define nombre para el eje horizontal
    "x_axis_label" : "$x$",
    # Se define nombre para el eje vertical
    "y_axis_label" : "$f(x)$",
    # Se define la posición en la que quiere que se genere la gráfica
    "graph_origin" : np.array((-4.25,-2.25,0))
}

    # Bloque que servirá para lograr el zoom
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    # Bloque de construcción de la animación
    def construct(self):
        # Título correspondiente al método presente
        titulo = TextMobject("Método de la secante")
         # Ecuación correspondiente al método presente
        ecuacion = TexMobject(
            r"x_{i+1}= x_{i}-\frac{(x_{i}-x_{i-1})f(x_{i})}{f(x_{i})-f(x_{i-1})}}"
        )
        # Misma ecuación que la anterior pero que se posicionará en una esquina
        ecuaesq=TexMobject(
            r"x_{i+1}= x_{i}-\frac{(x_{i}-x_{i-1})f(x_{i})}{f(x_{i})-f(x_{i-1})}}"
        )
        # Se coloca la ecuaión en la esquina derecha superior
        ecuaesq.to_corner(UP+RIGHT)
        # Se mueve la ecuación esquinera hacia la derecha
        ecuaesq.shift(RIGHT)
        # Se ajusta su tamaño en cierta escala
        ecuaesq.scale(0.65)

        # Se escribe el título
        self.play(Write(titulo))
        # Se espera un tiempo con esta animación
        self.wait()
        self.play(Transform(titulo,ecuacion))
        # Se espera un tiempo con esta animación
        self.wait()
        # Se transforma la euación en la ecuación esquinera
        self.play(Transform(titulo,ecuaesq))

        # Se llama a la función que define los ejes
        self.setup_axes()
        # Se define la gráfica que se desea mostrar y de color verde
        graph = self.get_graph(lambda x : x**2 - x - 1 , color = GREEN)

        # Se muestra la gráfica
        self.play(ShowCreation(graph))
        # Se espera un tiempo con esta animación
        self.wait()

        # Se define el punto y una línea punteada a él
        dot1 = Dot(self.coords_to_point(4.75,16.8125),color=RED)
        vert1 = self.get_vertical_line_to_graph(4.75,graph, color = WHITE)
        punteada1= DashedVMobject(vert1)

        # Se muesta la línea punteada y el punto
        self.play(ShowCreation(punteada1))
        self.add(dot1)

        # Se define el punto y una línea punteada a él
        dot2 = Dot(self.coords_to_point(3.5,7.75),color=RED)
        vert2 = self.get_vertical_line_to_graph(3.5,graph, color = WHITE)
        punteada2= DashedVMobject(vert2)

        # Se muesta la línea punteada
        self.play(ShowCreation(punteada2))
        # Se agrega el punto
        self.add(dot2)
        # Se espera un tiempo con esta animación
        self.wait()

        # Se define la recta que pasa por los puntos
        recta1 = self.get_graph(lambda x : 7.25*x - 17.625 , color = RED)
        # Se define el punto
        dot3 = Dot(self.coords_to_point(2.431034483,0),color=RED)

        # Se muestra la recta y se agrega el punto
        self.play(ShowCreation(recta1))
        self.add(dot3)
        # Se espera un tiempo con esta animación
        self.wait()

        # Se define el punto y una línea punteada a él
        dot4 = Dot(self.coords_to_point(2.431034483,2.4788941),color=RED)
        vert3 = self.get_vertical_line_to_graph(2.431034483,graph, color = WHITE)
        punteada3= DashedVMobject(vert3)
        # Se muesta la línea punteada y se agrega el punto
        self.play(ShowCreation(punteada3))
        self.add(dot4)

        # Se define la recta que pasa por los puntos
        recta2= self.get_graph(lambda x : 4.93103*x - 9.50862 , color = RED)
        # Se define un punto
        dot5= Dot(self.coords_to_point(1.92832,0), color= RED)

        # Se muestra la recta y se agrega el punto
        self.play(ShowCreation(recta2))
        self.add(dot5)

        # Se espera un tiempo con esta animación
        self.wait()

        # Se define el punto y la línea punteada a él
        dot6= Dot(self.coords_to_point(1.92832,0.79), color= RED)
        vert4 = self.get_vertical_line_to_graph(1.92832,graph, color = WHITE)
        punteada4= DashedVMobject(vert4)
        # Se muestra la línea punteada y se agrega el punto
        self.play(ShowCreation(punteada4))
        self.add(dot6)

        # Se espera un tiempo con esta animación
        self.wait()

        # Se ajustan los puntos a cierto tamaño
        dot3.scale(0.5)
        dot4.scale(0.5)
        dot5.scale(0.5)
        dot6.scale(0.5)

        # Se define en que punto se quiere enfocar
        enfoque = Dot(self.coords_to_point(1.92,0.5))
        # Se realiza el enfoque con cierta cantidad de este
        self.play(
            self.camera_frame.scale,.35,
            self.camera_frame.move_to,enfoque
        )

        # Se espera un tiempo con esta animación
        self.wait()

        # Se define la recta que pasa por los puntos
        recta3= self.get_graph(lambda x : 3.35954*x - 5.68828 , color = RED)
        # Se define el punto
        dot7= Dot(self.coords_to_point(1.69317228,0), color= RED)
        # Se ajusta el tamaño del punto
        dot7.scale(0.5)

        # Se muestra la recta
        self.play(ShowCreation(recta3))
        # Se agrega el punto
        self.add(dot7)

        # Se espera un tiempo con esta animación
        self.wait()

        # Se define el punto y la línea punteada a él
        dot8= Dot(self.coords_to_point(1.69317228,0.17366), color= RED)
        vert5 = self.get_vertical_line_to_graph(1.69317228,graph, color = WHITE)
        punteada5= DashedVMobject(vert5)
        # Se muestra la línea punteada
        self.play(ShowCreation(punteada5))
        # Se modifica el tamaño del punto
        dot8.scale(0.5)
        # Se agrega el punto
        self.add(dot8)

        # Se espera un tiempo con esta animación
        self.wait()


    # Función en la que se definen los ejes
    def setup_axes(self):
        # Agregar estos ejes a la gráfica
        GraphScene.setup_axes(self)
        # Parametros para las etiquetas
        #   Para x
        init_label_x = -1
        end_label_x = 5
        step_x = 1
        #   Para y
        init_label_y = -4
        end_label_y = 16
        step_y = 2
        # Posiciones para las etiquetas
        #   Para x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   Para y
        self.y_axis.label_direction = LEFT
        # Agregar etiquetas a la gráfica
        #   Para x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   Para y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #   Se agrega la animación
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )

# Clase para el método del trapecio
class Trapecio(GraphScene):

    # Se realiza la configuración de la gráfica
    CONFIG = {
    # Valor máximo de y en la gráfica
    "y_max" : 10,
    # Valor mínimo de y en la gráfica
    "y_min" : -3,
    # Valor máximo de x en la gráfica
    "x_max" : 8,
    # Valor mínimo de x en la gráfica
    "x_min" : -1,
    # Se define el color de los ejes
    "axes_color" : BLUE,
    # Se define nombre para el eje horizontal
    "x_axis_label" : "$x$",
    # Se define nombre para el eje vertical
    "y_axis_label" : "$f(x)$",
    # Se define la posición en la que quiere que se genere la gráfica
    "graph_origin" : np.array((-5.3,-2,0))
}

    # Bloque de construcción de la animación
    def construct(self):
        # Título correspondiente al método presente
        titulo = TextMobject("Método del trapecio")
        # Ecuación correspondiente al método presente
        ecuacion = TexMobject(
            r"I = (b-a)\frac{f(a)+f(b)}{2}"
        )
        # Misma ecuación que la anterior pero que se posicionará en una esquina
        ecuaesq=TexMobject(
            r"I = (b-a)\frac{f(a)+f(b)}{2}"
        )
        # Se coloca la ecuaión en la esquina derecha superior
        ecuaesq.to_corner(UP+RIGHT)

        # Se escribe el título
        self.play(Write(titulo))
        # Se espera un tiempo con esta animación
        self.wait()
        # Se transforma el título en la ecuación
        self.play(Transform(titulo,ecuacion))
        # Se espera un tiempo con esta animación
        self.wait()
        # Se transforma la euación en la ecuación esquinera
        self.play(Transform(titulo,ecuaesq))

        # Se llama a la función que define los ejes
        self.setup_axes()
        # Se define la gráfica que se desea mostrar y de color verde
        graph = self.get_graph(lambda x : (-0.4)*x**2 + 4*x - 4 , color = GREEN,
            x_min=0.25, x_max=8)

        # Se muestra la gráfica
        self.play(ShowCreation(graph))
        # Se espera un tiempo con esta animación
        self.wait()

        # Se definen ciertos puntos
        dot1 = Dot(self.coords_to_point(2,0))
        dot2 = Dot(self.coords_to_point(7,0))

        # Se agregan los puntos
        self.add(dot1,dot2)

        # Se definen líneas punteadas a los puntos anteriores
        vert1 = self.get_vertical_line_to_graph(2,graph, color = WHITE)
        punteada1= DashedVMobject(vert1)
        vert2 = self.get_vertical_line_to_graph(7,graph, color = WHITE)
        punteada2= DashedVMobject(vert2)

        # Se muestran las líneas punteadas
        self.play(ShowCreation(punteada1), ShowCreation(punteada2))

        # Se definen ciertos puntos
        dot3 = Dot(self.coords_to_point(2,2.4255419))
        dot4 = Dot(self.coords_to_point(7,4.430524))

        # Se agregan los puntos
        self.add(dot3,dot4)

        # Se espera un tiempo con esta animación
        self.wait()

        # Se define una recta en color rojo y se muestra
        recta1= self.get_graph(lambda x : 0.403403215*x + 1.61443462 , color = RED)
        self.play(ShowCreation(recta1))

        # Se espera un tiempo con esta animación
        self.wait()

        # Se define un área
        area = self.get_area(recta1,2,7)
        # Se agrega el área
        self.add(area)

        # Se espera un tiempo con esta animación
        self.wait()

    # Función en la que se definen los ejes
    def setup_axes(self):
        # Agregar estos ejes a la gráfica
        GraphScene.setup_axes(self)
        # Parametros para las etiquetas
        #   Para x
        init_label_x = -1
        end_label_x = 8
        step_x = 1
        #   Para y
        init_label_y = -3
        end_label_y = 10
        step_y = 1
        # Posiciones para las etiquetas
        #   Para x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   Para y
        self.y_axis.label_direction = LEFT
        # Agregar etiquetas a la gráfica
        #   Para x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   Para y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #  Se agrega la animación
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )

# Clase para el método de Simson Tercio
class SimpsonTercio(GraphScene):

    # Se realiza la configuración de la gráfica
    CONFIG = {
    # Valor máximo de y en la gráfica
    "y_max" : 1.5,
    # Valor mínimo de y en la gráfica
    "y_min" : -0.5,
    # Valor máximo de x en la gráfica
    "x_max" : 2.5,
    # Valor mínimo de x en la gráfica
    "x_min" : -2.5,
    # Se define el color de los ejes
    "axes_color" : BLUE,
    # Se define la frecuecia de las líneas en el eje vertical
    "y_tick_frequency" : 0.5,
    # Se define la frecuecia de las líneas en el eje horizontal
    "x_tick_frequency" : 0.5,
    # Se define nombre para el eje horizontal
    "x_axis_label" : "$x$",
    # Se define nombre para el eje vertical
    "y_axis_label" : "$f(x)$",
    # Se define la posición en la que quiere que se genere la gráfica
    "graph_origin" : np.array((-2.4,-2,0))
}

    # Bloque de construcción de la animación
    def construct(self):
        # Título correspondiente al método presente
        titulo = TextMobject("Método de Simpson 1/3")
        # Ecuación correspondiente al método presente
        ecuacion = TexMobject(
            r"I \cong (b-a)\frac{f(x_{0})+4f(x_1)+f(x_2)}{6}"
        )
        # Misma ecuación que la anterior pero que se posicionará en una esquina
        ecuaesq=TexMobject(
            r"I \cong (b-a)\frac{f(x_{0})+4f(x_1)+f(x_2)}{6}"
        )
        # Se coloca la ecuaión en la esquina derecha superior
        ecuaesq.to_corner(UP+RIGHT)

        # Se escribe el título
        self.play(Write(titulo))
        # Se espera un tiempo con esta animación
        self.wait()
        # Se transforma el título en la ecuación
        self.play(Transform(titulo,ecuacion))
        # Se espera un tiempo con esta animación
        self.wait()
        # Se transforma la euación en la ecuación esquinera
        self.play(Transform(titulo,ecuaesq))

        # Se llama a la función que define los ejes
        self.setup_axes()
        # Se define la gráfica que se desea mostrar y de color verde
        graph = self.get_graph(lambda x : np.e**-x**2 , color = GREEN,
            x_min=-2.5, x_max=2.5)
        # Se muestra la gráfica
        self.play(ShowCreation(graph))
        # Se espera un tiempo con esta animación
        self.wait()

        # Se definieron los puntos
        dot1 = Dot(self.coords_to_point(-1,0.3678))
        dot2 = Dot(self.coords_to_point(-0.5,0.7788))
        dot3 = Dot(self.coords_to_point(0,1))
        dot4 = Dot(self.coords_to_point(0.5,0.7788))
        dot5 = Dot(self.coords_to_point(1,0.3678))

        # Se agregaron los puntos
        self.add(dot1,dot2,dot3,dot4,dot5)

        # Se espera un tiempo con esta animación
        self.wait()

        # Se definen líneas punteadas para los puntos
        vert1 = self.get_vertical_line_to_graph(-1,graph, color = WHITE)
        punteada1= DashedVMobject(vert1)
        vert2 = self.get_vertical_line_to_graph(-0.5,graph, color = WHITE)
        punteada2= DashedVMobject(vert2)
        vert3 = self.get_vertical_line_to_graph(0,graph, color = WHITE)
        punteada3= DashedVMobject(vert3)
        vert4 = self.get_vertical_line_to_graph(0.5,graph, color = WHITE)
        punteada4= DashedVMobject(vert4)
        vert5 = self.get_vertical_line_to_graph(1,graph, color = WHITE)
        punteada5= DashedVMobject(vert5)

        # Se muestran las líneas punteadas
        self.play(ShowCreation(punteada1),ShowCreation(punteada2),
        ShowCreation(punteada3),ShowCreation(punteada4),ShowCreation(punteada5))
        # Se espera un tiempo con esta animación
        self.wait()

        # Se define la parábola
        parab1 = self.get_graph(lambda x : -0.3796*x**2 + 0.2526*x + 1 , color = RED,
            x_min=-2.5, x_max=2.5)

        # Se muestra la parábola
        self.play(ShowCreation(parab1))

        # Se define la parábola
        parab2 = self.get_graph(lambda x : -0.8848*x**2 + 1 , color = RED,
            x_min=-2.5, x_max=2.5)

        # Se muestra la parábola
        self.play(ShowCreation(parab2))

        # Se define la parábola
        parab3 = self.get_graph(lambda x : -0.3796*x**2 - 0.2526*x + 1 , color = RED,
            x_min=-2.5, x_max=2.5)

        # Se muestra la parábola
        self.play(ShowCreation(parab3))

    # Función en la que se definen los ejes
    def setup_axes(self):
        # Agregar estos ejes a la gráfica
        GraphScene.setup_axes(self)
        # Parametros para las etiquetas
        #   Para x
        init_label_x = -2
        end_label_x = 2
        step_x = 1
        #   Para y
        init_label_y = 0
        end_label_y = 1
        step_y = 1
        # Posiciones para las etiquetas
        #   Para x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   Para y
        self.y_axis.label_direction = LEFT
        # Agregar etiquetas a la gráfica
        #   Para x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   Para y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #   Se agrega la animación
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )
