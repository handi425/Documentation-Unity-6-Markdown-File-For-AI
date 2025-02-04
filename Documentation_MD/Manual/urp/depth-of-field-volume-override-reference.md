[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/depth-of-field-volume-override-reference.html)
  * [中文](/cn/current/Manual/urp/depth-of-field-volume-override-reference.html)
  * [日本語](/ja/current/Manual/urp/depth-of-field-volume-override-reference.html)
  * [한국어](/kr/current/Manual/urp/depth-of-field-volume-override-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/depth-of-field-volume-override-reference.html)
  * [中文](/cn/current/Manual/urp/depth-of-field-volume-override-reference.html)
  * [日本語](/ja/current/Manual/urp/depth-of-field-volume-override-reference.html)
  * [한국어](/kr/current/Manual/urp/depth-of-field-volume-override-reference.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](../post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](../urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](../urp/post-processing-in-urp.html)
  * [Post-processing Volume Overrides reference for URP](../urp/EffectList.html)
  * [Depth of Field in URP](../urp/depth-of-field-urp.html)
  * Depth of Field Volume Override reference for URP

[](../urp/depth-of-field-volume-override.html)

Depth of Field Volume Override in URP

[](../urp/Post-Processing-Film-Grain.html)

Film Grain Volume Override reference for URP

# Depth of Field Volume Override reference for URP

The **Depth of Field** A post-processing effect that simulates the focus
properties of a camera lens. [More info](../PostProcessingOverview.html)  
See in [Glossary](../Glossary.html#DepthofField) Volume Override has multiple
propeties that can alter the way Depth of Field appears. These properties vary
depending on which Depth of Field mode is selected.

## Properties

**Property** | **Description**  
---|---  
**Mode** | Select the mode that URP uses to set the focus for the depth of field effect:

  * **Off** : Select this option to disable depth of field.
  * **Gaussian** : Select this option to use the faster but more limited depth of field mode.
  * **Bokeh** : Select this option to use the Bokeh-based depth of field mode.

  
  
### Gaussian Depth of Field

**Property** | **Description**  
---|---  
**Start** | Set the distance from the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) at which the far field starts
blurring.  
**End** | Set the distance from the Camera at which the far field blur reaches its maximum blur radius.  
**Max Radius** | Set the maximum radius the far blur can reach. The default value is 1.   
**Note** : Values above 1 can cause visual under-sampling artifacts to appear
in your scene. If your blur effects are not smooth or appear to have static
noise in them, try decreasing the value back to 1 or lower.  
**High Quality Sampling** | Use higher quality sampling to reduce flickering and improve the overall blur smoothness. This can cause some performance cost.  
  
### Bokeh Depth of Field

The **Bokeh** Depth of Field mode closely imitates the effect of a real-life
camera. For this reason, the settings are based on real-life camera settings,
and offer a number of properties to adjust the diaphragm blades on the Camera.
For an introduction to diaphragm blades and how they affect the visual quality
of your Camera output, refer to Improve Photography’s guide [Aperture Blades:
How many is best?](https://improvephotography.com/29529/aperture-blades-many-
best/).

**Property** | **Description**  
---|---  
**Focus Distance** | Set the distance from the Camera to the focus point.  
**Focal Length** | Set the distance, in millimeters, between the Camera sensor and the Camera lens. The larger the value is, the shallower the depth of field.  
**Aperture** | Set the ratio of aperture (known as f-stop or f-number). The smaller the value is, the shallower the depth of field is.  
**Blade Count** | Use the slider to set the number of diaphragm blades the Camera uses to form the aperture. The more blades you use, the rounder the bokeh appears.  
**Blade Curvature** | Use the slider to set the curvature of diaphragm blades the Camera uses to form the aperture. The smaller the value is, the more visible aperture blades are. A value of 1 makes the bokeh perfectly circular.*  
**Blade Rotation** | Use the slider to set the rotation of diaphragm blades in degrees.  
  
[](../urp/depth-of-field-volume-override.html)

Depth of Field Volume Override in URP

[](../urp/Post-Processing-Film-Grain.html)

Film Grain Volume Override reference for URP

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

