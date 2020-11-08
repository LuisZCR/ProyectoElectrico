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

class Reglaf(GraphScene):

    CONFIG = {
    "y_max" : 4,
    "y_min" : -4,
    "x_max" : 1.5,
    "x_min" : -1.5,
    "axes_color" : BLUE,
    "x_axis_label" : "$x$",
    "y_axis_label" : "$f(x)$",
    "graph_origin" : np.array((-2.5,-0.5,0))
}

    def construct(self):
        titulo = TextMobject("Método de la regla falsa")
        ecuacion = TexMobject(
            r"x_{a}= x_{b}-\frac{f(x_{b})(x_{a}-x_{b})}{f(x_a)-f(x_{b})}"
        )
        cond = TexMobject(
            r"f(x_a)\cdot f(x_{b})<0"
        )
        ecuacion.move_to(UP*2)
        ecuaesq=TexMobject(
            r"x_{a}= x_{b}-\frac{f(x_{b})(x_{a}-x_{b})}{f(x_a)-f(x_{b})}"
        )
        ecuaesq.to_corner(UP+RIGHT)

        self.play(Write(titulo))
        self.wait()
        VGroup(titulo, cond).arrange(DOWN*5)
        self.play(Transform(titulo,ecuacion),FadeInFrom(cond, UP),)
        self.wait()
        self.play(Transform(titulo,ecuaesq),LaggedStart(*map(FadeOutAndShiftDown, cond)),)

        self.setup_axes()
        graph = self.get_graph(lambda x : 3*(x**3) + 2*x + 2, color = GREEN)

        puntoa1 = TexMobject("x_{a_{1}}")
        label_coord = self.input_to_graph_point(-1,graph)
        puntoa1.next_to(label_coord,RIGHT+DOWN)
        puntob1 = TexMobject("x_{b_{1}}")
        label_coord2 = self.input_to_graph_point(-0.5,graph)
        puntob1.next_to(label_coord2,RIGHT+UP)
        puntom1 = TexMobject("x_{M_{1}}", color=RED)
        label_coord = self.input_to_graph_point(-0.58621,graph)
        puntom1.next_to(label_coord,RIGHT+DOWN)

        dota1 = Dot(self.coords_to_point(-1,-3))
        dotb1 = Dot(self.coords_to_point(-0.5,0.625))
        dotm1 = Dot(self.coords_to_point(-0.5862068966,0.223256361), color=RED)

        recta1 = self.get_graph(lambda x : 7.25*x + 4.25, color = RED)

        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        self.add(dota1,dotb1)
        self.play(ShowCreation(puntoa1) ,ShowCreation(puntob1))
        self.play(ShowCreation(recta1), run_time=2)
        self.add(dotm1)
        self.play(ShowCreation(puntom1))

        self.wait()

        puntoa2 = TexMobject("x_{a_{2}}")
        label_coord = self.input_to_graph_point(-1,graph)
        puntoa2.next_to(label_coord,RIGHT+DOWN)
        puntob2 = TexMobject("x_{b_{2}}")
        label_coord2 = self.input_to_graph_point(-0.586206966,graph)
        puntob2.next_to(label_coord2,LEFT+UP)
        puntom2 = TexMobject("x_{M_{2}}", color=RED)
        label_coord = self.input_to_graph_point(-0.58621,graph)
        puntom2.next_to(label_coord,RIGHT+UP)

        dota2 = Dot(self.coords_to_point(-1,-3))
        dotb2 = Dot(self.coords_to_point(-0.5862068966,0.2232563861))
        dotm2 = Dot(self.coords_to_point(-0.61488,0.072823), color=RED)

        recta2 = self.get_graph(lambda x : (7.78959)*x + (4.78959) , color = RED)


        self.remove(dota1,dotb1,dotm1)
        self.add(dota2,dotb2)
        self.play(Transform(puntoa1,puntoa2), Transform(puntob1,puntob2))
        self.play(Transform(recta1,recta2))
        self.add(dotm2)
        self.play(Transform(puntom1,puntom2))
        self.wait()

        puntoa3 = TexMobject("x_{a_{3}}")
        label_coord = self.input_to_graph_point(-1,graph)
        puntoa3.next_to(label_coord,RIGHT+DOWN)
        puntob3 = TexMobject("x_{b_{3}}")
        label_coord3 = self.input_to_graph_point(-0.61488,graph)
        puntob3.next_to(label_coord2,LEFT+UP)
        puntom3 = TexMobject("x_{M_{3}}", color=RED)
        label_coord = self.input_to_graph_point(-0.62400,graph)
        puntom3.next_to(label_coord,RIGHT+UP)

        dota3 = Dot(self.coords_to_point(-1,-3))
        dotb3 = Dot(self.coords_to_point(-0.61488,0.072823))
        dotm3 = Dot(self.coords_to_point(-0.62400,0.02307), color=RED)

        recta3 = self.get_graph(lambda x : (7.97887)*x + (4.97887) , color = RED)


        self.remove(dota2,dotb2,dotm2)
        self.add(dota3,dotb3)
        self.play(Transform(puntoa1,puntoa3), Transform(puntob1,puntob3))
        self.play(Transform(recta1,recta3))
        self.add(dotm3)
        self.play(Transform(puntom1,puntom3))

        self.wait()

        puntoa4 = TexMobject("x_{a_{4}}")
        label_coord = self.input_to_graph_point(-1,graph)
        puntoa4.next_to(label_coord,RIGHT+DOWN)
        puntob4 = TexMobject("x_{b_{4}}")
        label_coord2 = self.input_to_graph_point(-0.62400,graph)
        puntob4.next_to(label_coord2,LEFT+UP)
        puntom4 = TexMobject("x_{M_{4}}", color=RED)
        label_coord = self.input_to_graph_point(-0.62687,graph)
        puntom4.next_to(label_coord,RIGHT+UP)

        dota4 = Dot(self.coords_to_point(-1,-3))
        dotb4 = Dot(self.coords_to_point(-0.62400,0.02307))
        dotm4 = Dot(self.coords_to_point(-0.62687,0.00722), color=RED)

        recta4 = self.get_graph(lambda x : (8.04007)*x + (5.04007) , color = RED)

        self.remove(dota3,dotb3,dotm3)
        self.add(dota4,dotb4)
        self.play(Transform(puntoa1,puntoa4), Transform(puntob1,puntob4))
        self.play(Transform(recta1,recta4))
        self.add(dotm4)
        self.play(Transform(puntom1,puntom4))

        self.wait()

        puntoa5 = TexMobject("x_{a_{5}}")
        label_coord = self.input_to_graph_point(-1,graph)
        puntoa5.next_to(label_coord,RIGHT+DOWN)
        puntob5 = TexMobject("x_{b_{5}}")
        label_coord2 = self.input_to_graph_point(-0.62687,graph)
        puntob5.next_to(label_coord2,LEFT+UP)
        puntom5 = TexMobject("x_{M_{5}}", color=RED)
        label_coord = self.input_to_graph_point(-0.62777,graph)
        puntom5.next_to(label_coord,RIGHT+UP)

        dota5 = Dot(self.coords_to_point(-1,-3))
        dotb5 = Dot(self.coords_to_point(-0.62687,0.00722))
        dotm5 = Dot(self.coords_to_point(-0.62777,0.00225), color=RED)

        recta5 = self.get_graph(lambda x : (8.05944)*x + (5.05944) , color = RED)

        self.remove(dota4,dotb4,dotm4)
        self.add(dota5,dotb5)
        self.play(Transform(puntoa1,puntoa5), Transform(puntob1,puntob5))
        self.play(Transform(recta1,recta5))
        self.add(dotm5)
        self.play(Transform(puntom1,puntom5))

        self.wait()

        puntoa6 = TexMobject("x_{a_{6}}")
        label_coord = self.input_to_graph_point(-1,graph)
        puntoa6.next_to(label_coord,RIGHT+DOWN)
        puntob6 = TexMobject("x_{b_{6}}")
        label_coord2 = self.input_to_graph_point(-0.62777,graph)
        puntob6.next_to(label_coord2,LEFT+UP)
        puntom6 = TexMobject("x_{M_{6}}", color=RED)
        label_coord = self.input_to_graph_point(-0.62805,graph)
        puntom6.next_to(label_coord,RIGHT+UP)

        dota6 = Dot(self.coords_to_point(-1,-3))
        dotb6 = Dot(self.coords_to_point(-0.62777,0.00225))
        dotm6 = Dot(self.coords_to_point(-0.62805,0.000703), color=RED)

        recta6 = self.get_graph(lambda x : (8.06557)*x + (5.06557) , color = RED)

        self.remove(dota5,dotb5,dotm5)
        self.add(dota6,dotb6)
        self.play(Transform(puntoa1,puntoa6), Transform(puntob1,puntob6))
        self.play(Transform(recta1,recta6))
        self.add(dotm6)
        self.play(Transform(puntom1,puntom6))

        self.wait()


    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self)
        # Parametters of labels
        #   For x
        init_label_x = -1
        end_label_x = 1
        step_x = 1
        #   For y
        init_label_y = -4
        end_label_y = 4
        step_y = 1
        # Position of labels
        #   For x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   For y
        self.y_axis.label_direction = LEFT
        # Add labels to graph
        #   For x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   For y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #   Add Animation
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )

class NewtonR(GraphScene,MovingCameraScene):

    CONFIG = {
    "y_max" : 16,
    "y_min" : -2,
    "x_max" : 5,
    "x_min" : -1,
    "axes_color" : BLUE,
    "x_axis_label" : "$x$",
    "y_axis_label" : "$f(x)$",
    "graph_origin" : np.array((-4.5,-2.5,0))
}
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        titulo = TextMobject("Método de Newton-Raphson")
        ecuacion = TexMobject(
            r"x_{i+1}= x_{i}-\frac{f(x_{i})}{f'(x_{i})}}"
        )
        ecuaesq=TexMobject(
            r"x_{i+1}= x_{i}-\frac{f(x_{i})}{f'(x_{i})}}"
        )
        ecuaesq.to_corner(UP+RIGHT)

        self.play(Write(titulo))
        self.wait()
        self.play(Transform(titulo,ecuacion))
        self.wait()
        self.play(Transform(titulo,ecuaesq))

        self.setup_axes()
        graph = self.get_graph(lambda x : x**2 - 1 , color = GREEN)

        self.play(ShowCreation(graph))
        self.wait()

        dot1 = Dot(self.coords_to_point(4,0))
        vert1 = self.get_vertical_line_to_graph(4,graph, color = WHITE)
        punteada1= DashedVMobject(vert1)

        self.add(dot1)
        self.play(ShowCreation(punteada1))

        recta1 = self.get_graph(lambda x : 8*x -17 , color = RED)
        self.play(ShowCreation(recta1))

        dot2 = Dot(self.coords_to_point(2.125,0))
        self.add(dot2)
        self.wait()

        vert2 = self.get_vertical_line_to_graph(2.125,graph, color = WHITE)
        punteada2= DashedVMobject(vert2)

        self.play(ShowCreation(punteada2))

        recta2 = self.get_graph(lambda x : 4.25*x -5.515625 , color = RED)
        self.play(ShowCreation(recta2))

        enfoque = Dot(self.coords_to_point(0.85,0.5))
        self.play(
            self.camera_frame.scale,.35,
            self.camera_frame.move_to,enfoque
        )

        dot3 = Dot(self.coords_to_point(1.297794118,0))
        dot3.scale(0.45)
        self.add(dot3)
        self.wait()

        vert3 = self.get_vertical_line_to_graph(1.297794118,graph, color = WHITE)
        punteada3 = DashedVMobject(vert3)

        self.play(ShowCreation(punteada3))

        recta3 = self.get_graph(lambda x : 2.595588*x -2.684269266 , color = RED)
        self.play(ShowCreation(recta3))


        enfoque2 = Dot(self.coords_to_point(1.034166157,0))
        self.play(
            self.camera_frame.scale,.1,
            self.camera_frame.move_to,enfoque2
        )

        dot4 = Dot(self.coords_to_point(1.034166157,0))
        dot4.scale(0.1)
        self.add(dot4)
        self.wait()

        vert4 = self.get_vertical_line_to_graph(1.034166157,graph , color = WHITE)
        punteada4 = DashedVMobject(vert4)

        self.play(ShowCreation(punteada4))

        linea1 = self.get_graph(lambda x : 0.06989 , color = YELLOW)
        linea2 = self.get_graph(lambda x : -0.06989 , color = YELLOW)

        self.play(ShowCreation(linea1),ShowCreation(linea2))

        area1 = self.get_area(linea1,0,2)
        area2 = self.get_area(linea2,0,2)

        self.play(ShowCreation(area1),ShowCreation(area2))

        self.wait()

    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self)
        # Parametters of labels
        #   For x
        init_label_x = -1
        end_label_x = 5
        step_x = 1
        #   For y
        init_label_y = 2
        end_label_y = 16
        step_y = 2
        # Position of labels
        #   For x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   For y
        self.y_axis.label_direction = LEFT
        # Add labels to graph
        #   For x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   For y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #   Add Animation
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )

class Secante(GraphScene,MovingCameraScene):

    CONFIG = {
    "y_max" : 16,
    "y_min" : -4,
    "x_max" : 5,
    "x_min" : -2,
    "axes_color" : BLUE,
    "y_tick_frequency" : 2,
    "x_axis_label" : "$x$",
    "y_axis_label" : "$f(x)$",
    "graph_origin" : np.array((-4.25,-2.25,0))
}

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        titulo = TextMobject("Método de la secante")
        ecuacion = TexMobject(
            r"x_{i+1}= x_{i}-\frac{(x_{i}-x_{i-1})f(x_{i})}{f(x_{i})-f(x_{i-1})}}"
        )
        ecuaesq=TexMobject(
            r"x_{i+1}= x_{i}-\frac{(x_{i}-x_{i-1})f(x_{i})}{f(x_{i})-f(x_{i-1})}}"
        )
        ecuaesq.to_corner(UP+RIGHT)
        ecuaesq.shift(RIGHT)
        ecuaesq.scale(0.65)

        self.play(Write(titulo))
        self.wait()
        self.play(Transform(titulo,ecuacion))
        self.wait()
        self.play(Transform(titulo,ecuaesq))

        self.setup_axes()
        graph = self.get_graph(lambda x : x**2 - x - 1 , color = GREEN)

        self.play(ShowCreation(graph))
        self.wait()

        dot1 = Dot(self.coords_to_point(4.75,16.8125),color=RED)
        vert1 = self.get_vertical_line_to_graph(4.75,graph, color = WHITE)
        punteada1= DashedVMobject(vert1)

        self.play(ShowCreation(punteada1))
        self.add(dot1)

        dot2 = Dot(self.coords_to_point(3.5,7.75),color=RED)
        vert2 = self.get_vertical_line_to_graph(3.5,graph, color = WHITE)
        punteada2= DashedVMobject(vert2)

        self.play(ShowCreation(punteada2))
        self.add(dot2)
        self.wait()

        recta1 = self.get_graph(lambda x : 7.25*x - 17.625 , color = RED)
        dot3 = Dot(self.coords_to_point(2.431034483,0),color=RED)

        self.play(ShowCreation(recta1))
        self.add(dot3)
        self.wait()

        dot4 = Dot(self.coords_to_point(2.431034483,2.4788941),color=RED)
        vert3 = self.get_vertical_line_to_graph(2.431034483,graph, color = WHITE)
        punteada3= DashedVMobject(vert3)
        self.play(ShowCreation(punteada3))
        self.add(dot4)

        recta2= self.get_graph(lambda x : 4.93103*x - 9.50862 , color = RED)
        dot5= Dot(self.coords_to_point(1.92832,0), color= RED)

        self.play(ShowCreation(recta2))
        self.add(dot5)

        self.wait()

        dot6= Dot(self.coords_to_point(1.92832,0.79), color= RED)
        vert4 = self.get_vertical_line_to_graph(1.92832,graph, color = WHITE)
        punteada4= DashedVMobject(vert4)
        self.play(ShowCreation(punteada4))
        self.add(dot6)

        self.wait()

        dot3.scale(0.5)
        dot4.scale(0.5)
        dot5.scale(0.5)
        dot6.scale(0.5)

        enfoque = Dot(self.coords_to_point(1.92,0.5))
        self.play(
            self.camera_frame.scale,.35,
            self.camera_frame.move_to,enfoque
        )

        self.wait()

        recta3= self.get_graph(lambda x : 3.35954*x - 5.68828 , color = RED)
        dot7= Dot(self.coords_to_point(1.69317228,0), color= RED)
        dot7.scale(0.5)

        self.play(ShowCreation(recta3))
        self.add(dot7)

        self.wait()

        dot8= Dot(self.coords_to_point(1.69317228,0.17366), color= RED)
        vert5 = self.get_vertical_line_to_graph(1.69317228,graph, color = WHITE)
        punteada5= DashedVMobject(vert5)
        self.play(ShowCreation(punteada5))
        dot8.scale(0.5)
        self.add(dot8)

        self.wait()



    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self)
        # Parametters of labels
        #   For x
        init_label_x = -1
        end_label_x = 5
        step_x = 1
        #   For y
        init_label_y = -4
        end_label_y = 16
        step_y = 2
        # Position of labels
        #   For x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   For y
        self.y_axis.label_direction = LEFT
        # Add labels to graph
        #   For x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   For y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #   Add Animation
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )

class Trapecio(GraphScene):

    CONFIG = {
    "y_max" : 10,
    "y_min" : -3,
    "x_max" : 8,
    "x_min" : -1,
    "axes_color" : BLUE,
    "x_axis_label" : "$x$",
    "y_axis_label" : "$f(x)$",
    "graph_origin" : np.array((-5.3,-2,0))
}

    def construct(self):
        titulo = TextMobject("Método del trapecio")
        ecuacion = TexMobject(
            r"I = (b-a)\frac{f(a)+f(b)}{2}"
        )
        ecuaesq=TexMobject(
            r"I = (b-a)\frac{f(a)+f(b)}{2}"
        )
        ecuaesq.to_corner(UP+RIGHT)

        self.play(Write(titulo))
        self.wait()
        self.play(Transform(titulo,ecuacion))
        self.wait()
        self.play(Transform(titulo,ecuaesq))

        self.setup_axes()
        graph = self.get_graph(lambda x : (-0.4)*x**2 + 4*x - 4 , color = GREEN,
            x_min=0.25, x_max=8)

        self.play(ShowCreation(graph))
        self.wait()

        dot1 = Dot(self.coords_to_point(2,0))
        dot2 = Dot(self.coords_to_point(7,0))

        self.add(dot1,dot2)

        vert1 = self.get_vertical_line_to_graph(2,graph, color = WHITE)
        punteada1= DashedVMobject(vert1)
        vert2 = self.get_vertical_line_to_graph(7,graph, color = WHITE)
        punteada2= DashedVMobject(vert2)

        self.play(ShowCreation(punteada1), ShowCreation(punteada2))

        dot3 = Dot(self.coords_to_point(2,2.4255419))
        dot4 = Dot(self.coords_to_point(7,4.430524))

        self.add(dot3,dot4)

        self.wait()

        recta1= self.get_graph(lambda x : 0.403403215*x + 1.61443462 , color = RED)
        self.play(ShowCreation(recta1))

        self.wait()

        area = self.get_area(recta1,2,7)

        self.add(area)

        self.wait()

    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self)
        # Parametters of labels
        #   For x
        init_label_x = -1
        end_label_x = 8
        step_x = 1
        #   For y
        init_label_y = -3
        end_label_y = 10
        step_y = 1
        # Position of labels
        #   For x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   For y
        self.y_axis.label_direction = LEFT
        # Add labels to graph
        #   For x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   For y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #   Add Animation
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )

class SimpsonTercio(GraphScene):

    CONFIG = {
    "y_max" : 1.5,
    "y_min" : -0.5,
    "x_max" : 2.5,
    "x_min" : -2.5,
    "axes_color" : BLUE,
    "y_tick_frequency" : 0.5,
    "x_tick_frequency" : 0.5,
    "x_axis_label" : "$x$",
    "y_axis_label" : "$f(x)$",
    "graph_origin" : np.array((-2.4,-2,0))
}

    def construct(self):
        titulo = TextMobject("Método de Simpson 1/3")
        ecuacion = TexMobject(
            r"I \cong (b-a)\frac{f(x_{0})+4f(x_1)+f(x_2)}{6}"
        )
        ecuaesq=TexMobject(
            r"I \cong (b-a)\frac{f(x_{0})+4f(x_1)+f(x_2)}{6}"
        )
        ecuaesq.to_corner(UP+RIGHT)

        self.play(Write(titulo))
        self.wait()
        self.play(Transform(titulo,ecuacion))
        self.wait()
        self.play(Transform(titulo,ecuaesq))

        self.setup_axes()
        graph = self.get_graph(lambda x : np.e**-x**2 , color = GREEN,
            x_min=-2.5, x_max=2.5)

        self.play(ShowCreation(graph))
        self.wait()

        dot1 = Dot(self.coords_to_point(-1,0.3678))
        dot2 = Dot(self.coords_to_point(-0.5,0.7788))
        dot3 = Dot(self.coords_to_point(0,1))
        dot4 = Dot(self.coords_to_point(0.5,0.7788))
        dot5 = Dot(self.coords_to_point(1,0.3678))

        self.add(dot1,dot2,dot3,dot4,dot5)

        self.wait()

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

        self.play(ShowCreation(punteada1),ShowCreation(punteada2),
        ShowCreation(punteada3),ShowCreation(punteada4),ShowCreation(punteada5))
        self.wait()

        parab1 = self.get_graph(lambda x : -0.3796*x**2 + 0.2526*x + 1 , color = RED,
            x_min=-2.5, x_max=2.5)

        self.play(ShowCreation(parab1))

        parab2 = self.get_graph(lambda x : -0.8848*x**2 + 1 , color = RED,
            x_min=-2.5, x_max=2.5)

        self.play(ShowCreation(parab2))

        parab3 = self.get_graph(lambda x : -0.3796*x**2 - 0.2526*x + 1 , color = RED,
            x_min=-2.5, x_max=2.5)

        self.play(ShowCreation(parab3))

    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self)
        # Parametters of labels
        #   For x
        init_label_x = -2
        end_label_x = 2
        step_x = 1
        #   For y
        init_label_y = 0
        end_label_y = 1
        step_y = 1
        # Position of labels
        #   For x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   For y
        self.y_axis.label_direction = LEFT
        # Add labels to graph
        #   For x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   For y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #   Add Animation
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )
