[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/depth-of-field-volume-override.html)
  * [中文](/cn/current/Manual/urp/depth-of-field-volume-override.html)
  * [日本語](/ja/current/Manual/urp/depth-of-field-volume-override.html)
  * [한국어](/kr/current/Manual/urp/depth-of-field-volume-override.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/depth-of-field-volume-override.html)
  * [中文](/cn/current/Manual/urp/depth-of-field-volume-override.html)
  * [日本語](/ja/current/Manual/urp/depth-of-field-volume-override.html)
  * [한국어](/kr/current/Manual/urp/depth-of-field-volume-override.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](../post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](../urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](../urp/post-processing-in-urp.html)
  * [Post-processing Volume Overrides reference for URP](../urp/EffectList.html)
  * [Depth of Field in URP](../urp/depth-of-field-urp.html)
  * Depth of Field Volume Override in URP

[](../urp/depth-of-field-urp.html)

Depth of Field in URP

[](../urp/depth-of-field-volume-override-reference.html)

Depth of Field Volume Override reference for URP

# Depth of Field Volume Override in URP

The **Depth Of Field** A post-processing effect that simulates the focus
properties of a camera lens. [More info](../PostProcessingOverview.html)  
See in [Glossary](../Glossary.html#DepthofField) component applies a depth of
field effect, which simulates the focus properties of a **camera** A component
which creates an image of a particular viewpoint in your scene. The output is
either drawn to the screen or captured as a texture. [More
info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) lens. In real life, a camera can
only focus sharply on an object at a specific distance. Objects nearer or
farther from the camera are out of focus. The blurring gives a visual cue
about an object’s distance, and introduces “bokeh”, which refers to visual
artifacts that appear around bright areas of the image as they fall out of
focus. To read more about bokeh, refer to the [Wikipedia article on
Bokeh](https://en.wikipedia.org/wiki/Bokeh).

The Universal **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](../render-
pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) has two depth of
field modes:

  * **Gaussian** : this mode approximates camera-like effects, but doesn’t imitate them completely. It has a limited blur radius and only does far-field blurring. This mode is the fastest, and is the best mode for lower-end platforms.  
![Gaussian Depth Of Field](../../uploads/urp/post-proc/dof-gaussian.png)

  * **Bokeh** : a slower but higher quality mode that closely imitates the effects of a real-life camera. It can do both near & far-field blurring, and generates bokeh on areas with high luminosity intensity, also known as hot spots.  
![Gaussian Depth Of Field](../../uploads/urp/post-proc/dof-bokeh.png)

[](../urp/depth-of-field-urp.html)

Depth of Field in URP

[](../urp/depth-of-field-volume-override-reference.html)

Depth of Field Volume Override reference for URP

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

