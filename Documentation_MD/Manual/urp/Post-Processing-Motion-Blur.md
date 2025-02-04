[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/Post-Processing-Motion-Blur.html)
  * [中文](/cn/current/Manual/urp/Post-Processing-Motion-Blur.html)
  * [日本語](/ja/current/Manual/urp/Post-Processing-Motion-Blur.html)
  * [한국어](/kr/current/Manual/urp/Post-Processing-Motion-Blur.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/Post-Processing-Motion-Blur.html)
  * [中文](/cn/current/Manual/urp/Post-Processing-Motion-Blur.html)
  * [日本語](/ja/current/Manual/urp/Post-Processing-Motion-Blur.html)
  * [한국어](/kr/current/Manual/urp/Post-Processing-Motion-Blur.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](../post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](../urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](../urp/post-processing-in-urp.html)
  * [Post-processing Volume Overrides reference for URP](../urp/EffectList.html)
  * Motion Blur Volume Override reference for URP

[](../urp/Post-Processing-Lift-Gamma-Gain.html)

Lift Gamma Gain Volume Override reference for URP

[](../urp/Post-Processing-Panini-Projection.html)

Panini Projection Volume Override reference for URP

# Motion Blur Volume Override reference for URP

![Scene with Motion Blur effect turned off.](../../uploads/urp/post-
proc/motion-blur-off.png) Scene with Motion Blur effect turned off. ![Scene
with Motion Blur effect turned on.](../../uploads/urp/post-proc/motion-
blur.png) Scene with Motion Blur effect turned on.

The Motion Blur effect simulates the blur that occurs in an image when a real-
world **camera** A component which creates an image of a particular viewpoint
in your scene. The output is either drawn to the screen or captured as a
texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) films objects moving faster than
the camera’s exposure time. This is usually due to rapidly moving objects, or
a long exposure time.

Universal **Render Pipeline** A series of operations that take the contents of
a Scene, and displays them on a screen. Unity lets you choose from pre-built
render pipelines, or write your own. [More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) only blurs camera
motions.

## Properties

**Property** | **Description**  
---|---  
**Mode** | Select the motion blur technique.  
Options:

  * **Camera Only** : use only the motion of the camera to blur the objects. This technique does not use the motion vectors. This technique has better performance than **Camera and Objects**.
  * **Camera and Objects** : use the motion of both the camera and the GameObjects. GameObject motion vectors overwrite the camera motion vectors.

  
**Quality** | Set the quality of the effect. Lower presets give better performance, but at a lower visual quality and a higher risk of visual artifacts.  
**Intensity** | Set the strength of the motion blur filter to a value from 0 to 1. Higher values give a stronger blur effect, but can cause lower performance, depending on the **Clamp** parameter.  
**Clamp** | Set the maximum length that the velocity resulting from Camera rotation can have. This limits the blur at high velocity, to avoid excessive performance costs. The value is measured as a fraction of the screen’s full resolution. The value range is 0 to 0.2. A lower value uses less resources and results in better performance.  
  
The default value is 0.05.  
  
[](../urp/Post-Processing-Lift-Gamma-Gain.html)

Lift Gamma Gain Volume Override reference for URP

[](../urp/Post-Processing-Panini-Projection.html)

Panini Projection Volume Override reference for URP

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

