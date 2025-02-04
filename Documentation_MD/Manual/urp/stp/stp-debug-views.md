[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/stp/stp-debug-views.html)
  * [中文](/cn/current/Manual/urp/stp/stp-debug-views.html)
  * [日本語](/ja/current/Manual/urp/stp/stp-debug-views.html)
  * [한국어](/kr/current/Manual/urp/stp/stp-debug-views.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/stp/stp-debug-views.html)
  * [中文](/cn/current/Manual/urp/stp/stp-debug-views.html)
  * [日本語](/ja/current/Manual/urp/stp/stp-debug-views.html)
  * [한국어](/kr/current/Manual/urp/stp/stp-debug-views.html)

  * [Working in Unity](../../working-in-unity.html)
  * [Cameras](../../Cameras.html)
  * [Cameras in URP](../../urp/urp-cameras-landing.html)
  * [Upscaling resolution in URP with Spatial-Temporal Post-Processing](../../urp/change-resolution-scale-urp.html)
  * Spatial-Temporal Post-processing Rendering Debugger reference for URP

[](../../urp/stp/stp-enable.html)

Enable Spatial-Temporal Post-processing in URP

[](../../urp/universal-additional-camera-data.html)

Access camera data with the Universal Additional Camera Data component in URP

# Spatial-Temporal Post-processing Rendering Debugger reference for URP

There are six debug views for Spatial-Temporal Post-processing (STP). To
access them, open the Rendering Debugger window and navigate to **Rendering**
> **Map Overlays** and select **STP**. Unity shows the **STP Debug Views**
property where you can select one of the views.

For more information on how to access the Rendering Debugger window, refer to
[How to access the Rendering Debugger](../features/rendering-debugger.html).

## Debug views

**Debug view** | **Description**  
---|---  
**Clipped Input Color** | Show the **HDR** high dynamic range  
See in [Glossary](../../Glossary.html#HDR) input color clipped between 0 and
1.  
**Log Input Depth** | Show the input depth in logarithmic scale.  
**Reversible Tonemapped Input Color** | Show the input color mapped to a 0–1 range with a reversible tonemapper.  
**Shaped Absolute Input Motion** | Visualize the input motion vectors.  
**Motion Reprojection** | Visualize the reprojected color difference across several frames.  
**Sensitivity** | Visualize the pixel sensitivities. Green areas show where STP can’t predict motion behavior. These areas are likely to render with reduced visual quality. STP struggles to predict motion in areas when occluded objects first become visible or when there is fast movement. Incorrect object motion vectors can also cause issues with motion prediction.  
  
Red areas highlight pixels that are excluded from TAA, so STP intentionally
does not predict their motion. This helps avoid unnecessary blurring and
ghosting, especially when rendering transparent objects.  
  
[](../../urp/stp/stp-enable.html)

Enable Spatial-Temporal Post-processing in URP

[](../../urp/universal-additional-camera-data.html)

Access camera data with the Universal Additional Camera Data component in URP

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

