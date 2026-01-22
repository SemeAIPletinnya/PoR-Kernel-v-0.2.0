def silence_control(values, threshold=0.01):
    return [v if abs(v) > threshold else 0.0 for v in values]
