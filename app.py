# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 11:18:22 2026

@author: ag261
"""

from special_relativity.lorentz import gamma, lorentz_transform, inverse_lorentz
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import time
import plotly.graph_objects as go

import streamlit as st

st.set_page_config(page_title="Relativity Simulator", layout="wide")

#st.title("🕒 Relativity Simulator")

mode = st.sidebar.selectbox(
    "Choose Section",
    ["Home", "Special Relativity", "General Relativity"]
)



# -------------------------------HOME PAGE---------------------------------


if mode == "Home":

    st.markdown("""
    <style>
    .hero {
        background-color: #f2f2f2;
        padding: 50px;
        border-radius: 15px;
    }
    .big-title {
        font-size: 60px;
        font-weight: 800;
    }
    .sub-title {
        font-size: 28px;
        color: #777;
    }
    .hero-text {
        font-size: 18px;
        color: #444;
    }
    .button {
        background-color: black;
        color: white;
        padding: 12px 25px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <style>
    .navbar {
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 40px;
        font-weight: 600;
    }
    
    .nav-right {
        font-size: 14px;
        color: #555;
    }
    </style>
    
    <div class="navbar">
        <div><b>Relativity Simulator</b></div>
        <div class="nav-right">Created by <b>AYUSH GUPTA</b></div>
    </div>
    """, unsafe_allow_html=True)



    
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown("""
        <div class="hero">
            <div class="big-title">Relativity</div>
            <div class="big-title">Simulator</div>
            <br>
            <b>Exploring Space, Time, and Gravity</b><br><br>
            <div class="hero-text">
            Visualize and understand Special & General Relativity through
            interactive simulations, mathematics, and physical intuition.
            </div>
            <br><br>
            
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image(
            "https://miro.medium.com/v2/resize:fit:1400/1*1TKBTRYpnGBQbhrE-XIj9Q.jpeg",
            use_container_width=True
        )
        
        
        
    st.divider()

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        ### 01  
        **Special Relativity (STR)**  
    
        - Lorentz Transformations  
        - Time Dilation  
        - Length Contraction  
        - Relativity of Simultaneity  
        - Velocity Addition  
        - Minkowski Spacetime (2D)  
        - Minkowski Spacetime (3D)  
        - Spacetime Paths & Causality  
        - Twin Paradox  
        """)
    
    with col4:
        st.markdown("""
        ### 02  
        **General Relativity (GR)**  
    
        - Gravitational Time Dilation  
        - Black Hole & Event Horizon  
        - Light Bending (Gravitational Lensing)  
        - Orbits & Geodesics  
        - Gravitational Redshift  
        - Gravitational Waves  
        - Cosmology (Expanding Universe)  
        - 3D Universe Expansion  
        - Bubble Universe Model  
        """)

    

    st.divider()

    st.subheader("About This Simulator")

    st.markdown("""
    The **Relativity Simulator** is an interactive learning platform designed to make the
    concepts of **Special Relativity** and **General Relativity** more intuitive, visual,
    and accessible.
    
    Relativity is often taught through equations alone, which can make its deep physical
    ideas difficult to grasp. This simulator bridges that gap by combining:
    
    - Mathematical expressions  
    - Visual demonstrations  
    - Interactive controls  
    - Conceptual explanations  
    
    to help users *see* and *understand* how spacetime works.
    """)
    
    st.markdown("""
    ### Why This Simulator Was Created
    
    Many students encounter relativity as a collection of formulas to memorize.
    However, the true power of Einstein’s theories lies in their **physical interpretation**:
    
    - Time is not absolute  
    - Space and time are connected  
    - Gravity is the curvature of spacetime  
    - Motion depends on the observer  
    
    This platform was created to move beyond rote learning and build **physical intuition**
    through visualization and interaction.
    """)
    
    st.markdown("""
    ### What Makes This Simulator Different
    
    Unlike traditional textbooks or static notes, this simulator allows users to:
    
    - Adjust physical parameters  
    - Observe relativistic effects in real time  
    - Visualize spacetime geometry  
    - Explore multiple reference frames  
    - Understand causality and motion  
    
    Every topic is presented with both **conceptual clarity** and **mathematical accuracy**.
    """)
    
    st.markdown("""
    ### Who This Is For
    
    This simulator is designed for:
    
    - Undergraduate physics students  
    - Enthusiasts of modern physics  
    - Learners curious about spacetime  
    - Anyone who wants a deeper understanding of relativity  
    
    No advanced background is required — the explanations are structured to guide users
    from basic ideas to more advanced concepts.
    """)
    
    st.markdown("""
    ### Educational Philosophy
    
    Relativity is not just a theory of motion —  
    it is a new way of understanding reality itself.
    
    This simulator aims to:
    
    - Encourage curiosity  
    - Strengthen intuition  
    - Connect theory with visualization  
    - Make abstract ideas tangible  
    
    The ultimate goal is to help learners *experience* spacetime, not just calculate it.
    """)


    
    col_left, col_right = st.columns([1.5, 1])

    with col_left:
        st.subheader("A Brief History of Relativity")
    
        st.markdown("""
        At the end of the 19th century, classical physics could not explain several
        experimental results, particularly those involving the nature of light.
        
        Experiments such as the **Michelson–Morley experiment** showed that the speed of light
        is the same for all observers, contradicting Newtonian ideas of absolute space and time.
        """)
    
        st.markdown("""
        ### Special Relativity (1905)
        
        In **1905**, Albert Einstein introduced the theory of **Special Relativity**.
        
        He proposed two fundamental principles:
        
        - The laws of physics are the same in all inertial frames  
        - The speed of light is constant for all observers  
        
        From these ideas emerged revolutionary conclusions:
        
        - Time is not absolute  
        - Length depends on motion  
        - Simultaneity is relative  
        - Mass and energy are equivalent (E = mc²)  
        """)
    
        st.markdown("""
        ### General Relativity (1915)
        
        In **1915**, Einstein extended his ideas to gravity with **General Relativity**.
        
        Instead of treating gravity as a force, he showed that:
        
        - Mass and energy curve spacetime  
        - Objects follow geodesics in this curved geometry  
        - Gravity is the geometry of spacetime itself  
        
        This theory successfully explained:
        
        - The precession of Mercury’s orbit  
        - Gravitational time dilation  
        - The bending of light by gravity  
        """)
    
    with col_right:
        st.image(
            "https://static.independent.co.uk/s3fs-public/thumbnails/image/2015/09/11/01/3143975.jpg",
            caption="Albert Einstein (1879–1955)",
            use_container_width=True
        )

    
    st.markdown("""
    ### Modern Developments
    
    Over the past century, relativity has been confirmed by many experiments, including:
    
    - Gravitational lensing  
    - GPS time corrections  
    - Black hole imaging  
    - Gravitational wave detection  
    
    Relativity is now a cornerstone of modern physics, shaping our understanding of
    the universe, from black holes to cosmology.
    """)
    
    st.markdown("""
    ### Why Relativity Matters
    
    Relativity transformed our understanding of reality by showing that:
    
    - Space and time are connected  
    - Motion depends on the observer  
    - Gravity is a geometric effect  
    - The universe is dynamic and evolving  
    
    It remains one of the most profound achievements in the history of science.
    """)
    
    st.subheader("About the Creator")

    st.markdown("""
    **Ayush Gupta**  
    Physics Undergraduate | Aspiring Theoretician  
    
    Ayush Gupta is a physics undergraduate with a strong interest in the
    foundations of modern theoretical physics, particularly in the areas of
    **Relativity, Quantum Mechanics, and Cosmology**.
    
    He is the author of *“Principles of Quantum Mechanics for Beginners”*,  
    a book aimed at making quantum theory more accessible to students and
    enthusiasts through clear explanations and intuitive reasoning.
    
    Alongside independent research and writing, he has also contributed to
    academic work through the publication of research papers, reflecting his
    growing involvement in theoretical and conceptual physics.
    
    Beyond science, he maintains a **spiritual and philosophical outlook** toward
    nature and reality, viewing physics not only as a technical discipline, but
    also as a deeper exploration of the universe and human understanding.
    

    This simulator is part of his broader effort to make advanced physics
    more **intuitive, visual, and conceptually meaningful** for learners.
    """)
    
    st.markdown("""
    ### Connect with the Creator
    
    🌐 **Website:**  
    <a href="https://sites.google.com/view/ayushgupta-physics" target="_blank">
    ayushgupta-physics
    </a>
    
    💼 **LinkedIn:**  
    <a href="https://www.linkedin.com/in/ayush-gupta-32b412263" target="_blank">
    linkedin.com/in/AYUSH GUPTA
    </a>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### Support This Project ☕
    
    If you found this simulator helpful, you can support its development:
    
    ☕ Buy Me a Coffee  
    https://buymeacoffee.com/guptadynamics  
    """)


    st.caption("© 2026 Gupta Dynamics | Relativity Simulator")





# -------------------------------Special Relativity---------------------------------
if mode == "Special Relativity":
    sr_topic = st.sidebar.selectbox(
        "Choose Topic",
        [
            "Lorentz Transformations",
            "Time Dilation",
            "Length Contraction",
            "Relativity of Simultaneity",
            "Velocity Addition",
            "Minkowski Spacetime (2D)",
            "Minkowski Spacetime (3D)",
            "Spacetime Paths & Causality",
            "Twin Paradox"
        ]
    )

    st.header(sr_topic)


    if sr_topic == "Lorentz Transformations":
    
        st.subheader("Lorentz Transformation Equations")
    
        st.latex(r"t' = \gamma \left(t - \frac{vx}{c^2}\right)")
        st.latex(r"x' = \gamma (x - vt)")
        st.latex(r"\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}")
    
        st.subheader("Inverse Lorentz Transformations")
    
        st.latex(r"t = \gamma \left(t' + \frac{vx'}{c^2}\right)")
        st.latex(r"x = \gamma (x' + vt')")
    
        st.markdown("""
        **Physical Meaning:**
        - Space and time depend on the observer's motion  
        - Moving observers measure different coordinates  
        - The speed of light is the same for all observers  
        """)
    
        st.divider()
    
        # ---------- Forward Calculator ----------
        st.subheader("Lorentz Transformation Calculator")
    
        v = st.slider("Velocity (v/c)", 0.0, 0.99, 0.5)
    
        g = gamma(v)
        st.info(f"Gamma (γ) = {g:.4f}")
    
        t = st.number_input("Enter time t", value=1.0)
        x = st.number_input("Enter position x", value=1.0)
    
        t_p, x_p = lorentz_transform(t, x, v)
    
        st.success("Transformed Coordinates:")
        st.write(f"t' = {t_p:.4f}")
        st.write(f"x' = {x_p:.4f}")
    
        st.divider()
    
        # ---------- Inverse Calculator ----------
        st.subheader("Inverse Lorentz Transformation Calculator")
    
        t_p2 = st.number_input("Enter t'", value=t_p)
        x_p2 = st.number_input("Enter x'", value=x_p)
    
        t_back, x_back = inverse_lorentz(t_p2, x_p2, v)
    
        st.success("Transformed Coordinates:")
        st.write(f"t = {t_back:.4f}")
        st.write(f"x = {x_back:.4f}")
    
    
    if sr_topic == "Time Dilation":
    
        st.subheader("Time Dilation in Special Relativity")
    
        st.latex(r"\Delta t = \gamma \Delta \tau")
        st.latex(r"\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}")
    
        st.markdown("""
        **Physical Meaning:**
        - A moving clock runs slower  
        - Time depends on the observer's motion  
        - This has been verified experimentally  
        """)
    
        st.divider()
    
        # --------- Controls ----------
        v = st.slider("Velocity (v/c)", 0.0, 0.99, 0.6)
        proper_time = st.number_input("Proper Time Δτ (seconds)", value=10.0)
    
        g = gamma(v)
        dilated_time = g * proper_time
    
        st.info(f"Gamma (γ) = {g:.4f}")
        st.success(f"Dilated Time (Δt) = {dilated_time:.4f} seconds")
        st.caption("Note: Time is shown in arbitrary units (e.g., seconds). The key effect is the relativistic scaling by γ.")
    
    
        st.divider()
    
        # --------- Clock Comparison Plot ----------
        st.subheader("Clock Comparison")
    
        t = np.linspace(0, proper_time, 100)
        moving_clock = t
        stationary_clock = g * t
    
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.plot(t, stationary_clock, label="Stationary Observer Time Δt")
        ax.plot(t, moving_clock, label="Moving Clock Proper Time Δτ")
        ax.set_xlabel("Proper Time (Moving Clock)")
        ax.set_ylabel("Time Measured")
        ax.legend()
    
        st.pyplot(fig)
        
    
    
        st.subheader("Clock Comparison")
        
        v = st.slider("Velocity (v/c)", 0.0, 0.99, 0.6, key="td_anim_v")
        proper_time = st.number_input("Proper Time Δτ (seconds)", value=10.0, key="td_anim_time")
        
        g = gamma(v)
        
        #st.info(f"Gamma (γ) = {g:.3f}")
        
        col1, col2 = st.columns(2)
        stationary_placeholder = col1.empty()
        moving_placeholder = col2.empty()
        
        st.caption("Left: Stationary Observer | Right: Moving Clock")
        
        # Animation parameters
        dt = 0.2   # time step per frame
        steps = int(proper_time / dt)
        
        for i in range(steps + 1):
            moving_t = i * dt
            stationary_t = g * moving_t
        
            stationary_placeholder.metric(
                label="Stationary Clock Time",
                value=f"{stationary_t:.2f} s"
            )
        
            moving_placeholder.metric(
                label="Moving Clock Time",
                value=f"{moving_t:.2f} s"
            )
        
            time.sleep(0.1)
    
    
    if sr_topic == "Length Contraction":
    
        st.subheader("Length Contraction in Special Relativity")
    
        st.latex(r"L = \frac{L_0}{\gamma}")
        st.latex(r"\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}")
    
        st.markdown("""
        **Physical Meaning:**
        - A moving object appears shorter along the direction of motion  
        - Only the length parallel to motion contracts  
        - This is a relativistic effect observed at high speeds  
        """)
    
        st.divider()
    
        # -------- Controls --------
        v = st.slider("Velocity (v/c)", 0.0, 0.99, 0.6, key="lc_v")
        L0 = st.number_input("Proper Length L₀ (meters)", value=10.0, key="lc_L0")
    
        g = gamma(v)
        L = L0 / g
    
        st.info(f"Gamma (γ) = {g:.4f}")
        st.success(f"Contracted Length L = {L:.4f} meters")
    
        st.divider()
    
        # -------- Static Visualization --------
        st.subheader("Length Comparison")
    
        fig, ax = plt.subplots(figsize=(6, 2))
    
        ax.barh(["Rest Frame (L₀)"], [L0], color="blue")
        ax.barh(["Moving Frame (L)"], [L], color="red")
    
        ax.set_xlim(0, L0 * 1.2)
        ax.set_xlabel("Length (meters)")
        ax.set_title("Proper vs Contracted Length")
    
        st.pyplot(fig)
    
        st.divider()
    
        # -------- Animation: Rod Contraction --------
        st.subheader("Animated Length Contraction")
    
        st.caption("The rod contracts along the direction of motion as speed increases.")
    
        rod_placeholder = st.empty()
    
        steps = 30
        dt = 0.1
    
        for i in range(steps + 1):
            factor = i / steps
            current_L = L0 - factor * (L0 - L)
    
            fig2, ax2 = plt.subplots(figsize=(6, 2))
    
            ax2.barh(["Rod at Rest"], [L0], color="blue")
            ax2.barh(["Moving Rod"], [current_L], color="red")
    
            ax2.set_xlim(0, L0 * 1.2)
            ax2.set_xlabel("Length (meters)")
            ax2.set_title("Relativistic Length Contraction")
    
            rod_placeholder.pyplot(fig2)
    
            time.sleep(dt)
    
    
    if sr_topic == "Relativity of Simultaneity":
    
        st.subheader("Relativity of Simultaneity in Special Relativity")
    
        st.latex(r"\Delta t' = \gamma \left(\Delta t - \frac{v \Delta x}{c^2}\right)")
    
        st.markdown("""
        **Physical Meaning:**
        - Two events that are simultaneous in one frame  
          may not be simultaneous in another  
        - This happens because space and time mix  
        - Simultaneity depends on the observer's motion  
        """)
    
        st.divider()
    
        # -------- Controls --------
        v = st.slider("Velocity (v/c)", 0.0, 0.99, 0.5, key="sim_v")
        delta_x = st.number_input("Spatial Separation Δx (meters)", value=10.0, key="sim_dx")
    
        g = gamma(v)
    
        # In frame S: Δt = 0
        delta_t_prime = -g * v * delta_x
    
        st.info(f"Gamma (γ) = {g:.4f}")
        st.success(f"Time difference in moving frame Δt' = {delta_t_prime:.4f} seconds")
    
        st.caption("Events that are simultaneous in one frame are not simultaneous in another.")
    
        st.divider()
    
        # -------- Visualization --------
        st.subheader("Spacetime Visualization")
    
        # Two events simultaneous in S
        t = [0, 0]
        x = [0, delta_x]
    
        # Transform to S'
        t_p = [-g * v * delta_x, 0]
        x_p = [0, g * delta_x]
    
        fig, ax = plt.subplots(figsize=(4, 3))
    
        ax.scatter(x, t, color="blue", label="Frame S (Simultaneous)")
        ax.scatter(x_p, t_p, color="red", label="Frame S' (Not Simultaneous)")
    
        ax.axhline(0, linestyle="--", color="gray")
    
        ax.set_xlabel("Position")
        ax.set_ylabel("Time")
        ax.legend()
    
        st.pyplot(fig)
    
    
        st.subheader("Relativity of Simultaneity: Two Reference Frames")
    
        colA, colB = st.columns(2)
    
    
        with colA:
            st.markdown("### Ground Frame (Train is Moving)")
            st.markdown("Lightning strikes are **simultaneous** in this frame.")
        
            play_ground = st.button("▶ Play Ground Frame", key="play_ground")
        
            placeholderA = st.empty()
        
            if play_ground:
                train_length = 10
                ground_length = 20
                frames = 40
                train_pos_start = -8
                train_pos_end = 8
        
                for i in range(frames):
        
                    train_x = train_pos_start + (train_pos_end - train_pos_start) * i / frames
        
                    fig, ax = plt.subplots(figsize=(5, 2))
        
                    ax.plot([-ground_length, ground_length], [0, 0], color="black")
                    ax.plot([train_x, train_x + train_length], [0.2, 0.2], linewidth=6, color="blue")
        
                    if i == frames // 2:
                        ax.scatter(train_x, 0.2, color="yellow", s=100)
                        ax.scatter(train_x + train_length, 0.2, color="yellow", s=100)
        
                    observer_x = train_x + train_length / 2
                    ax.scatter(observer_x, 0.2, color="red", s=80)
        
                    ax.set_xlim(-ground_length, ground_length)
                    ax.set_ylim(-1, 1)
                    ax.axis("off")
        
                    placeholderA.pyplot(fig)
                    time.sleep(0.1)
    
    
    
    
        with colB:
            st.markdown("### Train Frame (Train is at Rest)")
            st.markdown("Lightning strikes are **NOT simultaneous** in this frame.")
        
            play_train = st.button("▶ Play Train Frame", key="play_train")
        
            placeholderB = st.empty()
        
            if play_train:
                train_length = 10
                ground_length = 20
                frames = 40
        
                front_flash = frames // 3
                back_flash = 2 * frames // 3
        
                for i in range(frames):
        
                    fig, ax = plt.subplots(figsize=(5, 2))
        
                    ax.plot([-ground_length, ground_length], [0, 0], color="black")
                    ax.plot([0, train_length], [0.2, 0.2], linewidth=6, color="blue")
        
                    if i == front_flash:
                        ax.scatter(train_length, 0.2, color="yellow", s=100)
                        ax.text(train_length, 0.4, "Front", color="yellow")
        
                    if i == back_flash:
                        ax.scatter(0, 0.2, color="yellow", s=100)
                        ax.text(0, 0.4, "Back", color="yellow")
        
                    observer_x = train_length / 2
                    ax.scatter(observer_x, 0.2, color="red", s=80)
        
                    ax.set_xlim(-ground_length, ground_length)
                    ax.set_ylim(-1, 1)
                    ax.axis("off")
        
                    placeholderB.pyplot(fig)
                    time.sleep(0.1)
    
        st.markdown("""
        ### Key Takeaway
        
        The **same physical events** can have **different time orderings**
        in different reference frames.
        
        There is **no absolute simultaneity** in Special Relativity.
        """)
        
    if sr_topic == "Velocity Addition":
    
        st.subheader("Relativistic Velocity Addition")
    
        st.latex(r"u' = \frac{u + v}{1 + \frac{uv}{c^2}}")
    
        st.markdown("""
        **Physical Meaning:**
        - Velocities do NOT add normally at high speeds  
        - The speed of light is the same for all observers  
        - No object can exceed the speed of light  
        """)
    
        st.divider()
    
        # -------- Controls --------
        u = st.slider("Object Speed u (as fraction of c)", -0.99, 0.99, 0.5, key="vel_u")
        v = st.slider("Frame Speed v (as fraction of c)", -0.99, 0.99, 0.5, key="vel_v")
    
        # Classical result
        u_classical = u + v
    
        # Relativistic result
        u_rel = (u + v) / (1 + u * v)
    
        st.success(f"Relativistic Velocity u' = {u_rel:.4f} c")
        st.info(f"Classical Velocity (u + v) = {u_classical:.4f} c")
    
        st.caption("Notice how the relativistic result never exceeds the speed of light.")
    
        st.divider()
    
        # -------- Visualization --------
        st.subheader("Classical vs Relativistic Comparison")
    
        labels = ["Classical", "Relativistic"]
        values = [abs(u_classical), abs(u_rel)]
    
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.bar(labels, values)
        ax.set_ylim(0, 1.1)
        ax.set_ylabel("Speed (fraction of c)")
        ax.set_title("Velocity Addition Comparison")
    
        st.pyplot(fig)
    
        st.subheader("Animated Velocity Addition")
        
        st.markdown("""
        A spaceship moves inside a moving train.  
        Even when both move very fast, the total speed never exceeds the speed of light.
        """)
        
        u = st.slider("Spaceship Speed inside Train (u/c)", 0.0, 0.99, 0.7, key="anim_u")
        v = st.slider("Train Speed relative to Ground (v/c)", 0.0, 0.99, 0.7, key="anim_v")
        
        u_rel = (u + v) / (1 + u * v)
        
        st.info(f"Relativistic Combined Speed = {u_rel:.4f} c")
        
        play_anim = st.button("▶ Play Velocity Animation")
        
        placeholder = st.empty()
        
        ground_length = 30
        train_length = 10
        frames = 40
        
        if play_anim:
        
            for i in range(frames):
        
                fig, ax = plt.subplots(figsize=(6, 2))
        
                # Ground line
                ax.plot([-ground_length, ground_length], [0, 0], color="black")
        
                # Train motion
                train_x = -10 + (20 * i / frames)
                ax.plot([train_x, train_x + train_length], [0.2, 0.2],
                        linewidth=6, color="blue", label="Train")
        
                # Spaceship inside train
                ship_x = train_x + (train_length * u * i / frames)
                ax.scatter(ship_x, 0.2, color="red", s=80, label="Spaceship")
        
                ax.set_xlim(-ground_length, ground_length)
                ax.set_ylim(-1, 1)
                ax.axis("off")
        
                ax.legend(loc="upper right")
        
                placeholder.pyplot(fig)
        
                time.sleep(0.1)
    
        
    if sr_topic == "Minkowski Spacetime (2D)":
    
        st.subheader("Visualizing Space and Time in 2D")
    
        st.markdown("""
        This diagram shows how **space and time mix** in Special Relativity.
    
        - Vertical axis: time (ct)  
        - Horizontal axis: space (x)  
        - Light rays: 45° lines  
        - Observers: worldlines  
        """)
    
        st.divider()
    
        # -------- Controls --------
        v = st.slider("Observer Velocity (v/c)", -0.9, 0.9, 0.5, key="mink_v")
    
        g = gamma(v)
    
        st.info(f"Gamma (γ) = {g:.3f}")
    
        # -------- Spacetime Grid --------
        t = np.linspace(-10, 10, 200)
        x = np.linspace(-10, 10, 200)
    
        # Light rays
        light1 = t
        light2 = -t
    
        # Worldlines
        x_stationary = np.zeros_like(t)
        x_moving = v * t
    
        # -------- Plot --------
        fig, ax = plt.subplots(figsize=(6, 6))
    
        # Axes
        ax.axhline(0, color="black")
        ax.axvline(0, color="black")
    
        # Light cones
        ax.plot(light1, t, linestyle="--", color="orange", label="Light Ray")
        ax.plot(light2, t, linestyle="--", color="orange")
    
        # Worldlines
        ax.plot(x_stationary, t, color="blue", label="Stationary Observer")
        ax.plot(x_moving, t, color="red", label="Moving Observer")
    
        # Simultaneity lines
        t0 = 4
        x_sim = np.linspace(-10, 10, 200)
        t_sim = t0 * np.ones_like(x_sim)
    
        t_prime_sim = g * (t0 - v * x_sim)
        ax.plot(x_sim, t_sim, color="blue", linestyle=":")
        ax.plot(x_sim, t_prime_sim, color="red", linestyle=":")
    
        # Labels
        ax.set_xlabel("Space (x)")
        ax.set_ylabel("Time (ct)")
        ax.set_title("Minkowski Spacetime (2D)")
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.legend()
        ax.grid(True)
    
        st.pyplot(fig)
    
        st.markdown("""
        ### How to read this diagram
    
        - **Blue vertical line** → observer at rest  
        - **Red tilted line** → moving observer  
        - **Orange lines** → light rays (speed of light)  
        - **Dotted lines** → simultaneity slices  
    
        Notice how simultaneity is **different** for each observer.
        """)
    
    if sr_topic == "Minkowski Spacetime (3D)":
    
        st.subheader("Visualizing Space and Time in 3D")
    
        st.markdown("""
        This 3D diagram shows spacetime with:
        - Two space dimensions (x, y)
        - One time dimension (ct)
    
        The light cone separates **causal** and **non-causal** regions.
        """)
    
        v = st.slider("Observer Velocity (v/c)", 0.0, 0.9, 0.5, key="mink3d_v")
        g = gamma(v)
    
        st.info(f"Gamma (γ) = {g:.3f}")
    
        # -------- Grid for Light Cones (Future + Past) --------
        t = np.linspace(0, 8, 50)
        theta = np.linspace(0, 2*np.pi, 50)
        T, Theta = np.meshgrid(t, theta)
        
        X = T * np.cos(Theta)
        Y = T * np.sin(Theta)
        
        Z_future = T          # Future light cone (ct > 0)
        Z_past = -T           # Past light cone (ct < 0)
    
    
        # -------- Future Light Cone --------
        future_cone = go.Surface(
            x=X, y=Y, z=Z_future,
            colorscale="Viridis",
            opacity=0.4,
            showscale=False,
            name="Future Light Cone"
        )
        
        # -------- Past Light Cone --------
        past_cone = go.Surface(
            x=X, y=Y, z=Z_past,
            colorscale="Plasma",
            opacity=0.4,
            showscale=False,
            name="Past Light Cone"
        )
    
    
        # -------- Worldline: Stationary Observer --------
        t_line = np.linspace(0, 8, 100)
        x_stationary = np.zeros_like(t_line)
        y_stationary = np.zeros_like(t_line)
    
        worldline_rest = go.Scatter3d(
            x=x_stationary,
            y=y_stationary,
            z=t_line,
            mode="lines",
            line=dict(color="blue", width=6),
            name="Stationary Observer"
        )
    
        # -------- Worldline: Moving Observer --------
        x_moving = v * t_line
        y_moving = np.zeros_like(t_line)
    
        worldline_move = go.Scatter3d(
            x=x_moving,
            y=y_moving,
            z=t_line,
            mode="lines",
            line=dict(color="red", width=6),
            name="Moving Observer"
        )
    
        # -------- Build Figure --------
        fig = go.Figure(data=[future_cone, past_cone, worldline_rest, worldline_move])
    
    
        fig.update_layout(
            scene=dict(
                xaxis_title="Space (x)",
                yaxis_title="Space (y)",
                zaxis_title="Time (ct)",
                xaxis=dict(range=[-8, 8]),
                yaxis=dict(range=[-8, 8]),
                zaxis=dict(range=[-8, 8]),
            ),
            height=600,
            margin=dict(l=0, r=0, b=0, t=30)
        )
    
        st.plotly_chart(fig, use_container_width=True)
    
        st.markdown("""
        ### How to interpret this diagram
        
        - The **upper cone** is the **future light cone**  
        - The **lower cone** is the **past light cone**  
        - Events inside the cones can be causally connected  
        - Events outside cannot affect each other  
        
        - Blue line → observer at rest  
        - Red line → moving observer  
        
        Spacetime geometry determines what can influence what.
        """)
        
    
    if sr_topic == "Spacetime Paths & Causality":
        st.subheader("Events, Worldlines, and Light Cones")
    
        st.markdown("""
        This 3D spacetime diagram shows:
        
        - **Worldlines**: paths of observers through spacetime  
        - **Light cones**: limits of causal influence  
        - **Events**: points in spacetime  
        
        Only events inside the light cone can be causally connected.
        """)
        
        # -------- Controls --------
        v = st.slider("Moving Observer Speed (v/c)", 0.0, 0.9, 0.5, key="causal_v")
        
        event_x = st.slider("Event Position x", -6.0, 6.0, 2.0, key="event_x")
        event_y = st.slider("Event Position y", -6.0, 6.0, 0.0, key="event_y")
        event_t = st.slider("Event Time (ct)", -6.0, 6.0, 3.0, key="event_t")
        
        g = gamma(v)
        
        # -------- Light Cones --------
        t = np.linspace(0, 6, 50)
        theta = np.linspace(0, 2*np.pi, 50)
        T, Theta = np.meshgrid(t, theta)
        
        X = T * np.cos(Theta)
        Y = T * np.sin(Theta)
        
        Z_future = T
        Z_past = -T
        
        future_cone = go.Surface(
            x=X, y=Y, z=Z_future,
            opacity=0.35,
            showscale=False,
            name="Future Light Cone"
        )
        
        past_cone = go.Surface(
            x=X, y=Y, z=Z_past,
            opacity=0.35,
            showscale=False,
            name="Past Light Cone"
        )
        
        # -------- Worldlines --------
        t_line = np.linspace(-6, 6, 100)
        
        # Stationary observer
        worldline_rest = go.Scatter3d(
            x=np.zeros_like(t_line),
            y=np.zeros_like(t_line),
            z=t_line,
            mode="lines",
            line=dict(color="blue", width=6),
            name="Stationary Observer"
        )
        
        # Moving observer
        worldline_move = go.Scatter3d(
            x=v * t_line,
            y=np.zeros_like(t_line),
            z=t_line,
            mode="lines",
            line=dict(color="red", width=6),
            name="Moving Observer"
        )
        
        # -------- Event --------
        event = go.Scatter3d(
            x=[event_x],
            y=[event_y],
            z=[event_t],
            mode="markers",
            marker=dict(size=6, color="yellow"),
            name="Event"
        )
        
        # -------- Causality Check --------
        interval = event_t**2 - (event_x**2 + event_y**2)
        
        if interval > 0:
            causal_msg = "🟢 This event is inside the light cone (causally connected)."
        elif interval == 0:
            causal_msg = "🟡 This event lies on the light cone (light signal)."
        else:
            causal_msg = "🔴 This event is outside the light cone (no causal connection)."
        
        st.info(causal_msg)
        
        # -------- Build Figure --------
        fig = go.Figure(data=[future_cone, past_cone, worldline_rest, worldline_move, event])
        
        fig.update_layout(
            scene=dict(
                xaxis_title="Space (x)",
                yaxis_title="Space (y)",
                zaxis_title="Time (ct)",
                xaxis=dict(range=[-6, 6]),
                yaxis=dict(range=[-6, 6]),
                zaxis=dict(range=[-6, 6]),
            ),
            height=600,
            margin=dict(l=0, r=0, b=0, t=30)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        ### How to interpret this:
        
        - **Blue line** → observer at rest  
        - **Red line** → moving observer  
        - **Cones** → light cones (causal limits)  
        - **Yellow point** → event  
        
        Only events inside the cone can influence the observer.
        """)
    
    
        st.markdown("""
        ## Causality Principle in Special Relativity
        
        **Causality** means:
        
        > A cause must always occur **before** its effect.
        
        In Special Relativity, this is enforced by the **speed of light limit**:
        
        - No information or influence can travel faster than light  
        - Only events inside the **light cone** can be causally connected  
        - Events outside the light cone **cannot affect each other**
        """)
        
        
        st.markdown("""
        ### Why Light Cones Matter
        
        The light cone divides spacetime into three regions:
        
        1. **Future Light Cone**  
           Events that can be influenced by the present event  
        
        2. **Past Light Cone**  
           Events that could have influenced the present event  
        
        3. **Elsewhere (Outside the Cone)**  
           Events that are too far away in space to be causally connected  
        
        Because nothing can travel faster than light:
        
        - Causes and effects must stay **inside the light cone**  
        - This preserves the logical order of events  
        - No observer can see an effect happen before its cause
        """)
        
        
        st.markdown("""
        ### Relativity and Causality
        
        Different observers may disagree on:
        
        - The **time order** of distant events  
        - Whether two events are simultaneous  
        
        However:
        
        - All observers agree on **causal order**  
        - If one event can cause another, its order is the same for everyone  
        
        This is because causal events always lie **inside the light cone**.
        """)
        
        
        st.markdown("""
        ### Final Takeaway
        
        The geometry of spacetime replaces the classical idea of absolute time.
        
        Light cones define what is **physically possible**:
        
        - They protect causality  
        - They limit information flow  
        - They preserve cause-and-effect  
        
        In Special Relativity, **causality is a geometric property of spacetime**.
        """)
    
    
    if sr_topic == "Twin Paradox":
        st.subheader("Time Dilation and Asymmetric Aging")
    
        st.markdown("""
        One twin stays on Earth, while the other travels at high speed into space
        and then returns.
        
        Because the traveling twin moves at relativistic speed, they experience
        **less proper time** and age less.
        """)
        
        # -------- Controls --------
        v = st.slider("Spaceship Speed (v/c)", 0.0, 0.95, 0.8, key="twin_v")
        T = st.number_input("One-way Travel Time (Earth frame, years)", value=10.0, key="twin_T")
        
        g = gamma(v)
        
        # Earth twin time
        t_earth = 2 * T
        
        # Space twin proper time
        t_space = 2 * T / g
        
        st.info(f"Gamma (γ) = {g:.3f}")
        st.success(f"Earth Twin Age Increase = {t_earth:.2f} years")
        st.success(f"Space Twin Age Increase = {t_space:.2f} years")
        
        st.divider()
        st.caption("Note: The initial age of both twins is assumed to be 0 years. The values shown represent the *increase* in age during the journey.")
    
        
        # -------- Worldline Plot --------
        st.subheader("Spacetime Worldlines")
        
        t = np.linspace(0, 2*T, 200)
        
        # Earth twin worldline
        x_earth = np.zeros_like(t)
        
        # Space twin worldline (out + back)
        x_space = np.piecewise(
            t,
            [t < T, t >= T],
            [lambda t: v*t, lambda t: v*(2*T - t)]
        )
        
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Plot worldlines
        ax.plot(x_earth, t, label="Earth Twin", color="blue", linewidth=2)
        ax.plot(x_space, t, label="Space Twin", color="red", linewidth=2)
        
        # Turnaround point
        ax.scatter(v*T, T, color="black", zorder=5)
        ax.text(v*T, T, " Turnaround", fontsize=9)
        
        ax.set_xlabel("Space (x)")
        ax.set_ylabel("Time (t)")
        ax.set_title("Twin Paradox: Spacetime Worldlines")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        st.divider()
        
        # -------- Animation --------
        st.subheader("Animated Twin Journey")
        
        play_twin = st.button("▶ Play Twin Journey")
        
        placeholder = st.empty()
        
        frames = 60
        
        if play_twin:
        
            for i in range(frames + 1):
        
                frac = i / frames
                current_t = 2 * T * frac
        
                if current_t <= T:
                    x_ship = v * current_t
                else:
                    x_ship = v * (2*T - current_t)
        
                fig2, ax2 = plt.subplots(figsize=(6, 2))
        
                # Earth
                ax2.scatter(0, 0, color="blue", s=80, label="Earth Twin")
        
                # Spaceship
                ax2.scatter(x_ship, 0, color="red", s=80, label="Space Twin")
        
                ax2.set_xlim(-1, v*T + 1)
                ax2.set_ylim(-1, 1)
                ax2.axis("off")
                ax2.legend(loc="upper right")
        
                placeholder.pyplot(fig2)
                time.sleep(0.1)
        
        st.divider()
        
        # -------- Explanation --------
        st.markdown("""
        ### Why the Traveling Twin Ages Less
        
        - The Earth twin stays in one inertial frame  
        - The space twin **changes frames** at the turnaround  
        - Proper time depends on the **path through spacetime**  
        
        In spacetime geometry:
        
        > The straight worldline (Earth twin) has **maximum proper time**  
        > The bent worldline (Space twin) has **less proper time**
        
        So the result is not a paradox — it is a geometric effect.
        """)
        
        st.markdown("""
        ### Key Takeaway
        
        The Twin Paradox is not about who is "really moving".
        
        It is about:
        
        - Worldlines  
        - Proper time  
        - Spacetime geometry  
        
        Relativity replaces intuition with **geometry**.
        """)
        
        
        
# -----------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------
# -------------------------------General Relativity---------------------------------
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------



elif mode == "General Relativity":

    gr_topic = st.sidebar.selectbox(
        "Choose Topic",
        [
            "Gravitational Time Dilation",
            "Black Hole & Event Horizon",
            "Light Bending (Gravitational Lensing)",
            "Orbits & Geodesics",
            "Gravitational Redshift",
            "Gravitational Waves",
            "Cosmology (Expanding Universe)",
            "3D Universe Expansion",
            "Bubble Universe Model"
        ]
    )

    st.header(gr_topic)



    if gr_topic == "Gravitational Time Dilation":

        st.subheader("How Gravity Affects the Flow of Time")
    
        st.markdown("""
        In General Relativity, gravity affects the flow of time.
    
        Clocks closer to a massive object run **slower** than clocks far away.
        """)
    
        st.latex(r"\Delta t_\infty = \frac{\Delta \tau}{\sqrt{1 - \frac{2GM}{rc^2}}}")
    
        st.divider()
    
        # -------- Schwarzschild Radius --------
        st.latex(r"r_s = \frac{2GM}{c^2}")
    
        st.markdown("""
        ### Schwarzschild Radius
    
        The **Schwarzschild radius** is the critical radius at which a mass becomes a black hole.
    
        - If an object is compressed inside this radius, not even light can escape  
        - This forms an **event horizon**  
        - For Earth, rₛ ≈ 9 mm  
        - For the Sun, rₛ ≈ 3 km  
        """)
    
        st.divider()
    
        # -------- Constants (scaled units) --------
        G = 1     # Gravitational constant (scaled)
        c = 1     # Speed of light (scaled)
    
        # -------- Controls --------
        M = st.slider("Mass of Object (M)", 0.1, 10.0, 5.0, key="gr_mass")
        r = st.slider("Distance from Center (r)", 1.1, 20.0, 8.0, key="gr_radius")
    
        proper_time = st.number_input("Proper Time Δτ (seconds)", value=10.0, key="gr_time")
    
        # Schwarzschild radius
        r_s = 2 * G * M / c**2
    
        # -------- Time Dilation Calculation --------
        if r <= r_s:
            st.error("r ≤ rₛ : You are inside the event horizon. Time dilation becomes infinite for a distant observer.")
            time_factor = None
        else:
            time_factor = 1 / np.sqrt(1 - r_s / r)
            dilated_time = proper_time * time_factor
    
            st.info(f"Schwarzschild Radius rₛ = {r_s:.3f}")
            st.success(f"Time at Infinity Δt∞ = {dilated_time:.3f} seconds")
    
            st.caption("Note: Time runs slower closer to the massive object.")
    
        st.divider()
    
        # -------- Visualization --------
        st.subheader("Time Flow Comparison")
    
        r_values = np.linspace(r_s + 0.1, 20, 100)
        time_factors = 1 / np.sqrt(1 - r_s / r_values)
    
        fig, ax = plt.subplots(figsize=(6, 4))
    
        ax.plot(r_values, time_factors, color="purple")
        ax.axvline(r_s, color="black", linestyle="--", label="Event Horizon")
    
        ax.set_xlabel("Distance from Center (r)")
        ax.set_ylabel("Time Dilation Factor")
        ax.set_title("Gravitational Time Dilation vs Distance")
        ax.legend()
        ax.grid(True)
    
        st.pyplot(fig)
    
        st.divider()
    
        # -------- Optional Animation --------
        st.subheader("Animated Clock Near a Massive Object")
    
        play_gr = st.button("▶ Play Gravitational Clock Animation")
        placeholder = st.empty()
    
        if time_factor is None:
            st.warning("Animation disabled: You are inside the event horizon.")
        else:
            if play_gr:
                for i in range(30):
                    local_time = i * 0.5
                    far_time = local_time * time_factor
    
                    fig2, ax2 = plt.subplots(figsize=(5, 2))
    
                    ax2.barh(["Far Away Clock"], [far_time], color="green")
                    ax2.barh(["Near Mass Clock"], [local_time], color="red")
    
                    ax2.set_xlim(0, far_time + 1)
                    ax2.set_xlabel("Elapsed Time")
                    ax2.set_title("Gravitational Time Dilation")
    
                    placeholder.pyplot(fig2)
                    time.sleep(0.1)
    
        st.divider()
    
        # -------- Explanation --------
        st.markdown("""
        ### What is happening?
    
        - Gravity curves spacetime  
        - Stronger gravity → slower clocks  
        - Near a black hole, time slows dramatically  
        - At the event horizon, time appears to stop for a distant observer  
    
        This effect has been confirmed experimentally (e.g., GPS satellites).
        """)
    
        st.markdown("""
        ### Key Insight
    
        - Motion slows time (Special Relativity)  
        - Gravity slows time (General Relativity)  
    
        In GR, time dilation is a **geometric effect of curved spacetime**.
        """)
    
    
    if gr_topic == "Black Hole & Event Horizon":

        st.subheader("When Spacetime Becomes Extreme")
    
        st.markdown("""
        A **black hole** is a region of spacetime where gravity is so strong
        that nothing — not even light — can escape.
    
        The boundary of this region is called the **event horizon**.
        """)
    
        st.latex(r"r_s = \frac{2GM}{c^2}")
    
        st.divider()
    
        # -------- Constants (scaled units) --------
        G = 1
        c = 1
    
        # -------- Controls --------
        M = st.slider("Black Hole Mass (M)", 0.5, 10.0, 5.0, key="bh_mass")
    
        # Schwarzschild radius
        r_s = 2 * G * M / c**2
    
        st.info(f"Schwarzschild Radius rₛ = {r_s:.3f}")
    
        st.markdown("""
        ### What Is the Event Horizon?
        
        The **event horizon** is the boundary where escape becomes impossible.
        
        At this radius:
        
        - Even light cannot move outward  
        - Time appears to slow down infinitely for a distant observer  
        - All future directions lead inward  
        
        The event horizon is not a physical surface —  
        it is a **geometric boundary in spacetime**.
        """)

    
        st.divider()
    
        # -------- Radial Spacetime Visualization --------
        st.subheader("Spacetime Around a Black Hole")
    
        r = np.linspace(r_s + 0.1, 20, 300)
    
        curvature = 1 / np.sqrt(1 - r_s / r)
    
        fig, ax = plt.subplots(figsize=(6, 4))
    
        ax.plot(r, curvature, color="black")
        ax.axvline(r_s, color="red", linestyle="--", label="Event Horizon")
    
        ax.set_xlabel("Radial Distance r")
        ax.set_ylabel("Spacetime Curvature Factor")
        ax.set_title("Spacetime Warping Near a Black Hole")
        ax.legend()
        ax.grid(True)
    
        st.pyplot(fig)
    
        st.caption("Spacetime curvature increases dramatically near the event horizon.")
    
        st.divider()
    
        # -------- Light Escape Visualization --------
        st.subheader("Can Light Escape?")
    
        r_test = st.slider("Light Emission Radius r", r_s + 0.1, 20.0, 10.0, key="light_r")
    
        if r_test <= r_s:
            st.error("Light cannot escape. This point is inside the event horizon.")
        else:
            st.success("Light can escape to infinity.")
    
        st.divider()
        
        st.markdown("""
        ### Why Can't Light Escape?
        
        Light always travels locally at the speed of light.
        
        However, near a black hole, spacetime is curved so strongly that the **structure of possible paths** changes.
        
        Let \( r_s \) be the Schwarzschild radius (event horizon).
        
        - **For \( r > r_s \)**  
          Light can move outward and escape to infinity.
        
        - **For \( r = r_s \)**  
          Light remains trapped at the event horizon.  
          To a distant observer, it appears "frozen" in time.
        
        - **For \( r < r_s \)**  
          All future paths point inward.  
          Even light must move toward the center.
        
        This happens because:
        
        - Spacetime itself is strongly curved  
        - The outward direction disappears  
        - All light paths point inward  
        
        So light is not slowed down —  
        it is **trapped by spacetime geometry**.
        """)

    
        # -------- Simple Animation --------
        st.subheader("Infall Toward a Black Hole (Improved Animation)")

        play_fall = st.button("▶ Play Infall Animation")
        
        if play_fall:
        
            r_positions = np.linspace(20, r_s + 0.3, 60)
        
            frames = []
            for r_pos in r_positions:
                frames.append(
                    go.Frame(
                        data=[
                            go.Scatter(
                                x=[0], y=[0],
                                mode="markers",
                                marker=dict(size=40, color="black"),
                                name="Black Hole"
                            ),
                            go.Scatter(
                                x=[r_pos], y=[0],
                                mode="markers",
                                marker=dict(size=15, color="blue"),
                                name="Falling Object"
                            )
                        ]
                    )
                )
        
            fig = go.Figure(
                data=[
                    go.Scatter(x=[0], y=[0], mode="markers",
                               marker=dict(size=40, color="black"),
                               name="Black Hole"),
                    go.Scatter(x=[20], y=[0], mode="markers",
                               marker=dict(size=15, color="blue"),
                               name="Falling Object")
                ],
                layout=go.Layout(
                    xaxis=dict(range=[-22, 22], showgrid=False, zeroline=False),
                    yaxis=dict(range=[-10, 10], showgrid=False, zeroline=False),
                    height=400,
                    title="Object Falling Into a Black Hole",
                    updatemenus=[dict(
                        type="buttons",
                        showactive=False,
                        buttons=[dict(
                            label="Play",
                            method="animate",
                            args=[None, {"frame": {"duration": 50, "redraw": True},
                                         "fromcurrent": True}]
                        )]
                    )]
                ),
                frames=frames
            )
        
            # Event horizon circle
            fig.add_shape(
                type="circle",
                xref="x", yref="y",
                x0=-r_s, y0=-r_s,
                x1=r_s, y1=r_s,
                line=dict(color="red", width=3),
                name="Event Horizon"
            )
        
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        ### Why Does the Object Fall Into the Black Hole?
        
        In General Relativity, gravity is not a force in the usual sense.  
        Instead, mass **curves spacetime**, and objects simply follow the natural paths
        (called *geodesics*) in this curved geometry.
        
        As an object approaches a black hole:
        
        - Spacetime becomes increasingly curved  
        - All possible future paths point inward  
        - Escape becomes impossible  
        
        This is why the object inevitably falls into the black hole.
        """)
        
        
        st.markdown("""
        ### Key Takeaway
        
        A black hole does not trap objects by pulling harder.
        
        It traps them because **spacetime itself is curved so strongly**  
        that escape paths no longer exist.
        
        Gravity in General Relativity is geometry.
        """)

    if gr_topic == "Light Bending (Gravitational Lensing)":
        st.subheader("How Gravity Curves the Path of Light")

        st.markdown("""
        In General Relativity, massive objects curve spacetime.
        
        Light follows these curved paths, causing **gravitational lensing**.
        """)
        
        st.latex(r"\alpha \approx \frac{4GM}{c^2 b}")
        
        st.divider()
        
        # -------- Constants (scaled units) --------
        G = 1
        c = 1
        
        # -------- Controls --------
        M = st.slider("Lens Mass (M)", 0.5, 10.0, 5.0, key="lens_mass")
        b = st.slider("Impact Parameter (b)", 1.5, 10.0, 5.0, key="impact_b")
        
        # Bending angle
        alpha = 4 * G * M / (c**2 * b)
        
        st.info(f"Deflection Angle α ≈ {alpha:.3f} radians")
        
        st.divider()
        
        # -------- Light Ray Visualization (2D Curved Spacetime) --------
        st.subheader("Spacetime Curvature and Light Bending (2D)")
        
        M = st.slider("Mass (M)", 1.0, 10.0, 5.0, key="lens_mass_2d")
        
        # Spacetime grid (fabric)
        x = np.linspace(-20, 20, 200)
        y = np.linspace(-10, 10, 80)
        X, Y = np.meshgrid(x, y)
        
        R = np.sqrt(X**2 + Y**2)
        Z = -M / (R + 2)   # Curvature profile
        
        fig, ax = plt.subplots(figsize=(8, 4))
        
        # Draw spacetime fabric
        for i in range(0, len(y), 4):
            ax.plot(x, Y[i] + Z[i]*0.6, color="lightgray", linewidth=1)
        
        # Light rays (bending around the mass)
        x_vals = np.linspace(-20, 20, 400)
        
        def light_path(y0):
            bend = (4 * M) * x_vals / (x_vals**2 + y0**2 + 12)
            bend = bend * np.exp(-0.03 * np.abs(x_vals))  # flatten far away
            return y0 + bend
        
        for y0 in [-6, -3, 0, 3, 6]:
            y_ray = light_path(y0)
            ax.plot(x_vals, y_ray, color="gold", linewidth=2)
        
        # Central mass
        ax.scatter(0, 0, s=250, color="black", zorder=5)
        
        # Labels and styling
        ax.set_xlim(-20, 20)
        ax.set_ylim(-10, 10)
        ax.set_title("Light Bending Due to Curved Spacetime")
        ax.axis("off")
        
        st.pyplot(fig)

        
        
        st.subheader("Animated Light Bending in Curved Spacetime")

        M = st.slider("Mass (M)", 1.0, 10.0, 5.0, key="anim_mass")
        
        # Spacetime surface
        x = np.linspace(-10, 10, 60)
        y = np.linspace(-10, 10, 60)
        X, Y = np.meshgrid(x, y)
        R = np.sqrt(X**2 + Y**2)
        Z = -M / (R + 1)
        
        surface = go.Surface(
            x=X, y=Y, z=Z,
            colorscale="Blues",
            opacity=0.9,
            showscale=False
        )
        
        # Light ray geometry
        x_vals = np.linspace(-10, 10, 300)
        
        def light_path(y0, progress):
            x_visible = x_vals[x_vals < -10 + 20 * progress]
            bend = (4 * M) * x_visible / (x_visible**2 + y0**2 + 6)
            y = y0 + bend
            r = np.sqrt(x_visible**2 + y**2)
            z = -M / (r + 1)
            return x_visible, y, z
        
        frames = []
        y_rays = [-6, -3, 0, 3, 6]
        
        for step in range(60):
            progress = step / 60
            data = [surface]
        
            for y0 in y_rays:
                xr, yr, zr = light_path(y0, progress)
                data.append(go.Scatter3d(
                    x=xr, y=yr, z=zr + 0.25,
                    mode="lines",
                    line=dict(color="gold", width=5),
                    showlegend=False
                ))
        
            # Central mass
            data.append(go.Scatter3d(
                x=[0], y=[0], z=[-M],
                mode="markers",
                marker=dict(size=10, color="black"),
                showlegend=False
            ))
        
            frames.append(go.Frame(data=data))
        
        fig = go.Figure(
            data=frames[0].data,
            layout=go.Layout(
                title="Light Bending in Curved Spacetime",
                scene=dict(
                    xaxis=dict(range=[-10, 10]),
                    yaxis=dict(range=[-10, 10]),
                    zaxis=dict(range=[-M-2, 1]),
                    xaxis_title="Space (x)",
                    yaxis_title="Space (y)",
                    zaxis_title="Spacetime Curvature"
                ),
                height=650,
                updatemenus=[dict(
                    type="buttons",
                    showactive=False,
                    buttons=[dict(
                        label="▶ Play",
                        method="animate",
                        args=[None, {
                            "frame": {"duration": 60, "redraw": True},
                            "fromcurrent": True
                        }]
                    )]
                )]
            ),
            frames=frames
        )
        
        st.plotly_chart(fig, use_container_width=True)

        
        # -------- Explanation --------
        st.markdown("""
        ### Why Does Light Bend?
        
        In General Relativity:
        
        - Mass curves spacetime  
        - Light follows the curved geometry  
        - So its path appears bent  
        
        Light is not pulled like a particle —  
        it is following the **shape of spacetime**.
        """)
        
        st.markdown("""
        ### What Is Gravitational Lensing?
        
        When light from a distant object passes near a massive body:
        
        - The light bends  
        - Multiple images can appear  
        - Rings and arcs can form  
        
        This effect is called **gravitational lensing** and is used to:
        
        - Detect dark matter  
        - Observe distant galaxies  
        - Test General Relativity  
        """)
        
        st.markdown("""
        ### Key Takeaway
        
        Gravity does not just move objects —  
        it reshapes the paths of light itself.
        
        Spacetime geometry controls how light travels.
        """)
   
    if gr_topic == "Orbits & Geodesics":

        st.subheader("Motion in Curved Spacetime")

        st.markdown("""
        In General Relativity, objects do not move because of a force.
        
        They move along **geodesics** —  
        the straightest possible paths in **curved spacetime**.
        """)
        
        st.divider()
        
        # -------- Concept Explanation --------
        st.markdown("""
        ### What is a Geodesic?
        
        A geodesic is the natural path an object follows in spacetime.
        
        - In flat space → straight lines  
        - In curved spacetime → curved paths  
        
        Orbits exist because spacetime itself is curved by mass.
        """)
        
        st.divider()
        
        # -------- Motion Type Selector --------
        motion_type = st.selectbox(
            "Choose Type of Motion",
            [
                "Stable Circular Orbit",
                "Elliptical Orbit",
                "Spiral Infall",
                "Escape Trajectory"
            ]
        )
        
        # -------- Controls --------
        M = st.slider("Central Mass (M)", 1.0, 10.0, 5.0, key="geo_mass")
        r0 = st.slider("Initial Distance (r₀)", 4.0, 15.0, 8.0, key="geo_r0")
        e = st.slider("Eccentricity (e)", 0.0, 0.9, 0.3, key="geo_e")
        
        st.divider()
        
        # -------- Trajectory Models --------
        theta = np.linspace(0, 2*np.pi, 600)
        
        if motion_type == "Stable Circular Orbit":
            r = r0 * np.ones_like(theta)
            description = "A stable geodesic where the object remains at constant distance."
        
        elif motion_type == "Elliptical Orbit":
            r = r0 / (1 + e * np.cos(theta))
            description = "A bound geodesic where the distance changes periodically."
        
        elif motion_type == "Spiral Infall":
            r = r0 * np.exp(-0.15 * theta)
            description = "An unstable geodesic that leads into the central mass."
        
        elif motion_type == "Escape Trajectory":
            r = r0 * (1 + 0.3 * theta)
            description = "An unbound geodesic where the object escapes to infinity."
        
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        
        # -------- Plot --------
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Central mass
        ax.scatter(0, 0, s=300, color="black", label="Central Mass")
        
        # Trajectory
        ax.plot(x, y, color="orange", linewidth=2, label="Geodesic Path")
        
        ax.set_aspect("equal")
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)
        ax.set_title("Geodesic Motion in Curved Spacetime")
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        st.caption(description)
        
        st.divider()
        
        # -------- Animation --------
        st.subheader("Animated Motion")
        
        play_geo = st.button("▶ Play Motion")
        
        placeholder = st.empty()
        
        if play_geo:
            for i in range(0,300,5):
                fig2, ax2 = plt.subplots(figsize=(5, 5))
        
                ax2.scatter(0, 0, s=300, color="black")
        
                ax2.plot(x, y, color="lightgray")
        
                ax2.scatter(x[i], y[i], color="orange", s=80)
        
                ax2.set_aspect("equal")
                ax2.set_xlim(-20, 20)
                ax2.set_ylim(-20, 20)
                ax2.set_title("Object Following a Geodesic")
                ax2.axis("off")
        
                placeholder.pyplot(fig2)
                time.sleep(0.005)
        
        st.divider()
        
        # -------- GR Explanation --------
        st.markdown("""
        ### Why Do These Paths Exist?
        
        Mass curves spacetime.
        
        This curvature creates natural paths (geodesics).
        
        Objects follow these paths automatically —  
        no force is required.
        """)
        
        st.markdown("""
        ### Why Does Strong Gravity Matter?
        
        Near very massive objects:
        
        - Geodesics become more curved  
        - Stable orbits can disappear  
        - Objects can spiral inward  
        - Even light can orbit  
        
        This is a purely relativistic effect.
        """)
        
        st.markdown("""
        ### Key Takeaway
        
        In General Relativity:
        
        Motion is geometry.
        
        Objects move the way spacetime tells them to move.
        """)

    if gr_topic == "Gravitational Redshift":

        st.subheader("How Gravity Changes Light’s Frequency")
    
        st.markdown("""
        Light escaping from a strong gravitational field loses energy.
    
        This causes its wavelength to increase — a phenomenon called **gravitational redshift**.
        """)
    
        st.latex(r"z = \frac{1}{\sqrt{1 - \frac{2GM}{rc^2}}} - 1")
    
        G, c = 1, 1
    
        M = st.slider("Mass (M)", 1.0, 10.0, 5.0)
        r = st.slider("Emission Radius (r)", 3.0, 20.0, 8.0)
    
        r_s = 2 * G * M / c**2
    
        if r <= r_s:
            st.error("Light cannot escape from inside the event horizon.")
        else:
            z = 1 / np.sqrt(1 - r_s / r) - 1
            st.success(f"Redshift z = {z:.3f}")
    
        st.markdown("""
        ### Physical Meaning
    
        - Light loses energy while climbing out of gravity  
        - Its frequency decreases  
        - Its wavelength increases  
        - We observe it as redshift  
        """)
        
        st.caption("Gravitational redshift has been measured using atomic clocks and satellites.")
        

    if gr_topic == "Gravitational Waves":

        st.subheader("Ripples in the Fabric of Spacetime")
    
        st.markdown("""
        Gravitational waves are ripples in spacetime caused by
        accelerating massive objects, such as black hole mergers.
        """)
    
        A = st.slider("Wave Amplitude", 0.1, 1.0, 0.5)
        f = st.slider("Wave Frequency", 1.0, 10.0, 3.0)
    
        t = np.linspace(0, 10, 500)
        h = A * np.sin(2 * np.pi * f * t)
    
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(t, h, color="purple")
        ax.set_title("Gravitational Wave Signal")
        ax.set_xlabel("Time")
        ax.set_ylabel("Strain h(t)")
        ax.grid(True)
    
        st.pyplot(fig)
    
        st.markdown("""
        ### What Are Gravitational Waves?
    
        - They are ripples in spacetime  
        - Produced by massive accelerating objects  
        - Travel at the speed of light  
        - Detected by LIGO & Virgo  
    
        They confirm Einstein’s predictions.
        """)
        
    if gr_topic == "Cosmology (Expanding Universe)":

        st.subheader("The Large-Scale Evolution of the Cosmos")

        st.markdown("""
        Modern cosmology describes the universe as **expanding**.
        
        This does not mean galaxies are flying away from a central explosion.  
        Instead, **space itself is stretching**.
        """)
        
        st.latex(r"v = H_0 d")
        
        st.markdown("""
        ### Hubble’s Law
        
        - **v** = recession velocity  
        - **d** = distance  
        - **H₀** = expansion rate  
        
        Farther galaxies move away faster because space expands uniformly.
        """)
        
        # ------------------ 2D Scale Factor Plot ------------------
        
        H0 = st.slider("Hubble Constant (H₀)", 50, 100, 70, key="H0_basic")
        
        t = np.linspace(0, 10, 200)
        a = np.exp(H0 * t / 1000)
        
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(t, a, color="blue")
        ax.set_title("Scale Factor of the Universe")
        ax.set_xlabel("Time")
        ax.set_ylabel("Scale Factor a(t)")
        ax.grid(True)
        
        st.pyplot(fig)
        
        st.markdown("""
        ### What Does This Mean?
        
        - Space itself expands  
        - Galaxies are carried apart  
        - No central explosion point  
        - Expansion happens everywhere  
        
        This is **geometric expansion**, not ordinary motion.
        """)
        
        st.divider()
        
        # ------------------ Plotly Animation ------------------
        
        st.subheader("Expanding Universe (Plotly Animation)")
        
        st.markdown("""
        The universe is expanding because **space itself is stretching**.
        
        Galaxies move apart without any central explosion.
        """)
        
        H0 = st.slider("Expansion Rate (H₀)", 50, 100, 70, key="H0_anim")
        
        np.random.seed(1)
        galaxies = np.random.randn(80, 2)
        
        frames = []
        
        for step in range(100):
            scale = 1 + step * H0 / 2000
            pos = galaxies * scale
        
            frames.append(go.Frame(
                data=[
                    go.Scatter(
                        x=pos[:, 0],
                        y=pos[:, 1],
                        mode="markers",
                        marker=dict(size=10, color="cyan")
                    )
                ]
            ))
        
        fig = go.Figure(
            data=[go.Scatter(
                x=galaxies[:, 0],
                y=galaxies[:, 1],
                mode="markers",
                marker=dict(
                    size=14,
                    color="lightblue",
                    symbol="circle",
                    opacity=0.85,
                    line=dict(width=1, color="white")
                )
            )],
            layout=go.Layout(
                title="Expansion of the Universe",
                xaxis=dict(range=[-10, 10], showgrid=False, zeroline=False),
                yaxis=dict(range=[-10, 10], showgrid=False, zeroline=False),
                plot_bgcolor="black",
                paper_bgcolor="black",
                font=dict(color="white"),
                updatemenus=[dict(
                    type="buttons",
                    showactive=False,
                    buttons=[dict(
                        label="▶ Play",
                        method="animate",
                        args=[None, {
                            "frame": {"duration": 100, "redraw": True},
                            "fromcurrent": True
                        }]
                    )]
                )]
            ),
            frames=frames
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        ### What Is Happening?
        
        - Space itself is expanding  
        - Galaxies are carried apart  
        - No central explosion  
        - Expansion occurs everywhere  
        
        This is a geometric expansion of spacetime.
        """)


    if gr_topic == "3D Universe Expansion":

        st.subheader("Visualizing Cosmic Expansion in Three Dimensions")
    
        st.markdown("""
        In three dimensions, cosmic expansion means that **all distances increase**.
    
        Every observer sees distant galaxies moving away,  
        even though there is no special center of expansion.
        """)
    
        st.markdown("""
        ### What This Visualization Shows
    
        - Galaxies distributed in 3D space  
        - Space expanding uniformly  
        - All points separating from each other  
        - No preferred direction or center  
        """)
    
        H0 = st.slider("Expansion Rate (H₀)", 50, 100, 70, key="H0_3d")
        frames_count = st.slider("Expansion Duration", 40, 120, 80, key="frames_3d")
    
        np.random.seed(2)
        galaxies = np.random.randn(120, 3)
        sizes = np.random.randint(6, 14, size=len(galaxies))
    
        frames = []
    
        for step in range(frames_count):
            scale = np.exp(step * H0 / 2000)
            pos = galaxies * scale
    
            frames.append(go.Frame(
                data=[go.Scatter3d(
                    x=pos[:, 0],
                    y=pos[:, 1],
                    z=pos[:, 2],
                    mode="markers",
                    marker=dict(size=sizes, color="lightblue", opacity=0.85)
                )]
            ))
    
        fig = go.Figure(
            data=[go.Scatter3d(
                x=galaxies[:, 0],
                y=galaxies[:, 1],
                z=galaxies[:, 2],
                mode="markers",
                marker=dict(size=sizes, color="lightblue", opacity=0.85)
            )],
            layout=go.Layout(
                title="3D Expansion of the Universe",
                scene=dict(
                    xaxis=dict(range=[-40, 40], showbackground=False),
                    yaxis=dict(range=[-40, 40], showbackground=False),
                    zaxis=dict(range=[-40, 40], showbackground=False),
                    bgcolor="#02040f"
                ),
                paper_bgcolor="#02040f",
                font=dict(color="white"),
                updatemenus=[dict(
                    type="buttons",
                    showactive=False,
                    buttons=[dict(
                        label="▶ Play",
                        method="animate",
                        args=[None, {"frame": {"duration": 80, "redraw": True}, "fromcurrent": True}]
                    )]
                )]
            ),
            frames=frames
        )
    
        st.plotly_chart(fig, use_container_width=True)
    
        st.markdown("""
        ### Physical Interpretation
    
        Each galaxy can be treated as stationary in space.
    
        As spacetime expands, the metric distances between them increase.
    
        This is a geometric effect, not a force.
        """)
    
        st.markdown("""
        ### Key Idea
    
        Expansion is a property of **spacetime itself**,  
        not the motion of galaxies through space.
        """)
        
    if gr_topic == "Bubble Universe Model":

        st.subheader("A Spherical View of Cosmic Expansion")
    
        st.markdown("""
        The bubble (or balloon) model is a visualization tool.
    
        It helps us understand how expansion works **without requiring a center**.
        """)
    
        st.markdown("""
        ### The Balloon Analogy
    
        Imagine dots drawn on the surface of a balloon.
    
        As the balloon inflates:
    
        - The dots move apart  
        - No dot is at the center  
        - Expansion happens everywhere  
    
        The dots represent galaxies.  
        The balloon represents space.
        """)
    
        H0 = st.slider("Expansion Rate (H₀)", 50, 100, 70, key="H0_sphere")
        frames_count = st.slider("Expansion Duration", 40, 120, 80, key="frames_sphere")
    
        np.random.seed(3)
        N = 150
        theta = np.random.uniform(0, 2*np.pi, N)
        phi = np.random.uniform(0, np.pi, N)
    
        R0 = 5
        x0 = R0 * np.sin(phi) * np.cos(theta)
        y0 = R0 * np.sin(phi) * np.sin(theta)
        z0 = R0 * np.cos(phi)
    
        galaxies = np.column_stack((x0, y0, z0))
        sizes = np.random.randint(6, 14, size=N)
    
        frames = []
    
        for step in range(frames_count):
            scale = np.exp(step * H0 / 2500)
            pos = galaxies * scale
    
            frames.append(go.Frame(
                data=[go.Scatter3d(
                    x=pos[:, 0],
                    y=pos[:, 1],
                    z=pos[:, 2],
                    mode="markers",
                    marker=dict(size=sizes, color="lightblue", opacity=0.85)
                )]
            ))
    
        fig = go.Figure(
            data=[go.Scatter3d(
                x=galaxies[:, 0],
                y=galaxies[:, 1],
                z=galaxies[:, 2],
                mode="markers",
                marker=dict(size=sizes, color="lightblue", opacity=0.85)
            )],
            layout=go.Layout(
                title="Bubble Universe Expansion",
                scene=dict(
                    xaxis=dict(range=[-40, 40], showbackground=False),
                    yaxis=dict(range=[-40, 40], showbackground=False),
                    zaxis=dict(range=[-40, 40], showbackground=False),
                    bgcolor="#02040f"
                ),
                paper_bgcolor="#02040f",
                font=dict(color="white"),
                updatemenus=[dict(
                    type="buttons",
                    showactive=False,
                    buttons=[dict(
                        label="▶ Play",
                        method="animate",
                        args=[None, {"frame": {"duration": 80, "redraw": True}, "fromcurrent": True}]
                    )]
                )]
            ),
            frames=frames
        )
    
        st.plotly_chart(fig, use_container_width=True)
    
        st.markdown("""
        ### What This Model Teaches
    
        - The universe does not expand from a center  
        - Expansion happens everywhere  
        - The bubble is a visualization tool  
        - The real universe has no physical boundary  
        """)


#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#-----------------------------------END----------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

        

