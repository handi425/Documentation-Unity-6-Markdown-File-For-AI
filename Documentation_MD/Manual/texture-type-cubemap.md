[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/texture-type-cubemap.html)
  * [中文](/cn/current/Manual/texture-type-cubemap.html)
  * [日本語](/ja/current/Manual/texture-type-cubemap.html)
  * [한국어](/kr/current/Manual/texture-type-cubemap.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/texture-type-cubemap.html)
  * [中文](/cn/current/Manual/texture-type-cubemap.html)
  * [日本語](/ja/current/Manual/texture-type-cubemap.html)
  * [한국어](/kr/current/Manual/texture-type-cubemap.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Textures reference](textures-reference.html)
  * Cubemap texture Import Settings window reference

[](texture-type-sprite.html)

Sprite (2D and UI) texture Import Settings window reference

[](class-Texture3D-reference.html)

3D texture preview reference

# Cubemap texture Import Settings window reference

You can further refine **Cubemap** A collection of six square textures that
can represent the reflections in an environment or the skybox drawn behind
your geometry. The six squares form the faces of an imaginary cube that
surrounds an object; each face represents the view along the directions of the
world axes (up, down, left, right, forward and back). [More info](class-
Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap) shape textures with the following
properties:

**Property:** | **Function:**  
---|---  
**Mapping** | Use **Mapping** to specify how the Texture is projected onto your **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject). This is set to **Auto** by
default.  
| **Auto** | Unity tries to create the layout from the Texture information.  
| **6 Frames Layout (Cubic Environment)** | The Texture contains six images arranged in one of the standard cubemap layouts: cross, or sequence (+x -x +y -y +z -z). The images can be orientated either horizontally or vertically.  
| **Latitude Longitude (Cylindrical)** | Maps the Texture to a 2D Latitude-Longitude representation.  
| **Mirrored Ball (Sphere Mapped)** | Maps the Texture to a sphere-like cubemap.  
**Convolution Type** | Choose the type of pre-convolution (filtering) that you want to use for this Texture. The result of pre-convolution is stored in mipmaps.   
This property is only available for the [Default](texture-type-default.html)
Texture type.  
| **None** | The Texture has no pre-convolution (no filtering). This is the default.  
| **Specular (Glossy Reflection)** | Select this to use cubemaps as **Reflection Probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe). The Texture mipmaps are pre-
convoluted (filtered) with the engine BRDF. For more information, see
Wikipedia’s page on [Bidirectional reflectance distribution
function](https://en.wikipedia.org/wiki/Bidirectional_reflectance_distribution_function).  
| **Diffuse (Irradiance)** | The Texture is convoluted (filtered) to represent irradiance. This is useful if you use the cubemap as a **Light Probe** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe).  
**Fixup Edge Seams** | This option is only available with the **None** or **Diffuse** convolution (filter). Use this on low-end platforms as a work-around for filtering limitations, such as cubemaps incorrectly filtered between faces.  
  
## Additional resources

  * [Cubemaps](class-Cubemap-landing.html)

[](texture-type-sprite.html)

Sprite (2D and UI) texture Import Settings window reference

[](class-Texture3D-reference.html)

3D texture preview reference

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

