import pyomo.environ as pyo


def model():
    model = pyo.AbstractModel()

    # Constant

    model.n = pyo.Param(
        doc="Total of Pickup-Delivery pair points",
        mutable=False,
        within=pyo.NonNegativeIntegers
    )

    # Sets 
    def init_set_pickup(model, offset=0):
        for i in range(model.n):
            yield i+1+offset

    def init_set_delivery(model):
        yield init_set_pickup(model, offset=model.n)

    model.P = pyo.Set(
        dimen=1, 
        doc="Pickup Set",
        initialize=init_set_pickup,
        ordered=True, 
        within=pyo.NonNegativeIntegers
    )
    model.D = pyo.Set(
        dimen=1, 
        doc="Delivery Set",
        initialize=init_set_delivery,
        ordered=True, 
        within=pyo.NonNegativeIntegers
    )

    model.V = model.P | model.D # Union of pickup and delivery

    # Parameters 

    model.c = pyo.Param(model.V, model.V, within=pyo.PositiveReals)

    # Variables

    model.x = pyo.Var(model.V, model.V, domain=pyo.Binary)

    # Objective Rule

    def obj_rule(model):
        return pyo.summation(model.c, model.x) # TODO: funciona ou nao pra variaveis de duas dimensoes?

    model.OBJ = pyo.Objective(rule=obj_rule)

    # definir constraints
    
    def ax_constraint_rule(m, i):
        # return the expression for the constraint for i
        return sum(m.a[i,j] * m.x[j] for j in m.J) >= m.b[i]

    # the next line creates one constraint for each member of the set model.I
    model.AxbConstraint = pyo.Constraint(model.I, rule=ax_constraint_rule)