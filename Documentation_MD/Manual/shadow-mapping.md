[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/shadow-mapping.html)
  * [中文](/cn/current/Manual/shadow-mapping.html)
  * [日本語](/ja/current/Manual/shadow-mapping.html)
  * [한국어](/kr/current/Manual/shadow-mapping.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/shadow-mapping.html)
  * [中文](/cn/current/Manual/shadow-mapping.html)
  * [日本語](/ja/current/Manual/shadow-mapping.html)
  * [한국어](/kr/current/Manual/shadow-mapping.html)

  * [Lighting](LightingOverview.html)
  * [Shadows](Shadows.html)
  * [Real-time shadows](shadow-realtime.html)
  * Shadow mapping

[](shadow-realtime.html)

Real-time shadows

[](shadow-distance.html)

Set shadow distance in a scene

# Shadow mapping

Unity performs shadow mapping to render real-time shadows.

## How shadow mapping works

Shadow mapping is the process of creating shadow textures called shadow maps.
Unity generates a shadow map from the perspective of a light in a similar way
to how a **camera** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) generates a depth texture. If you
consider a camera at the same location as the light, the areas of the
**scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) that the camera can’t see are the same
areas of the scene that rays from the light cannot reach. Those areas are in
shadow.

Unity populates the shadow map with information about how far rays from the
light travel before they hit a surface, and then samples the shadow map to
calculate real-time shadows for **GameObjects** The fundamental object in
Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that the light hits.

## Shadow map resolution

The larger the shadow map resolution, the better Unity can capture small
details in the shadow-casting geometry, and the more precise the shadows can
be. Larger shadow map resolution also requires more memory bandwidth.

For information on configuring the shadow map resolution, refer to the
following pages:

  * [Configure shadow resolution in URP](urp/shadow-resolution-urp.html)
  * [Configure shadow resolution in the Built-In Render Pipeline](shadow-resolution-birp.html)

##  Shadow mapping and performance

To create a shadow map for a point light, Unity captures the scene in six
directions. The performance impact is similar to rendering shadows from six
spot lights, and increases the number of draw calls significantly.

On mobile platforms, this process uses a significant amount of the available
resources per frame. Reduce the number of point lights within the camera view
as much as possible.

Real-time shadows from spot lights are significantly faster to render than
real-time shadows from point lights.

## Additional resources

  * [Configure shadow resolution in URP](urp/shadow-resolution-urp.html)
  * [Universal Render Pipeline Asset](urp/universalrp-asset.html)
  * [Configure shadow resolution in the Built-In Render Pipeline](shadow-resolution-birp.html)

[](shadow-realtime.html)

Real-time shadows

[](shadow-distance.html)

Set shadow distance in a scene

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

