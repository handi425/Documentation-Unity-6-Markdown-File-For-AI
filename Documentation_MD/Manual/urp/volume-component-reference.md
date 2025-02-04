[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/volume-component-reference.html)
  * [中文](/cn/current/Manual/urp/volume-component-reference.html)
  * [日本語](/ja/current/Manual/urp/volume-component-reference.html)
  * [한국어](/kr/current/Manual/urp/volume-component-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/volume-component-reference.html)
  * [中文](/cn/current/Manual/urp/volume-component-reference.html)
  * [日本語](/ja/current/Manual/urp/volume-component-reference.html)
  * [한국어](/kr/current/Manual/urp/volume-component-reference.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](../post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](../urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](../urp/post-processing-in-urp.html)
  * [Volumes in URP](../urp/volumes-landing-page.html)
  * Volume component reference for URP

[](../urp/VolumeOverrides.html)

Configure Volume Overrides in URP

[](../urp/EffectList.html)

Post-processing Volume Overrides reference for URP

# Volume component reference for URP

Volumes components contain properties that control how they affect **Cameras**
A component which creates an image of a particular viewpoint in your scene.
The output is either drawn to the screen or captured as a texture. [More
info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) and how they interact with other
Volumes.

Property | Description  
---|---  
**Mode** | Use the drop-down to select the method that URP uses to calculate whether this Volume can affect a Camera:  
• **Global** : Makes the Volume have no boundaries and allow it to affect
every Camera in the scene.  
• **Local** : Allows you to specify boundaries for the Volume so that the
Volume only affects Cameras inside the boundaries. Add a Collider to the
Volume’s GameObject and use that to set the boundaries.  
**Blend Distance** | The furthest distance from the Volume’s Collider that URP starts blending from. A value of 0 means URP applies this Volume’s overrides immediately upon entry.  
This property only appears when you select **Local** from the **Mode** drop-
down.  
**Weight** | The amount of influence the Volume has on the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene). URP applies this multiplier to the
value it calculates using the Camera position and Blend Distance.  
**Priority** | URP uses this value to determine which Volume it uses if more than one Volume overrides the same property. URP uses the Volume with the highest value.  
**Volume Profile** | A Volume Profile Asset that contains the Volume Components that store the properties URP uses to handle this Volume. The **Profile** field stores a [Volume Profile](Volume-Profile.html), which is an Asset that contains the properties that URP uses to render the scene. You can edit this Volume Profile, or assign a different Volume Profile to the **Profile** field. You can also create a Volume Profile by selecting the **New** button.  
  
[](../urp/VolumeOverrides.html)

Configure Volume Overrides in URP

[](../urp/EffectList.html)

Post-processing Volume Overrides reference for URP

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

