[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/varying-particle-system-properties-over-time.html)
  * [中文](/cn/current/Manual/varying-particle-system-properties-over-time.html)
  * [日本語](/ja/current/Manual/varying-particle-system-properties-over-time.html)
  * [한국어](/kr/current/Manual/varying-particle-system-properties-over-time.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/varying-particle-system-properties-over-time.html)
  * [中文](/cn/current/Manual/varying-particle-system-properties-over-time.html)
  * [日本語](/ja/current/Manual/varying-particle-system-properties-over-time.html)
  * [한국어](/kr/current/Manual/varying-particle-system-properties-over-time.html)

  * [Visual effects](visual-effects.html)
  * [Particle systems](ParticleSystems.html)
  * Vary Particle System properties over time

[](PartSysUsage.html)

Create and view a Particle System

[](configuring-particles.html)

Configuring particles

# Vary Particle System properties over time

Many of the numeric properties of particles or even the whole **Particle
System** A component that simulates fluid entities such as liquids, clouds and
flames by generating and animating large numbers of small 2D images in the
scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) can vary over time. Unity
provides several different methods of specifying how this variation happens:

  * **Constant:** The property’s value is fixed throughout its lifetime.
  * **Curve:** The value is specified by a curve/graph.
  * **Random Between Two Constants:** Two constant values define the upper and lower bounds for the value; the actual value varies randomly over time between those bounds.
  * **Random Between Two Curves:** Two curves define the upper and lower bounds of the value at a given point in its lifetime; the current value varies randomly between those bounds.

When you set a property to **Curve** or **Random Between Two Curves** , the
Particle System Curves editor appears at the bottom of the **Inspector** A
Unity window that displays information about the currently selected
GameObject, asset or project settings, allowing you to inspect and edit the
values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector):

![](../uploads/Main/ParticleSystemCurve.png)

To edit a curve, click and drag an end point or key to reshape the curve:

![](../uploads/Main/ParticleSystemCurveKeys.png)

Particle System curves are similar to [Animation curves](animeditor-
AnimationCurves.html)Allows you to add data to an imported clip so you can
animate the timings of other items based on the state of an animator. For
example, for a game set in icy conditions, you could use an extra animation
curve to control the emission rate of a particle system to show the player’s
condensing breath in the cold air. [More
info](AnimationCurvesOnImportedClips.html)  
See in [Glossary](Glossary.html#AnimationCurves). For information on using
curves, see the documentation on [Editing Curves](EditingCurves.html).

The Particle System Curves editor has the following buttons:

  * **Optimize** : Fits the curve into four or fewer keys to build a fast evaluator called a Polynomial, which is more efficient than reading the unoptimized curve.
  * **Remove** : Deletes the selected curve.

To edit the way in which the Particle System plays curves, click the cog next
to a selected key and choose one of the following options:

  * **Loop** : Plays the curve the specified number times over a particle’s life. For example, if you make a curve that scales a particle’s size up and down, you can tell it to loop multiple times, which causes the “up and down” animation to happen multiple times before the particle dies, instead of just once.
  * **Ping Pong** To repeatedly play an animation to the end, then in reverse back to the beginning, in a loop.  
See in [Glossary](Glossary.html#PingPong): Similar to **Loop** , but plays the
curve forwards then backwards in a continuous oscillation.

  * **Clamp** : Limits particle queries that fall outside the curve time range to the first or last value of the curve.

The **Start Color** property in the main module has the following options:

  * **Color:** All particles start with this color throughout the lifetime of the Particle System. Particles can still change color during their lifetime.
  * **Gradient:** The Particle System emits particles which start with the colour at the beginning of the gradient, and end at the colour at the end of the gradient. The gradient line represents the lifetime of the Particle System; the Particle System picks a color from the gradient at the point corresponding to the current age of the Particle System.
  * **Random Between Two Colors:** The Particle System chooses a starting particle color from a random linear interpolation between the two given colors.
  * **Random Between Two Gradients:** The Particle System chooses a color from each of the given gradients at the point corresponding to the current age of the system. The starting particle color is chosen as a random linear interpolation between the two chosen colors.
  * **Random Color:** Similar to **Gradient** mode, where particles take their initial color from the defined **Gradient**. However, in this mode, the Particle System does not choose samples based on the age of the Particle System, but instead it selects them at random. This mode also works well with the **Fixed Gradient Mode** , which is inside the Gradient Editor. When enabled, you can select a predefined list of precise starting colors, and apply a probability to each color.

Other color properties, such as **Color over Lifetime** , can use the
**Gradient** or **Random Between Two Gradients** modes.

To calculate the final particle color result, the Particle System multiplies
color properties in various modules together per channel.

When you set the **Gradient** color for particles, the Gradient Editor
appears:

![](../uploads/Main/PartSysGradientEditor.png)

  * **Mode:** Determines whether the particle color settings are blended or not.
  * **Color:** Displays the color of the currently selected key in the Gradient. Use this to edit the color at that position of the Gradient.
  * **Location:** Shows how far along on the Gradient the currently selected key is.
  * **Presets:** Allows you to save Gradient settings. Click New to make the current set of values a Gradient preset.

Color properties in various modules are multiplied together per channel to
calculate the final particle color result.

[](PartSysUsage.html)

Create and view a Particle System

[](configuring-particles.html)

Configuring particles

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

