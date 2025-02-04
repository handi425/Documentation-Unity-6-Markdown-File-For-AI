[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ObliqueFrustum.html)
  * [中文](/cn/current/Manual/ObliqueFrustum.html)
  * [日本語](/ja/current/Manual/ObliqueFrustum.html)
  * [한국어](/kr/current/Manual/ObliqueFrustum.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ObliqueFrustum.html)
  * [中文](/cn/current/Manual/ObliqueFrustum.html)
  * [日本語](/ja/current/Manual/ObliqueFrustum.html)
  * [한국어](/kr/current/Manual/ObliqueFrustum.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [The camera view](CameraView.html)
  * Make the camera perspective oblique

[](UnderstandingFrustum.html)

Introduction to the camera view

[](FrustumSizeAtDistance.html)

Calculate the size of the frustum at a distance

# Make the camera perspective oblique

By default, the view frustum is arranged symmetrically around the **camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera)’s center line, but it doesn’t
necessarily need to be. You can make the frustum oblique, which means that one
side is at a smaller angle to the centre line than the opposite side.

This makes the perspective on one side of the image seem more condensed,
giving the impression that the viewer is very close to the object visible at
that edge. An example of how this can be used is a car racing game; if the
frustum is flattened at its bottom edge, it appears to the viewer that they
are closer to the road, accentuating the feeling of speed.

![](../uploads/Main/ObliqueFrustum.png)

## Setting frustum obliqueness

Although the Camera component does not have functions specifically for setting
the obliqueness of the frustum, you can do it by either enabling the camera’s
[Physical Camera](PhysicalCameras.html) properties and applying a Lens Shift,
or by adding a script to alter the camera’s projection matrix.

**Note:** In the Built-in **Render Pipeline** A series of operations that take
the contents of a Scene, and displays them on a screen. Unity lets you choose
from pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), a Camera that uses an oblique
frustum can only use the Forward [rendering path](RenderingPaths.html)The
technique that a render pipeline uses to render graphics. Choosing a different
rendering path affects how lighting and shading are calculated. Some rendering
paths are more suited to different platforms and hardware than others. [More
info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath). If your Camera is set to use
the **Deferred Shading** A rendering path in the Built-in Render Pipeline that
places no limit on the number of Lights that can affect a GameObject. All
Lights are evaluated per-pixel, which means that they all interact correctly
with normal maps and so on. Additionally, all Lights can have cookies and
shadows. [More info](RenderTech-DeferredShading.html)  
See in [Glossary](Glossary.html#Deferredshading) rendering path and you make
its frustum oblique, Unity forces that Camera to use the **Forward rendering**
A rendering path that renders each object in one or more passes, depending on
lights that affect the object. Lights themselves are also treated differently
by Forward Rendering, depending on their settings and intensity. [More
info](RenderTech-ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering) path.

### Setting frustum obliqueness with Lens Shift

Enable a camera’s **Physical Camera** properties to expose the **Lens Shift**
options. You can use these to offset the camera’s focal center along the X and
Y axes in a way that minimizes distortion of the rendered image.

Shifting the lens reduces the frustum angle on the side opposite the direction
of the shift. For example, as you shift the lens up, the angle between the
bottom of the frustum and the camera’s center line gets smaller.

![Normally a camera’s frustum is symmetrical \(left\), meaning the angles on
either side of the center line are equal. Shifting the lens \(right\) makes
the frustum oblique, meaning the angle is smaller on one side than on the
other. ](../uploads/Main/ObliqueFrustum_LensShift.png) Normally a camera’s
frustum is symmetrical (left), meaning the angles on either side of the center
line are equal. Shifting the lens (right) makes the frustum oblique, meaning
the angle is smaller on one side than on the other.

For further information about the Physical Camera options, see documentation
on [Physical Cameras](PhysicalCameras.html).

### Setting frustum obliqueness using a script

The following script example shows how to quickly achieve an oblique frustum
by altering the camera’s projection matrix. Note that you can only see the
effect of the script while the game is running Play mode.

    
    
    using UnityEngine;
    using System.Collections;
    
    public class ExampleScript : MonoBehaviour {
        void SetObliqueness(float horizObl, float vertObl) {
            Matrix4x4 mat  = Camera.main.projectionMatrix;
            mat[0, 2] = horizObl;
            mat[1, 2] = vertObl;
            Camera.main.projectionMatrix = mat;
        }
    }
    

_C# script example_

It is not necessary to understand how the projection matrix works to make use
of this. The horizObl and vertObl values set the amount of horizontal and
vertical obliqueness, respectively. A value of zero indicates no obliqueness.
A positive value shifts the frustum rightwards or upwards, thereby flattening
the left or bottom side. A negative value shifts leftwards or downwards and
consequently flattens the right or top side of the frustum. The effect can be
seen directly if this script is added to a camera and the game is switched to
the **scene** A Scene contains the environments and menus of your game. Think
of each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view while the game runs; the wireframe
depiction of the camera’s frustum will change as you vary the values of
horizObl and vertObl in the **inspector** A Unity window that displays
information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector). A value of 1 or –1 in either
variable indicates that one side of the frustum is completely flat against the
centreline. It is possible although seldom necessary to use values outside
this range.

## Additional resources

  * [Camera Inspector windows reference for URP](urp/camera-components-reference-landing.html)
  * [Camera Inspector window reference for the Built-In Render Pipeline](class-Camera.html)

[](UnderstandingFrustum.html)

Introduction to the camera view

[](FrustumSizeAtDistance.html)

Calculate the size of the frustum at a distance

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

