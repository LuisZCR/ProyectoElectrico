from manimlib.imports import *

class Biseccion(GraphScene):

    CONFIG = {
    "y_max" : 50,
    "y_min" : 0,
    "x_max" : 7,
    "x_min" : 0,
    "y_tick_frequency" : 5,
    "axes_color" : BLUE,
    "x_axis_label" : "$t$",
    "y_axis_label" : "$f(t)$",
}

    def construct(self):
        titulo = TextMobject("Método de la bisección")
        ecuacion = TexMobject(
            r"\frac{b-a}{2^{n}}"
        )
        ecuaesq=TexMobject(
            r"\frac{b-a}{2^{n}}"
        )
        ecuaesq.to_corner(UP+RIGHT)
        self.play(Write(titulo))
        self.wait()
        self.play(Transform(titulo,ecuacion))
        self.wait()
        self.play(Transform(titulo,ecuaesq))

        self.setup_axes()
        graph = self.get_graph(lambda x : x**2 - 2, color = GREEN)
        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self)
        # Parametters of labels
        #   For x
        init_label_x = 2
        end_label_x = 7
        step_x = 1
        #   For y
        init_label_y = 20
        end_label_y = 50
        step_y = 5
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
    "y_max" : 50,
    "y_min" : -20,
    "x_max" : 7,
    "x_min" : 0,
    "y_tick_frequency" : 5,
    "axes_color" : BLUE,
    "x_axis_label" : "$t$",
    "y_axis_label" : "$f(t)$",
    "graph_origin" : np.array((-4.5,-1.5,0))
}

    def construct(self):
        titulo = TextMobject("Regla Falsa")
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
        graph = self.get_graph(lambda x : x**2 - 20, color = GREEN)
        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self)
        # Parametters of labels
        #   For x
        init_label_x = 1
        end_label_x = 7
        step_x = 1
        #   For y
        init_label_y = -20
        end_label_y = 50
        step_y = 5
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
