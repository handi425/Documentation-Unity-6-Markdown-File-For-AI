[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/probevolumes-showandadjust.html)
  * [中文](/cn/current/Manual/urp/probevolumes-showandadjust.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-showandadjust.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-showandadjust.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/probevolumes-showandadjust.html)
  * [中文](/cn/current/Manual/urp/probevolumes-showandadjust.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-showandadjust.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-showandadjust.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](../urp/probevolumes.html)
  * Display Adaptive Probe Volumes

[](../urp/probevolumes-use.html)

Use Adaptive Probe Volumes

[](../urp/probevolumes-changedensity.html)

Configure the size and density of Adaptive Probe Volumes

# Display Adaptive Probe Volumes

You can use the Rendering Debugger to check how URP places **Light Probes**
Light probes store information about how light passes through space in your
scene. A collection of light probes arranged within a given space can improve
lighting on moving objects and static LOD scenery within that space. [More
info](../LightProbes.html)  
See in [Glossary](../Glossary.html#LightProbe) in an Adaptive Probe Volume,
then use Adaptive Probe Volume settings to configure the layout.

## Display Adaptive Probe Volumes

To display Adaptive Probe Volumes, open the [Rendering
Debugger](features/rendering-debugger.html) and select the **Probe Volume**
tab.

You can do the following:

  * Enable **Probe Visualization** > **Display Probes** to display the locations of Light Probes and the lighting they store.
  * Enable **Subdivision Visualization** > **Display Bricks** to display the outlines of groups of Light Probes (‘bricks’). Refer to [Understanding Adaptive Probe Volumes](probevolumes-concept.html#how-probe-volumes-work) for more information on bricks.
  * Enable **Subdivision Visualization** > **Display Cells** to display the outlines of cells, which are groups of bricks used for [streaming](probevolumes-streaming.html).
  * Enable **Subdivision Visualization** > **Debug Probe Sampling** to display how neighboring Light Probes influence a chosen position. Select a surface to display the weights URP uses to sample nearby Light Probes.

If the Rendering Debugger displays invalid probes when you select **Display
Probes** , refer to [Fix issues with Adaptive Probe Volumes](probevolumes-
fixissues.html).

![The Rendering Debugger with Display Probes
enabled.](../../uploads/urp/probe-volumes/probevolumes-debug-
displayprobes.PNG)  

![The Rendering Debugger with Display Bricks
enabled.](../../uploads/urp/probe-volumes/probevolumes-debug-
displayprobebricks1.PNG)  

![The Rendering Debugger with Display Cells enabled.](../../uploads/urp/probe-
volumes/probevolumes-debug-displayprobecells.PNG)  

![The Rendering Debugger with Debug Probe Sampling
enabled](../../uploads/urp/probe-volumes/APVsamplingDebug.png)  

Refer to [Rendering Debugger](features/rendering-debugger.html) for more
information.

## Additional resources

  * [Configure the size and density of an Adaptive Probe Volume](probevolumes-changedensity.html)
  * [Adaptive Probe Volumes panel reference](probevolumes-lighting-panel-reference.html)
  * [Probe Volumes Options Override reference](probevolumes-options-override-reference.html)
  * [Probe Adjustment Volume component reference](probevolumes-adjustment-volume-component-reference.html)

[](../urp/probevolumes-use.html)

Use Adaptive Probe Volumes

[](../urp/probevolumes-changedensity.html)

Configure the size and density of Adaptive Probe Volumes

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

