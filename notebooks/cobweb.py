import ipywidgets
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize


EPSILON = 0.01
a_float_slider = ipywidgets.FloatSlider(value=3.0,
                                        min=0.0,
                                        max=10.0,
                                        step=EPSILON,
                                        description=r"$a$")

b_float_slider = ipywidgets.FloatSlider(value=0.25,
                                        min=0.0,
                                        max=1.0,
                                        step=EPSILON,
                                        description=r"$b$")

w_float_slider = ipywidgets.FloatSlider(value=0.3,
                                        min=0.0,
                                        max=1.0,
                                        step=EPSILON,
                                        description=r"$w$")

gamma_float_slider = ipywidgets.FloatSlider(value=3.6,
                                            min=0.0,
                                            max=10.0,
                                            step=EPSILON,
                                            description=r"$\gamma$")

p_bar_float_slider = ipywidgets.FloatSlider(value=5.0,
                                            min=0.0,
                                            max=10.0,
                                            step=EPSILON,
                                            description=r"$\bar{p}$")

initial_expected_price_slider = ipywidgets.FloatSlider(value=5.0,
                                                       min=0.0,
                                                       max=10.0,
                                                       step=EPSILON,
                                                       description=r"$p_0^e$")

T_int_slider = ipywidgets.IntSlider(value=50,
                                    min=1,
                                    max=500,
                                    step=EPSILON,
                                    description=r"$T$")


def _excess_demand(price, D, S, a, b, gamma, p_bar):
    """Excess demand function."""
    return D(price, a, b) - S(price, gamma, p_bar)


def _forecast_error(D_inverse, S, expected_price, **params):
    """Difference between observed price and expected price."""
    return observed_price(D_inverse, S, expected_price, **params) - expected_price


def _simulate(X0, F, T, **params):
    """Simulate a map F for T periods starting from X0."""
    X = np.empty(T + 1)
    X[0] = X0
    for t in range(T):
        X[t+1] = F(X[t], **params)
    return X



def quantity_demand_plot(D, a, b):
    """Plot quantity of goods demanded as a function of the observed price."""
    prices = np.linspace(0, 10, 1000)
    plt.plot(prices, D(prices, a, b), label=r"$D(p_t)$")
    plt.xlabel("Prices", fontsize=15)
    plt.ylabel("Quantities", fontsize=15)
    plt.ylim(0, 1.05 * a)
    plt.title("Goods demand function", fontsize=25)
    plt.legend()


def quantity_supply_plot(S, gamma, p_bar):
    """Plot quantity of goods supplied as a function of the expected price."""
    expected_prices = np.linspace(0, 2 * p_bar, 1000)
    plt.plot(expected_prices, S(expected_prices, gamma, p_bar),
             label=r"$S(p_t^e)$")
    plt.xlabel("Prices", fontsize=15)
    plt.ylabel("Quantities", fontsize=15)
    plt.xlim(0, 2 * p_bar)
    plt.ylim(0, 3.5)
    plt.title("Goods supply function", fontsize=25)
    plt.legend()


def supply_demand_plot(D, S, a, b, gamma, p_bar):
    """Plot demand and supply curves to find the market clearing equilibrium."""
    equilibrium_price = optimize.bisect(_excess_demand, 0, 100 * p_bar,
                                        args=(D, S, a, b, gamma, p_bar))

    prices = np.linspace(0, 2 * equilibrium_price, 1000)
    plt.plot(prices, S(prices, gamma, p_bar), label=r"$S_{\gamma}(p_t^e)$")
    plt.plot(prices, D(prices, a, b), label=r"$D(p_t)$")
    plt.plot(equilibrium_price, D(equilibrium_price, a, b), linestyle='none',
             marker='o', color='k', label=r"$p^*={}$".format(equilibrium_price))
    plt.xlabel("Prices", fontsize=15)
    plt.ylabel("Quantities", fontsize=15)
    plt.xlim(0, prices[-1])
    plt.ylim(0, 1.05 * a)
    plt.title("Market clearing equilibrium", fontsize=25)
    plt.legend()


def time_series_plot(F, X0, T, **params):
    """Plot time series of some map F."""
    delta = 1e-6
    traj1 = _simulate(X0, F, T, **params)
    traj2 = _simulate((1 + delta) * X0, F, T, **params)

    fig, ax = plt.subplots(1, 2, sharex=True)
    ax[0].plot(traj1)
    ax[0].set_xlabel('Time', fontsize=15)
    ax[0].set_ylabel('$p_t^e$', fontsize=15, rotation='horizontal')

    ax[1].plot(np.abs(traj1 - traj2))
    ax[0].set_xlabel('Time', fontsize=15)
    ax[1].set_yscale('log')
    ax[1].set_title("Dependence on initial conditions?", fontsize=15)
    fig.tight_layout()


def forecast_error_plot(D_inverse, S, F, X0, T, **params):
    """Plot forecast errors."""
    trajectory = _simulate(X0, F, T, **params)
    errors = _forecast_error(D_inverse, S, trajectory , **params)

    fig, ax = plt.subplots(1, 2)
    ax[0].plot(errors)
    ax[0].set_xlabel('Time')

    ax[1].hist(errors, bins=20)
    fig.suptitle('Forecast errors', fontsize=25)
    ax[1].set_xlabel('Errors')
    fig.tight_layout()
