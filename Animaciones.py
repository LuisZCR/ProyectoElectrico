from manimlib.imports import *


class Biseccion(GraphScene):

    CONFIG = {
    "y_max" : 6,
    "y_min" : -6,
    "x_max" : 6,
    "x_min" : -6,
    "axes_color" : BLUE,
    "x_axis_label" : "$x$",
    "y_axis_label" : "$f(x)$",
    "graph_origin" : np.array((0,0,0))
}

    def construct(self):
        titulo = TextMobject("Método de la bisección")
        ecuacion = TexMobject(
            r"\frac{b+a}{2}"
        )
        ecuaesq = TexMobject(
            r"\frac{b+a}{2}"
        )
        ecuaesq.to_corner(UP+RIGHT)
        self.play(Write(titulo))
        self.wait()
        self.play(Transform(titulo,ecuacion))
        self.wait()
        self.play(Transform(titulo,ecuaesq))

        self.setup_axes()
        graph = self.get_graph(lambda x : np.cos(x) - x, color = GREEN)
        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        self.wait()


        puntoa1 = TexMobject("x_{a_{1}}")
        label_coord = self.input_to_graph_point(-3,graph)
        puntoa1.next_to(label_coord,RIGHT+DOWN)
        puntob1 = TexMobject("x_{b_{1}}")
        label_coord2 = self.input_to_graph_point(3,graph)
        puntob1.next_to(label_coord2,RIGHT+UP)

        dota1 = Dot(self.coords_to_point(-3,2.01))
        dotb1 = Dot(self.coords_to_point(3,-3.989992))

        self.add(dota1,dotb1)
        self.play(ShowCreation(puntoa1) ,ShowCreation(puntob1))

        res1 = TexMobject(
            r"\frac{3+(-3)}{2}=0"
        )
        res1.to_corner(UP+RIGHT)
        self.play(Transform(titulo,res1))

        self.wait()

        puntoa2 = TexMobject("x_{a_{2}}")
        label_coord = self.input_to_graph_point(0,graph)
        puntoa2.next_to(label_coord,RIGHT+UP)
        puntob2 = TexMobject("x_{b_{2}}")
        label_coord2 = self.input_to_graph_point(3,graph)
        puntob2.next_to(label_coord2,RIGHT+UP)

        dota2 = Dot(self.coords_to_point(0,1))
        dotb2 = Dot(self.coords_to_point(3,-3.989992))

        self.remove(dota1,dotb1)
        self.add(dota2,dotb2)
        self.play(Transform(puntoa1,puntoa2), Transform(puntob1,puntob2))

        res2 = TexMobject(
            r"\frac{3+0}{2}=1.5"
        )
        res2.to_corner(UP+RIGHT)
        self.play(Transform(titulo,res2))

        self.wait()

        puntoa3 = TexMobject("x_{a_{3}}")
        label_coord = self.input_to_graph_point(0,graph)
        puntoa3.next_to(label_coord,RIGHT+UP)
        puntob3 = TexMobject("x_{b_{3}}")
        label_coord2 = self.input_to_graph_point(1.5,graph)
        puntob3.next_to(label_coord2,RIGHT+DOWN)

        dota3 = Dot(self.coords_to_point(0,1))
        dotb3 = Dot(self.coords_to_point(1.5,-1.429262))

        self.remove(dota2,dotb2)
        self.add(dota3,dotb3)
        self.play(Transform(puntoa1,puntoa3), Transform(puntob1,puntob3))

        res3 = TexMobject(
            r"\frac{1.5+0}{2}=0.75"
        )
        res3.to_corner(UP+RIGHT)
        self.play(Transform(titulo,res3))

        self.wait()

        puntoa4 = TexMobject("x_{a_{4}}")
        label_coord = self.input_to_graph_point(0,graph)
        puntoa4.next_to(label_coord,RIGHT+UP)
        puntob4 = TexMobject("x_{b_{4}}")
        label_coord2 = self.input_to_graph_point(0.75,graph)
        puntob4.next_to(label_coord2,RIGHT+UP)

        dota4 = Dot(self.coords_to_point(0,1))
        dotb4 = Dot(self.coords_to_point(0.75,-0.0183111))

        self.remove(dota3,dotb3)
        self.add(dota4,dotb4)
        self.play(Transform(puntoa1,puntoa4), Transform(puntob1,puntob4))

        res4 = TexMobject(
            r"\frac{0.75+0}{2}=0.375"
        )
        res4.to_corner(UP+RIGHT)
        self.play(Transform(titulo,res4))

        self.wait()

        puntoa5 = TexMobject("x_{a_{5}}")
        label_coord = self.input_to_graph_point(0.375,graph)
        puntoa5.next_to(label_coord,RIGHT+UP)
        puntob5 = TexMobject("x_{b_{5}}")
        label_coord2 = self.input_to_graph_point(0.75,graph)
        puntob5.next_to(label_coord2,RIGHT+UP)

        dota5 = Dot(self.coords_to_point(0.375,0.5555076))
        dotb5 = Dot(self.coords_to_point(0.75,-0.0183111))

        self.remove(dota4,dotb4)
        self.add(dota5,dotb5)
        self.play(Transform(puntoa1,puntoa5), Transform(puntob1,puntob5))

        res5 = TexMobject(
            r"\frac{0.375+0.75}{2}=0.5625"
        )
        res5.to_corner(UP+RIGHT)
        self.play(Transform(titulo,res5))

        self.wait(3)

        puntoan = TexMobject("x_{a_{n}}")
        label_coord = self.input_to_graph_point(0.739,graph)
        puntoan.next_to(label_coord,RIGHT+UP)
        puntoan.scale(0.75)
        puntobn = TexMobject("x_{b_{n}}")
        label_coord2 = self.input_to_graph_point(0.739,graph)
        puntobn.next_to(label_coord2,RIGHT+DOWN)
        puntobn.scale(0.75)

        dotan = Dot(self.coords_to_point(0.739,0.000142477), color=YELLOW)


        self.remove(dota5,dotb5)
        self.add(dotan)
        self.play(Transform(puntoa1,puntoan), Transform(puntob1,puntobn))

        res5 = TexMobject(
            r"\frac{0.739+0.739}{2}=0.739 ; n=19"
        )
        res5.scale(0.75)
        res5.to_corner(UP+RIGHT)
        self.play(Transform(titulo,res5))

        self.wait()

    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self)
        # Parametters of labels
        #   For x
        init_label_x = -6
        end_label_x = 6
        step_x = 1
        #   For y
        init_label_y = 6
        end_label_y = -6
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

class NewtonR(GraphScene):

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

        vert1 = self.get_vertical_line_to_graph(4,graph, color = WHITE)
        dota1 = Dot(self.coords_to_point(4,0))
        punteada1= DashedVMobject(vert1)

        self.add(dota1)
        self.play(ShowCreation(punteada1))

        self.wait()

        recta1 = self.get_graph(lambda x : 8*x -17 , color = RED)
        self.play(ShowCreation(recta1))
        self.wait()

        dotb1 = Dot(self.coords_to_point(2.125,0))
        self.add(dotb1)
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
