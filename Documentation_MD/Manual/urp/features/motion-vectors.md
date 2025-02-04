[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/features/motion-vectors.html)
  * [中文](/cn/current/Manual/urp/features/motion-vectors.html)
  * [日本語](/ja/current/Manual/urp/features/motion-vectors.html)
  * [한국어](/kr/current/Manual/urp/features/motion-vectors.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/features/motion-vectors.html)
  * [中文](/cn/current/Manual/urp/features/motion-vectors.html)
  * [日本語](/ja/current/Manual/urp/features/motion-vectors.html)
  * [한국어](/kr/current/Manual/urp/features/motion-vectors.html)

  * [Working in Unity](../../working-in-unity.html)
  * [Cameras](../../Cameras.html)
  * [Cameras in URP](../../urp/urp-cameras-landing.html)
  * [Motion vectors in URP](../../urp/features/motion-vectors-landing.html)
  * Introduction to motion vectors in URP

[](../../urp/features/motion-vectors-landing.html)

Motion vectors in URP

[](../../urp/features/motion-vectors-shader-support.html)

Built-in shader support for motion vectors in URP

# Introduction to motion vectors in URP

URP calculates the frame-to-frame screen-space movement of surface fragments
using a [motion vector render pass](motion-vectors-sample.html). URP stores
the movement data in a full-screen texture and the stored per-pixel values are
called motion vectors.

Unity runs the motion vector render pass only when there are active features
in the frame with render passes that request it. For example, the following
URP features request the motion vector pass: [temporal anti-aliasing](../anti-
aliasing.html#taa) and [motion blur](../Post-Processing-Motion-Blur.html). For
information on how to request the motion vector pass in a custom passes, refer
to section [Using the motion vector texture in your passes](motion-vectors-
sample.html).

Incorrect or missing motion vectors can result in [visual artifacts](motion-
vectors-troubleshooting.html) in effects that rely on them. Follow the
instructions on this page to ensure that your object renderers, Materials, and
**shaders** A program that runs on the GPU. [More info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader) are set up correctly to support
motion vectors.

URP supports motion vectors only for opaque materials, including alpha-clipped
materials. URP does not support motion vectors for transparent materials.

## Implementation details

This section describes how URP implements motion vectors.

###  Motion vector definition

A motion vector is a 2D vector representing a surface fragment’s motion
relative to the **camera** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera) since the last frame, projected
onto the camera’s near **clipping plane** A plane that limits how far or close
a camera can see from its current position. A camera’s viewable range is
between the far and near clipping planes. See far clipping plane and near
clipping plane. [More info](../../class-Camera.html)  
See in [Glossary](../../Glossary.html#clippingplane). The motion vector
texture uses 2 channels (R and G). Each texel stores the UV offset of each
visible surface fragment. If you subtract the motion vector for a given texel
from its current UV coordinate, you will get the UV coordinate of where this
texel would have been on the screen last frame. The computed last frame UV
coordinate can be outside the screen bounds.

### Object motion vectors and camera-only motion vectors

There are two categories of motion vectors:

  * **Camera motion vectors** : motion vectors caused only by the camera’s own motion.

  * **Object motion vectors** : motion vectors caused by a combination of the camera’s motion and the world-space motion of the object the fragment belongs to.

Given only the motion vector texture it’s impossible to infer whether a
fragment’s motion on screen is due to only camera motion, object motion or a
combination of both.

A single full-screen pass is enough to calculate camera motion vectors. Such
pass has a fixed per-frame computation load independent of **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene) complexity. It’s only necessary
to know the current 3D positions of all **pixels** The smallest unit in a
computer image. Pixel size depends on your screen resolution. Pixel lighting
is calculated at every screen pixel. [More info](../../ShadowPerformance.html)  
See in [Glossary](../../Glossary.html#pixel) on screen and how the camera
moved, which can be inferred from the **depth buffer** A memory store that
holds the z-value depth of each pixel in an image, where the z-value is the
depth for each rendered pixel from the projection plane. [More
info](../../class-RenderTexture.html)  
See in [Glossary](../../Glossary.html#depthbuffer) and the camera matrices for
the current and the previous frames.

Object motion vectors have computation load which depends on the number and
complexity of the moving objects in the scene because a draw per-object is
required to account for each object’s motion. Each draw needs to apply the
camera’s motion contribution too.

###  Cases when Unity renders per-object motion vectors

Unity renders object motion vectors for a **mesh** The main graphics primitive
of Unity. Meshes make up a large part of your 3D worlds. Unity supports
triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces
must be converted to polygons. [More info](../../mesh.html)  
See in [Glossary](../../Glossary.html#Mesh) in a frame when the following
three conditions are met:

  1. The shader associated with the mesh has a [MotionVectors pass](motion-vectors-shader-support.html) in an active SubShader block.

  2. The mesh is being rendered through any of the following renderers:

    1. **SkinnedMeshRenderer**.

    2. **MeshRenderer** , when its **Motion Vectors** property is not set to `Camera Motion Only`.

    3. Using the following APIs: [Graphics.RenderMesh](https://docs.unity3d.com/ScriptReference/Graphics.RenderMesh.html), [Graphics.RenderMeshInstanced](https://docs.unity3d.com/ScriptReference/Graphics.RenderMeshInstanced.html) or [Graphics.RenderMeshIndirect](https://docs.unity3d.com/ScriptReference/Graphics.RenderMeshIndirect.html), with the `MotionVectorMode` member of the `RenderParams` struct not set to `Camera`.

  3. If any of the following conditions is true:

    1. The `MotionVectorGenerationMode` property is set to `ForceNoMotion` on the `MeshRenderer` or the `RenderParams.MotionVectorMode` struct member of the `Grphics.Render...` APIs.

**Note:** The `ForceNoMotion` option requires a per-object motion vector pass
to be rendered every frame so that the camera motion vectors for such objects
can be overwritten with zeros.

    2. The **MotionVectors** pass [is enabled on the material](https://docs.unity3d.com/ScriptReference/Material.SetPass.html) (for example, when a material has a vertex animation in Shader Graph or alembic animation).

    3. The **MotionVectors** pass [is disabled on the material](https://docs.unity3d.com/ScriptReference/Material.SetPass.html) but the model matrices for the previous and the current frame don’t match, or if the object has skeletal animation. Stationary renderers without skeletal animation are not rendered with an object motion vector pass if their shader has a `MotionVectors` pass but it’s disabled on their material.

### MotionVectors pass in URP pre-built shaders

When the **MotionVectors** pass is enabled for the pre-built shaders, Unity
renders object motion vectors for **mesh renderers** A mesh component that
takes the geometry from the Mesh Filter and renders it at the position defined
by the object’s Transform component. [More info](../../class-
MeshRenderer.html)  
See in [Glossary](../../Glossary.html#MeshRenderer) even if they don’t move.

Unity enables the **MotionVectors** pass in the pre-built URP shaders when the
following conditions are true:

  * URP **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](../../SL-Shader.html)  
See in [Glossary](../../Glossary.html#ShaderLab) shaders: on a Material, the
**Alembic Motion Vectors** property is enabled in the **Advanced Options**
section.

  * URP Lit and Unlit Shader Graph shaders: in the **Graph**Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../../UsingTheInspector.html)  
See in [Glossary](../../Glossary.html#Inspector)**, any of the following
properties is set:

    * **Alembic Motion Vectors** is enabled.
    * **Additional Motion Vectors** property is set to **TimeBased** or **Custom**.

[](../../urp/features/motion-vectors-landing.html)

Motion vectors in URP

[](../../urp/features/motion-vectors-shader-support.html)

Built-in shader support for motion vectors in URP

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

