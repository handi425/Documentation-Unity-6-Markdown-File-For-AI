[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnderstandingFrustum.html)
  * [中文](/cn/current/Manual/UnderstandingFrustum.html)
  * [日本語](/ja/current/Manual/UnderstandingFrustum.html)
  * [한국어](/kr/current/Manual/UnderstandingFrustum.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnderstandingFrustum.html)
  * [中文](/cn/current/Manual/UnderstandingFrustum.html)
  * [日本語](/ja/current/Manual/UnderstandingFrustum.html)
  * [한국어](/kr/current/Manual/UnderstandingFrustum.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [The camera view](CameraView.html)
  * Introduction to the camera view

[](CameraView.html)

The camera view

[](ObliqueFrustum.html)

Make the camera perspective oblique

# Introduction to the camera view

What a **camera** A component which creates an image of a particular viewpoint
in your scene. The output is either drawn to the screen or captured as a
texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) sees is defined by its transform and
its Camera component. The transform position defines the viewpoint, its
forward (Z) axis defines the view direction, and its and upward (Y) axis
defines the top of the screen. Settings on the Camera component define the
size and shape of the region that falls within the view. With these parameters
set up, the camera can display what it currently “sees” to the screen. As the
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) moves and rotates, the displayed
view moves and rotates accordingly.

## The shape of the viewed region

Both perspective and orthographic cameras have a limit on how far they can
“see” from their current position. The limit is defined by a plane that is
perpendicular to the camera’s forward (Z) direction. This is known as the _far
clipping plane_ since objects at a greater distance from the camera are
“clipped” (ie, excluded from rendering). There is also a corresponding _near
clipping plane_ close to the camera - the viewable range of distance is that
between the two planes.

Without perspective, objects appear the same size regardless of their
distance. This means that the viewing volume of an orthographic camera is
defined by a rectangular box extending between the two **clipping planes** A
plane that limits how far or close a camera can see from its current position.
A camera’s viewable range is between the far and near clipping planes. See far
clipping plane and near clipping plane. [More info](class-Camera.html)  
See in [Glossary](Glossary.html#clippingplane).

When perspective is used, objects appear to diminish in size as the distance
from camera increases. This means that the width and height of the viewable
part of the **scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) grows with increasing distance. The
viewing volume of a perspective camera, then, is not a box but a pyramidal
shape with the apex at the camera’s position and the base at the **far
clipping plane** The maximum draw distance for a camera. Geometry beyond the
plane defined by this value is not rendered. The plane is perpendicular to the
camera’s forward (Z) direction.  
See in [Glossary](Glossary.html#Farclippingplane). The shape is not exactly a
pyramid, however, because the top is cut off by the **near clipping plane** A
plane that limits how close a camera can see from its current position. The
plane is perpendicular to the camera’s forward (Z) direction. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Nearclippingplane); this kind of truncated
pyramid shape is known as a _frustum_. Since its height is not constant, the
frustum is defined by the ratio of its width to its height (known as the
_aspect ratio_) and the angle between the top and bottom at the apex (known as
the _field of view_ or _FOV_). See the page about [understanding the view
frustum](UnderstandingFrustum.html) for a more detailed explanation.

## The view frustum

The word **frustum** refers to a solid shape that looks like a pyramid with
the top cut off parallel to the base. This is the shape of the region that can
be seen and rendered by a perspective camera. The following thought experiment
should help to explain why this is the case.

Imagine holding a straight rod (a broom handle or a pencil, for example) end-
on to a camera and then taking a picture. If the rod were held in the centre
of the picture, perpendicular to the camera lens, then only its end would be
visible as a circle on the picture; all other parts of it would be obscured.
If you moved it upward, the lower side would start to become visible but you
could hide it again by angling the rod upward. If you continued moving the rod
up and angling it further upward, the circular end would eventually reach the
top edge of the picture. At this point, any object above the line traced by
the rod in world space would not be visible on the picture.

![](../uploads/Main/Rods.png)

The rod could just as easily be moved and rotated left, right, or down or any
combination of horizontal and vertical. The angle of the “hidden” rod simply
depends on its distance from the centre of the screen in both axes.

The meaning of this thought experiment is that any point in a camera’s image
actually corresponds to a line in world space and only a single point along
that line is visible in the image. Everything behind that position on the line
is obscured.

The outer edges of the image are defined by the diverging lines that
correspond to the corners of the image. If those lines were traced backwards
towards the camera, they would all eventually converge at a single point. In
Unity, this point is located exactly at the camera’s transform position and is
known as the centre of perspective. The angle subtended by the lines
converging from the top and bottom centres of the screen at the centre of
perspective is called the field of view (often abbreviated to FOV).

As stated above, anything that falls outside the diverging lines at the edges
of the image will not be visible to the camera, but there are also two other
restrictions on what it will render. The near and far clipping planes are
parallel to the camera’s XY plane and each set at a certain distance along its
centre line. Anything closer to the camera than the near clipping plane and
anything farther away than the far clipping plane will not be rendered.

![](../uploads/Main/ViewFrustum.png)

The diverging corner lines of the image along with the two clipping planes
define a truncated pyramid - the view frustum.

[](CameraView.html)

The camera view

[](ObliqueFrustum.html)

Make the camera perspective oblique

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

