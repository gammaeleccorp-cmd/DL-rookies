import numpy as np
import matplotlib.pyplot as plt


class Update_Parameter:

    # Gradient Descent

    @staticmethod
    def gradient_descent(loss, gradient, x, y, lr=0.05, iterations=100):
        
        x_list, y_list = [x], [y]
        losses = [loss(x, y)]
        grads = []

        for _ in range(iterations):

            grad_x, grad_y = gradient(x, y)
            x = x - lr * grad_x
            y = y - lr * grad_y

            x_list.append(x)
            y_list.append(y)
            losses.append(loss(x, y))
            grads.append((grad_x, grad_y))

        return x_list, y_list, losses, grads


    # Momentum

    @staticmethod
    def momentum(loss, gradient, x, y, lr=0.05, m_beta=0.9, iterations=100):

        x_list, y_list = [x], [y]
        losses = [loss(x, y)]
        grads = []

        v_x, v_y = 0, 0

        for _ in range(iterations):

            grad_x, grad_y = gradient(x, y)

            v_x = m_beta * v_x + grad_x
            v_y = m_beta * v_y + grad_y

            x = x - lr * v_x
            y = y - lr * v_y

            x_list.append(x)
            y_list.append(y)
            losses.append(loss(x, y))
            grads.append((grad_x, grad_y))

        return x_list, y_list, losses, grads


    # AdaGrad

    @staticmethod
    def adagrad(loss, gradient, x, y, lr=0.05, eps=1e-8, iterations=100):

        x_list, y_list = [x], [y]
        losses = [loss(x, y)]
        grads = []
        effective_lr = [(lr, lr)]

        v_x, v_y = 0, 0

        for _ in range(iterations):

            grad_x, grad_y = gradient(x, y)

            v_x = v_x + grad_x**2
            v_y = v_y + grad_y**2

            lr_x = lr / np.sqrt(v_x + eps)
            lr_y = lr / np.sqrt(v_y + eps)

            x = x - lr_x * grad_x
            y = y - lr_y * grad_y

            x_list.append(x)
            y_list.append(y)
            losses.append(loss(x, y))
            grads.append((grad_x, grad_y))
            effective_lr.append((lr_x, lr_y))

        return x_list, y_list, losses, grads, effective_lr


    # RMSProp

    @staticmethod
    def rmsprop(loss, gradient, x, y, lr=0.05, r_beta=0.9, eps=1e-8, iterations=100):

        x_list, y_list = [x], [y]
        losses = [loss(x, y)]
        grads = []
        effective_lr = [(lr,lr)]

        v_x, v_y = 0, 0

        for _ in range(iterations):

            grad_x, grad_y = gradient(x, y)

            v_x = r_beta*v_x + (1-r_beta)*(grad_x**2)
            v_y = r_beta*v_y + (1-r_beta)*(grad_y**2)

            lr_x = lr / np.sqrt(v_x + eps)
            lr_y = lr / np.sqrt(v_y + eps)
 
            x = x - lr_x * grad_x
            y = y - lr_y * grad_y

            x_list.append(x)
            y_list.append(y)
            losses.append(loss(x, y))
            grads.append((grad_x, grad_y))
            effective_lr.append((lr_x, lr_y))

        return x_list, y_list, losses, grads, effective_lr


    # Adam

    @staticmethod
    def adam(loss, gradient, x, y, lr=0.05, beta1=0.9, beta2=0.999, eps=1e-8, iterations=100):

        x_list, y_list = [x], [y]
        losses = [loss(x, y)]
        grads = []
        effective_lr = [(lr, lr)]

        m_x, m_y = 0, 0
        v_x, v_y = 0, 0

        for t in range(1, iterations+1):

            grad_x, grad_y = gradient(x, y)

            m_x = beta1*m_x + (1-beta1)*(grad_x)
            m_y = beta1*m_y + (1-beta1)*(grad_y)

            m_hat_x = m_x / (1-beta1**t)
            m_hat_y = m_y / (1-beta1**t)

            v_x = beta2*v_x + (1-beta2)*(grad_x**2)
            v_y = beta2*v_y + (1-beta2)*(grad_y**2)

            v_hat_x = v_x / (1-beta2**t)
            v_hat_y = v_y / (1-beta2**t)

            lr_x = lr / (np.sqrt(v_hat_x) + eps)
            lr_y = lr / (np.sqrt(v_hat_y) + eps)

            x = x - lr_x * m_hat_x
            y = y - lr_y * m_hat_y

            x_list.append(x)
            y_list.append(y)
            losses.append(loss(x, y))
            grads.append((grad_x, grad_y))
            effective_lr.append((lr_x, lr_y))

        return x_list, y_list, losses, grads, effective_lr


    # AdamW

    @staticmethod
    def adamw(loss, gradient, x, y, lr=0.05, beta1=0.9, beta2=0.999, weight_decay=0.01, eps=1e-8, iterations=100):

        x_list, y_list = [x], [y]
        losses = [loss(x, y)]
        grads = []
        effective_lr = [(lr, lr)]
        
        m_x, m_y = 0, 0
        v_x, v_y = 0, 0
        λ = weight_decay

        for t in range(1, iterations+1):

            grad_x, grad_y = gradient(x, y)

            m_x = beta1*m_x + (1-beta1)*(grad_x)
            m_y = beta1*m_y + (1-beta1)*(grad_y)

            m_hat_x = m_x / (1-beta1**t)
            m_hat_y = m_y / (1-beta1**t)

            v_x = beta2*v_x + (1-beta2)*(grad_x**2)
            v_y = beta2*v_y + (1-beta2)*(grad_y**2)

            v_hat_x = v_x / (1-beta2**t)
            v_hat_y = v_y / (1-beta2**t)

            lr_x = lr / (np.sqrt(v_hat_x) + eps)
            lr_y = lr / (np.sqrt(v_hat_y) + eps)

            x = (1-lr*λ)*x - lr_x * m_hat_x
            y = (1-lr*λ)*y - lr_y * m_hat_y

            x_list.append(x)
            y_list.append(y)
            losses.append(loss(x, y))
            grads.append((grad_x, grad_y))
            effective_lr.append((lr_x, lr_y))

        return x_list, y_list, losses, grads, effective_lr


    # Final result

    @staticmethod
    def result(gradient_descent, momentum, adagrad, rmsprop, adam, adamw):

        print('     Algorithm     |   Final x   |   Final y   |   Final Loss   ')
        print('---------------------------------------------------------------')
        print(f'  Gradient Descent | {gradient_descent[0][-1]:>8.4f}    | {gradient_descent[1][-1]:>8.4f}    | {gradient_descent[2][-1]:>10.2f} ')
        print(f'      Momentum     | {momentum[0][-1]:>8.4f}    | {momentum[1][-1]:>8.4f}    | {momentum[2][-1]:>10.2f} ')
        print(f'      AdaGrad      | {adagrad[0][-1]:>8.4f}    | {adagrad[1][-1]:>8.4f}    | {adagrad[2][-1]:>10.2f} ')
        print(f'      RMSprop      | {rmsprop[0][-1]:>8.4f}    | {rmsprop[1][-1]:>8.4f}    | {rmsprop[2][-1]:>10.2f} ')
        print(f'       Adam        | {adam[0][-1]:>8.4f}    | {adam[1][-1]:>8.4f}    | {adam[2][-1]:>10.2f} ')
        print(f'       AdamW       | {adamw[0][-1]:>8.4f}    | {adamw[1][-1]:>8.4f}    | {adamw[2][-1]:>10.2f} ')



class Plot:

    labels = [
        "Gradient Descent",
        "Momentum",
        "AdaGrad",
        "RMSProp",
        "Adam",
        "AdamW"
    ]

    @staticmethod
    def loss_vs_iter(
        losses,
        title="Loss vs Iteration"
    ):

        fig, ax = plt.subplots(figsize=(12, 8))

        for label, loss in zip(Plot.labels, losses):
            ax.plot(
                range(len(loss)),
                loss,
                label=label
            )

        ax.set_xlabel("Iteration")
        ax.set_ylabel("Loss")
        ax.set_title(title)
        ax.legend()
        ax.grid(True)
        fig.tight_layout()

        plt.show()


    @staticmethod
    def contour_plot(
        loss,
        X_list,
        Y_list,
        title="Optimizer Paths",
        levels=20
    ):

        all_x = np.concatenate([np.asarray(x) for x in X_list])
        all_y = np.concatenate([np.asarray(y) for y in Y_list])

        valid = np.isfinite(all_x) & np.isfinite(all_y)

        all_x = all_x[valid]
        all_y = all_y[valid]

        x_min, x_max = all_x.min(), all_x.max()
        y_min, y_max = all_y.min(), all_y.max()

        x_range = x_max - x_min
        y_range = y_max - y_min

        x_padding = 0.1 * (x_range if x_range > 0 else 1)
        y_padding = 0.1 * (y_range if y_range > 0 else 1)

        x = np.linspace(
            x_min - x_padding,
            x_max + x_padding,
            400
        )

        y = np.linspace(
            y_min - y_padding,
            y_max + y_padding,
            400
        )

        X, Y = np.meshgrid(x, y)

        Z = loss(X, Y)

        fig, ax = plt.subplots(figsize=(12, 8))

        ax.contour(
            X,
            Y,
            Z,
            levels=levels,
            cmap="viridis"
        )

        for label, x_values, y_values in zip(
            Plot.labels,
            X_list,
            Y_list
        ):
            ax.plot(
                x_values,
                y_values,
                marker="o",
                markersize=3,
                label=label
            )

        ax.scatter(
            X_list[0][0],
            Y_list[0][0],
            marker="*",
            s=150,
            color="black",
            label="Start"
        )

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title(title)
        ax.legend()
        fig.tight_layout()

        plt.show()


    @staticmethod
    def gd_vs_adam(
        gradient_descent,
        adam,
        title="Gradient Descent vs Adam"
    ):

        fig, ax = plt.subplots(figsize=(12, 8))

        ax.plot(
            gradient_descent[0],
            gradient_descent[1],
            marker="o",
            markersize=3,
            label="Gradient Descent"
        )

        ax.plot(
            adam[0],
            adam[1],
            marker="o",
            markersize=3,
            label="Adam"
        )

        ax.scatter(
            gradient_descent[0][0],
            gradient_descent[1][0],
            marker="*",
            s=150,
            color="black",
            label="Start"
        )

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title(title)
        ax.legend()
        fig.tight_layout()

        plt.show()

        print(
            f"Gradient Descent:\n"
            f"Final (x, y) = "
            f"({gradient_descent[0][-1]:.3f}, "
            f"{gradient_descent[1][-1]:.3f})\n"
            f"Final loss = {gradient_descent[2][-1]:.3f}"
        )

        print(
            f"\nAdam:\n"
            f"Final (x, y) = "
            f"({adam[0][-1]:.3f}, "
            f"{adam[1][-1]:.3f})\n"
            f"Final loss = {adam[2][-1]:.3f}"
        )