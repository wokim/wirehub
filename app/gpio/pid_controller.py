class PIDController:
    def __init__(self, kp, ki, kd, setpoint):
        """
        Initialize PID controller.

        Parameters:
        - kp (float): Proportional gain (P control gain)
        - ki (float): Integral gain (I control gain)
        - kd (float): Derivative gain (D control gain)
        - setpoint (float): Target temperature
        """
        self.kp = kp  # P gain
        self.ki = ki  # I gain
        self.kd = kd  # D gain
        self.setpoint = setpoint  # Target temperature
        self.prev_error = 0.0  # Initialize previous error
        self.integral = 0.0  # Initialize integral term

    def calculate_output(self, current_temperature):
        """
        Calculate output using PID control.

        Parameters:
        - current_temperature (float): Current temperature

        Returns:
        - float: Calculated output value
        """
        # Calculate current error
        error = self.setpoint - current_temperature

        # Proportional control term
        proportional = self.kp * error

        # Integral control term
        self.integral += error
        integral = self.ki * self.integral

        # Derivative control term
        derivative = self.kd * (error - self.prev_error)
        self.prev_error = error

        # Calculate total control output
        output = proportional + integral + derivative

        # Return the output value (can be converted to PWM duty cycle, etc.)
        return output
