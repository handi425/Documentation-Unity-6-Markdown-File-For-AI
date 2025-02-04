[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/configuring-flare-elements.html)
  * [中文](/cn/current/Manual/configuring-flare-elements.html)
  * [日本語](/ja/current/Manual/configuring-flare-elements.html)
  * [한국어](/kr/current/Manual/configuring-flare-elements.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/configuring-flare-elements.html)
  * [中文](/cn/current/Manual/configuring-flare-elements.html)
  * [日本語](/ja/current/Manual/configuring-flare-elements.html)
  * [한국어](/kr/current/Manual/configuring-flare-elements.html)

  * [Visual effects](visual-effects.html)
  * [Lens flares](visual-effects-lens-flares.html)
  * [Lens flares in the Built-In Render Pipeline](lens-flare-birp.html)
  * Configuring Flare elements

[](create-lens-flare.html)

Create a lens flare

[](class-Flare.html)

Flare asset reference

# Configuring Flare elements

Learn how Unity manages elements on a Flare asset, and compare texture layout
options.

A Flare consists of multiple **Elements** , arranged along a line. The line is
calculated by comparing the position of the **GameObject** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) containing the Lens Flare to the
center of the screen. The line extends beyond the containing GameObject and
the screen center. All Flare **Elements** are strung out on this line.

For performance reasons, all **Elements** of one Flare must share the same
Texture. This Texture contains a collection of the different images that are
available as Elements in a single Flare. The **Texture Layout** defines how
the **Elements** are laid out in the **Flare Texture**. If you use many
different Flare assets, using a shared single **Flare Texture** that contains
all the **Elements** will give you best rendering performance.

Lens Flares are blocked by **Colliders** An invisible shape that is used to
handle physical collisions for an object. A collider doesn’t need to be
exactly the same shape as the object’s mesh - a rough approximation is often
more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider). A Collider in-between the Flare
GameObject and the **Camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) will hide the Flare, even if the
Collider does not have a **Mesh Renderer** A mesh component that takes the
geometry from the Mesh Filter and renders it at the position defined by the
object’s Transform component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer). If the in-between Collider is
marked as Trigger it will block the flare if and only if
**Physics.queriesHitTriggers** is true.

To override the **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) used for Flares, open the
[Graphics](class-GraphicsSettings.html) window and set **Lens Flares** A
component that simulates the effect of lights refracting inside a camera lens.
Use a Lens Flare to represent very bright lights or add atmosphere to your
scene. [More info](class-LensFlare.html)  
See in [Glossary](Glossary.html#LensFlare) to the shader that you would like
to use as the override.

## Understand texture layouts

These are the options you have for different Flare **Texture Layouts**. The
numbers in the images correspond to the **Image Index** property for each
**Element**.

### 1 Large 4 Small

![](../uploads/Main/FlaresLayout0.png)

Designed for large sun-style Flares where you need one of the **Elements** to
have a higher fidelity than the others. This is designed to be used with
Textures that are twice as high as they are wide.

### 1 Large 2 Medium 8 Small

![](../uploads/Main/FlaresLayout1.png)

Designed for complex flares that require 1 high-definition, 2 medium and 8
small images. This is used in the standard assets “50mm Zoom Flare” where the
two medium Elements are the rainbow-colored circles. This is designed to be
used with textures that are twice as high as they are wide.

### 1 Texture

![](../uploads/Main/FlaresLayout2.png)

A single image.

## 2x2 grid

![](../uploads/Main/FlaresLayout3.png)

A simple 2x2 grid.

### 3x3 grid

![](../uploads/Main/FlaresLayout4.png)

A simple 3x3 grid.

### 4x4 grid

![](../uploads/Main/FlaresLayout5.png)

A simple 4x4 grid.

Flare

[](create-lens-flare.html)

Create a lens flare

[](class-Flare.html)

Flare asset reference

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

