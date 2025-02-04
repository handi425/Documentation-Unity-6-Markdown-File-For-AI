[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/probevolumes-adjustment-volume-component-reference.html)
  * [中文](/cn/current/Manual/urp/probevolumes-adjustment-volume-component-reference.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-adjustment-volume-component-reference.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-adjustment-volume-component-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/probevolumes-adjustment-volume-component-reference.html)
  * [中文](/cn/current/Manual/urp/probevolumes-adjustment-volume-component-reference.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-adjustment-volume-component-reference.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-adjustment-volume-component-reference.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](../urp/probevolumes.html)
  * Probe Adjustment Volume component reference

[](../urp/probevolumes-options-override-reference.html)

Probe Volumes Options Override reference

[](../urp/features/rendering-layers.html)

Rendering Layers in URP

# Probe Adjustment Volume component reference

Select a [Probe Adjustment Volume Component](probevolumes-troubleshoot-light-
leaks.html#probevolumeadjustment) and open the **Inspector** A Unity window
that displays information about the currently selected GameObject, asset or
project settings, allowing you to inspect and edit the values. [More
info](../UsingTheInspector.html)  
See in [Glossary](../Glossary.html#Inspector) to view its properties.

Refer to the following for more information about using the Probe Adjustment
Volume component:

  * [Fix issues with Adaptive Probe Volumes](probevolumes-fixissues.html)
  * [Configure the size and density of Adaptive Probe Volumes](probevolumes-changedensity.html)

**Property** | **Description**  
---|---  
**Influence Volume**  
**Shape** | Set the shape of the Adjustment Volume to either **Box** or **Sphere**.  
**Size** | Set the size of the Adjustment Volume. This property only appears if you set **Shape** to **Box**.   
**Radius** | Set the radius of the Adjustment Volume. This property only appears if you set **Shape** to **Sphere**.  
**Mode** |  Select how to override probes inside the Adjustment Volume.

  * **Invalidate Probes** Mark selected probes as invalid. Refer to [How light probe validity works](probevolumes-fixissues#how-light-probe-validity-works) for more information.
  * **Override Validity Threshold** Override the threshold URP uses to determine whether Light Probes are marked as invalid. Refer to [Adjust Dilation](probevolumes-fixissues#adjust-dilation) for more information.
  * **Apply Virtual Offset** Change the position Light Probes use when sampling the lighting in the scene during baking. Refer to [Adjust Virtual Offset](probevolumes-fixissues#adjust-virtual-offset) for more information.
  * **Override Virtual Offset Settings** Override the biases URP uses during baking to determine when Light Probes use Virtual Offset, and calculate sampling positions. Refer to [Adjust Virtual Offset](probevolumes-fixissues#adjust-virtual-offset) for more information
  * **Intensity Scale** Override the intensity of probes to brighten or darken affected areas.
  * **Override Sky Direction** Override the directions Unity uses to sample the ambient probe, if you enable [sky occlusion](probevolumes-skyocclusion).
  * **Override Sample Count:** Override the number of samples Unity uses for Adaptive Probe Volumes.
  

  
  
### Mode settings

**Property** | **Description**  
---|---  
**Dilation Validity Threshold** |  Override the ratio of backfaces a probe samples before URP considers it invalid. This option only appears if you set **Mode** to **Override Validity Threshold** , and you enable **Additional Properties**.  
**Virtual Offset Rotation** |  Set the rotation angle for the Virtual Offset vector on all probes in the Adjustment Volume. This option only appears if you set **Mode** to **Apply Virtual Offset**.  
**Virtual Offset Distance** |  Set how far URP pushes probes along the Virtual Offset Rotation vector. This option only appears if you set **Mode** to **Apply Virtual Offset**.  
**Geometry Bias** |  Sets how far URP pushes a probe’s capture point out of geometry after one of its sampling rays hits geometry. This option only appears if you set **Mode** to **Override Virtual Offset Settings**.  
**Ray Origin Bias** |  Override the distance between a probe’s center and the point URP uses to determine the origin of that probe’s sampling ray. This can be used to push rays beyond nearby geometry if the geometry causes issues. This option appears only if you set **Mode** to **Override Virtual Offset Settings**.   
  
**Intensity Scale** |  Change the brightness of all probes covered by the Probe Volumes Adjustment Volume component. Use this sparingly, because changing the intensity of probe data can lead to inconsistencies in the lighting. This option only appears if you set **Mode** to **Intensity Scale**.  
**Sky Direction** |  Set the direction Unity uses to sample the ambient probe. This option only appears if you set **Mode** to **Override Sky Direction**.  
**Probes**  
**Direct Sample Count** | Set the number of samples Unity uses to calculate the direct light each probe stores. This option only appears if you set **Mode** to **Override Sample Count**.  
**Indirect Sample Count** | Set the number of samples Unity uses to calculate the indirect light each probe stores, including environment samples. This option only appears if you set **Mode** to **Override Sample Count**.  
**Sample Count Multiplier** | Set the value Unity multiplies **Direct Sample Count** and **Indirect Sample Count** by. This option only appears if you set **Mode** to **Override Sample Count**.  
**Max Bounces** | Set the number of times Unity bounces light off objects. This option only appears if you set **Mode** to **Override Sample Count**.  
**Sky Occlusion**  
  
**Sample Count** | Set the number of samples Unity uses to calculate the amount of light each probe receives from the sky, if you enable [sky occlusion](probevolumes-skyocclusion). This option only appears if you set **Mode** to **Override Sample Count**.  
**Max Bounces** | Set the number of times Unity bounces light from the sky off objects to calculate the sky occlusion data, if you enable [sky occlusion](probevolumes-skyocclusion). This option only appears if you set **Mode** to **Override Sample Count**.  
  

[](../urp/probevolumes-options-override-reference.html)

Probe Volumes Options Override reference

[](../urp/features/rendering-layers.html)

Rendering Layers in URP

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

