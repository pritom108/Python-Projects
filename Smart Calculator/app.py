import streamlit as st
import numpy as np
import pandas as pd
from smart_calc.normal_ops import NormalOps
from smart_calc.complex_ops import ComplexOps
from smart_calc.base_ops import BaseOps
from smart_calc.matrix_ops import MatrixOps


st.set_page_config(page_title='Smart Calculator', layout='wide')


st.title('Smart Calculator — multiple modes')


mode = st.sidebar.radio('Mode', ['Normal', 'Complex', 'Base-N', 'Matrix'])


if mode == 'Normal':
    st.header('Normal calculations')
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Normal')
        a = st.number_input('A', value=0.0, format='%f')
        b = st.number_input('B', value=0.0, format='%f')
        op = st.selectbox('Operation', ['add', 'sub', 'mul', 'div', 'pow'])
        if st.button('Compute'):
            try:
                fn = getattr(NormalOps, op)
                res = fn(a, b)
                st.success(f'Result: {res}')
            except Exception as e:
                st.error(str(e))
    with col2:
        st.subheader('Advanced')
        trig = st.selectbox('Trig', ['none', 'sin', 'cos', 'tan'])
        deg = st.checkbox('Degrees for trig', value=True)
        x = st.number_input('Value for trig/log/sqrt', value=0.0, key='advx')
        if st.button('Advanced compute'):
            try:
                if trig != 'none':
                    st.write('Trig:', NormalOps.trig(trig, x, degrees=deg))
                st.write('Log:', NormalOps.log(x) if x>0 else 'N/A')
                if float(x).is_integer() and x>=0 and x<=20:
                    st.write('Factorial:', NormalOps.factorial(int(x)))
            except Exception as e:
                st.error(e)


elif mode == 'Complex':
    st.header('Complex number calculations')
    sub = st.selectbox('Sub-mode', ['Rectangular (x+jy)', 'Polar (r∠θ)'])
    col1, col2 = st.columns(2)
    with col1:
        if sub.startswith('Rect'):
            x1 = st.number_input('x1 (real)', value=0.0, key='x1')
            y1 = st.number_input('y1 (imag)', value=0.0, key='y1')
            x2 = st.number_input('x2 (real)', value=0.0, key='x2')
            y2 = st.number_input('y2 (imag)', value=0.0, key='y2_')
            z1 = complex(x1, y1)
            z2 = complex(x2, y2)
        else:
            r1 = st.number_input('r1', value=1.0, key='r1')
            th1 = st.number_input('θ1 (deg)', value=0.0, key='th1')
            r2 = st.number_input('r2', value=1.0, key='r2')
            th2 = st.number_input('θ2 (deg)', value=0.0, key='th2')
            x1, y1 = ComplexOps.polar_to_rect(r1, th1)
            x2, y2 = ComplexOps.polar_to_rect(r2, th2)
            z1 = complex(x1, y1)
            z2 = complex(x2, y2)
    with col2:
        op = st.selectbox('Operation', ['add', 'sub', 'mul', 'div'])
        if st.button('Compute complex'):
            try:
                f = getattr(ComplexOps, op)
                z = f(z1, z2)
                r, th = ComplexOps.to_polar(z)
                st.write('Rectangular:', f'{z.real:.6g} + {z.imag:.6g}j')
                st.write('Polar: r={:.6g}, θ={:.6g}°'.format(r, th))
            except Exception as e:
                st.error(e)


elif mode == 'Base-N':
    st.header('Base-N calculations & conversions')

    col1, col2 = st.columns(2)

    # -----------------------------
    # Conversion Section
    # -----------------------------
    with col1:
        st.subheader("Base Conversion")
        base_from = st.selectbox('From base', [2, 8, 10, 16], index=2)
        s = st.text_input('Value (no prefix)', value='15')
        base_to = st.selectbox('To base', [2, 8, 10, 16], index=0)

        if st.button('Convert'):
            try:
                intval = BaseOps.from_base(s, base_from)
                out = BaseOps.to_base(intval, base_to)
                st.success(f'{s} (base {base_from}) → {out} (base {base_to})')
            except Exception as e:
                st.error(str(e))

    # -----------------------------
    # Complement Section
    # -----------------------------
    with col2:
        st.subheader("Complements (binary only)")
        bits = st.text_input('Binary string', value='0110')

        if st.button("Compute complements"):
            try:
                ones = BaseOps.ones_complement(bits)
                twos = BaseOps.twos_complement(bits)
                st.write('1s complement:', ones)
                st.write('2s complement:', twos)
            except Exception as e:
                st.error(str(e))


# ------------------------------------------------------------------------------------
# MATRIX MODE
# ------------------------------------------------------------------------------------
elif mode == 'Matrix':
    st.header('Matrix operations')

    rows = st.number_input('Rows', min_value=1, max_value=10, value=2)
    cols = st.number_input('Cols', min_value=1, max_value=10, value=2)

    txt = st.text_area(
        'Enter elements separated by commas or spaces (row-major order)',
        value='1 2 3 4'
    )

    # Building matrix A
    try:
        flat = [float(x) for x in txt.replace(',', ' ').split()]
        A = MatrixOps.make_matrix(int(rows), int(cols), flat)

        st.write('Matrix A:')
        st.dataframe(pd.DataFrame(A))
    except Exception as e:
        st.error(f'Could not build matrix: {e}')
        A = None

    if A is not None:
        st.subheader("Matrix Operations")

        op = st.selectbox(
            "Select matrix operation",
            ["Transpose", "Determinant", "Inverse", "Multiply with another matrix"]
        )

        # -----------------------------
        # Transpose
        # -----------------------------
        if op == "Transpose":
            if st.button("Compute"):
                result = MatrixOps.transpose(A)
                st.dataframe(pd.DataFrame(result))

        # -----------------------------
        # Determinant
        # -----------------------------
        elif op == "Determinant":
            if st.button("Compute"):
                try:
                    if A.shape[0] != A.shape[1]:
                        st.error("Determinant is only defined for square matrices")
                    else:
                        result = MatrixOps.det(A)
                        st.success(f"Determinant = {result}")
                except Exception as e:
                    st.error(str(e))

        # -----------------------------
        # Inverse
        # -----------------------------
        elif op == "Inverse":
            if st.button("Compute"):
                try:
                    result = MatrixOps.inv(A)
                    st.dataframe(pd.DataFrame(result))
                except Exception as e:
                    st.error(str(e))

        # -----------------------------
        # Matrix Multiplication
        # -----------------------------
        elif op == "Multiply with another matrix":
            st.write("### Enter second matrix")

            rows2 = st.number_input('Rows (B)', min_value=1, max_value=10, value=2, key="r2")
            cols2 = st.number_input('Cols (B)', min_value=1, max_value=10, value=2, key="c2")
            txt2 = st.text_area(
                'Matrix B elements (row-major)',
                value='1 0 0 1',
                key="B_text"
            )

            try:
                flat2 = [float(x) for x in txt2.replace(',', ' ').split()]
                B = MatrixOps.make_matrix(int(rows2), int(cols2), flat2)

                st.write("Matrix B:")
                st.dataframe(pd.DataFrame(B))
            except Exception as e:
                st.error(f'Could not build matrix B: {e}')
                B = None

            if B is not None and st.button("Multiply A × B"):
                try:
                    result = MatrixOps.mul(A, B)
                    st.success("Result of A × B:")
                    st.dataframe(pd.DataFrame(result))
                except Exception as e:
                    st.error(str(e))