from math import ceil, floor, pi, sin
from niveristand import nivs_rt_sequence, NivsParam
from niveristand.clientapi import DoubleValue, I32Value, I64Value
from niveristand.library import deltat, localhost_wait, nivs_yield, rem, seqtime


@NivsParam('ramp_out', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('init_value', DoubleValue(1), NivsParam.BY_VALUE)
@NivsParam('final_value', DoubleValue(10), NivsParam.BY_VALUE)
@NivsParam('duration', DoubleValue(10), NivsParam.BY_VALUE)
@nivs_rt_sequence
def ramp(ramp_out, init_value, final_value, duration):
    """
    Ramps a variable from an initial value to an ending value over the duration you specify.

    Args:
        ramp_out(:any:`DoubleValue`): variable you want to ramp.
        init_value(:any:`DoubleValue`): starting value.
        final_value(:any:`DoubleValue`): ending value.
        duration(:any:`DoubleValue`): time, in seconds, you want the ramp to take.

    """
    step_count = I64Value(0)
    increment = DoubleValue(0)

    step_count.value = ceil(duration.value / deltat())
    if step_count.value <= 0:
        ramp_out.value = final_value.value
    else:
        increment.value = ((final_value.value - init_value.value) / step_count.value)
        for i in range(step_count.value + 1):
            ramp_out.value = (i * increment.value) + init_value.value
            localhost_wait(deltat())
            nivs_yield()


@NivsParam('wave_out', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('amplitude', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('freq', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('phase', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('bias', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('duration', DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def sawtooth_wave(wave_out, amplitude, freq, phase, bias, duration):
    """
    Plays a sawtooth wave with the parameters you specify.

    Args:
        wave_out(:any:`DoubleValue`): variable onto which the sawtooth wave plays.
        amplitude(:any:`DoubleValue`): amplitude of the sawtooth wave.
        freq(:any:`DoubleValue`): frequency, in Hz, of the sawtooth wave.
        phase(:any:`DoubleValue`): phase, in degrees, of the sawtooth wave.
        bias(:any:`DoubleValue`): offset to add to the sawtooth wave.
        duration(:any:`DoubleValue`): duration, in seconds, to play the sawtooth wave.

    """
    init_time = DoubleValue(0)
    curr_phase = DoubleValue(0)
    init_time.value = seqtime()
    while seqtime() - init_time.value < duration.value:
        curr_phase.value = rem((freq.value * 360.0 * (seqtime() - init_time.value)) + phase.value, 360.0)
        if curr_phase.value < 180.0:
            wave_out.value = ((curr_phase.value / 180.0) * amplitude.value) + bias.value
        else:
            wave_out.value = (((curr_phase.value / 180.0) - 2.0) * amplitude.value) + bias.value
        localhost_wait(deltat())
        nivs_yield()


@NivsParam('wave_out', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('amplitude', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('freq', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('phase', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('bias', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('duration', DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def sine_wave(wave_out, amplitude, freq, phase, bias, duration):
    """
    Plays a sine wave with the parameters you specify.

    Args:
        wave_out(:any:`DoubleValue`): variable onto which the sine wave plays.
        amplitude(:any:`DoubleValue`): amplitude of the sine wave.
        freq(:any:`DoubleValue`): frequency, in Hz, of the sine wave.
        phase(:any:`DoubleValue`): phase, in degrees, of the sine wave.
        bias(:any:`DoubleValue`): offset to add to the sine wave.
        duration(:any:`DoubleValue`): duration, in seconds, to play the sine wave.

    """
    init_time = DoubleValue(0)
    phase_rad = DoubleValue(0)

    init_time.value = seqtime()
    phase_rad.value = (phase.value * pi) / 180.0
    while seqtime() - init_time.value < duration.value:
        wave_out.value = amplitude.value * \
            sin(((2 * pi * freq.value) * (seqtime() - init_time.value)) + phase_rad.value) + bias.value
        localhost_wait(deltat())
        nivs_yield()


@NivsParam('wave_out', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('amplitude', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('freq', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('phase', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('bias', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('duty_cycle', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('duration', DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def square_wave(wave_out, amplitude, freq, phase, bias, duty_cycle, duration):
    """
    Plays a square wave with the parameters you specify.

    Args:
        wave_out(:any:`DoubleValue`): variable onto which the square wave plays.
        amplitude(:any:`DoubleValue`): amplitude of the square wave.
        freq(:any:`DoubleValue`): frequency, in Hz, of the square wave.
        phase(:any:`DoubleValue`): phase, in degrees, of the square wave.
        bias(:any:`DoubleValue`): offset to add to the square wave.
        duty_cycle(:any:`DoubleValue`): percentage of time the square wave remains high versus low over one period.
        duration(:any:`DoubleValue`): time, in seconds, to play the square wave.

    """
    init_time = DoubleValue(0)
    curr_phase = DoubleValue(0)

    init_time.value = seqtime()
    while seqtime() - init_time.value < duration.value:
        curr_phase.value = rem(((freq.value * 360.0 * (seqtime() - init_time.value)) + phase.value), 360.0)
        if curr_phase.value < (duty_cycle.value * 3.6):
            wave_out.value = amplitude.value + bias.value
        else:
            wave_out.value = -amplitude.value + bias.value
        localhost_wait(deltat())
        nivs_yield()


@NivsParam('wave_out', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('amplitude', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('freq', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('phase', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('bias', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('duration', DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def triangle_wave(wave_out, amplitude, freq, phase, bias, duration):
    """
    Plays a triangle wave with the parameters you specify.

    Args:
        wave_out(:any:`DoubleValue`): variable onto which the triangle wave plays.
        amplitude(:any:`DoubleValue`): amplitude of the triangle wave.
        freq(:any:`DoubleValue`): frequency, in Hz, of the triangle wave.
        phase(:any:`DoubleValue`): phase, in degrees, of the triangle wave.
        bias(:any:`DoubleValue`): offset to add to the triangle wave.
        duration(:any:`DoubleValue`): duration, in seconds, to play the triangle wave.

    """
    init_time = DoubleValue(0)
    curr_phase = DoubleValue(0)

    init_time.value = seqtime()
    while seqtime() - init_time.value < duration.value:
        curr_phase.value = rem((freq.value * 360.0 * (seqtime() - init_time.value)) + phase.value, 360.0)
        if curr_phase.value < 90.0:
            wave_out.value = ((curr_phase.value / 90.0) * amplitude.value) + bias.value
        elif curr_phase.value < 270.0:
            wave_out.value = ((2.0 - (curr_phase.value / 90.0)) * amplitude.value) + bias.value
        else:
            wave_out.value = (((curr_phase.value / 90.0) - 4.0) * amplitude.value) + bias.value
        localhost_wait(deltat())
        nivs_yield()


@NivsParam('wave_out', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('amplitude', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('duration', DoubleValue(0), NivsParam.BY_REF)
@NivsParam('seed', I32Value(0), NivsParam.BY_VALUE)
@nivs_rt_sequence
def uniform_white_noise_wave(wave_out, amplitude, seed, duration):
    """
    Plays a uniform white noise wave with the parameters you specify.

    Args:
        wave_out(:any:`DoubleValue`): variable onto which the white noise wave plays.
        amplitude(:any:`DoubleValue`): amplitude of the white noise wave.
        seed(:any:`I32Value`): seed for random number generator.
        duration(:any:`DoubleValue`): duration, in seconds, to play the white noise wave.

    """
    x_seed = I32Value(0)
    y_seed = I32Value(0)
    z_seed = I32Value(0)
    init_time = DoubleValue(0)
    seed_sum = DoubleValue(0)

    x_seed.value = seed.value
    y_seed.value = (seed.value * 8191) & 16383
    z_seed.value = (y_seed.value * 8191) & 16383
    init_time.value = seqtime()

    while seqtime() - init_time.value < duration.value:
        x_seed.value = rem(x_seed.value * 171.0, 30269.0)
        y_seed.value = rem(x_seed.value * 172.0, 30307.0)
        z_seed.value = rem(x_seed.value * 170.0, 30323.0)
        seed_sum.value = (x_seed.value / 30269.0) + (y_seed.value / 30307.0) + (z_seed.value / 30323.0)
        wave_out.value = amplitude.value * ((seed_sum - floor(seed_sum.value)) - 0.5) * 2.0
        localhost_wait(deltat())
        nivs_yield()
