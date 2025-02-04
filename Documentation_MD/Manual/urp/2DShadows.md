[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/2DShadows.html)
  * [中文](/cn/current/Manual/urp/2DShadows.html)
  * [日本語](/ja/current/Manual/urp/2DShadows.html)
  * [한국어](/kr/current/Manual/urp/2DShadows.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/2DShadows.html)
  * [中文](/cn/current/Manual/urp/2DShadows.html)
  * [日本語](/ja/current/Manual/urp/2DShadows.html)
  * [한국어](/kr/current/Manual/urp/2DShadows.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [2D lighting in URP](../urp/2d-index.html)
  * Create shadows with Shadow Caster 2D in URP

[](../urp/HDREmulationScale.html)

HDR emulation scale

[](../urp/ShaderGraph.html)

Create a 2D sprite lit Shader Graph in URP

# Create shadows with Shadow Caster 2D in URP

Learn how the **Shadow Caster 2D** component defines the shape and properties
that a Light uses to determine its cast shadows.

Add the **Shadow Caster 2D** component to a GameObject by going to menu:
**Component > Rendering > 2D > Shadow Caster 2D**.

**Property** | **Function**  
---|---  
**Use Renderer Silhouette** | Enable this and **Self Shadows** to include the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject) Renderer’s silhouette as part
of the shadow. Enable this and disable Self Shadows to exclude the Renderer’s
silhouette from the shadow. This option is only available when a valid
Renderer is present.  
**Casts Shadows** | Enable this to have the Renderer cast shadows.  
**Self Shadows** | Enable this to have the Renderer cast shadows on itself.  
![](../../uploads/urp/2D/RendSilhou_disabled_SS_false.png) | ![](../../uploads/urp/2D/RendSilhou_enabled_SS_false.png)  
---|---  
**Use Renderer Silhouette** disabled, **Self Shadow** disabled |  **Use Renderer Silhouette** enabled, **Self Shadow** disabled  
![](../../uploads/urp/2D/RendSilhou_disabled_SS_true_.png) | ![](../../uploads/urp/2D/RendSilhou_enabled_SS_true.png)  
**Use Renderer Silhouette** disabled, **Self Shadows** enabled |  **Use Renderer Silhouette** enabled, **Self Shadows** enabled  
  
## Composite Shadow Caster 2D

The **Composite Shadow Caster 2D** merges the shape of multiple **Shadow
Caster 2Ds** together as a single **Shadow Caster 2D**. Add the **Composite
Shadow Caster 2D** component to a GameObject by going to menu: **Component >
Rendering > 2D > Composite Shadow Caster 2D**, then parent GameObjects with
the **Shadow Caster 2D** component to it. The Composite component merges all
Shadow Caster 2Ds within this hierarchy, including any Shadow Caster 2Ds on
the parent as well.

![](../../uploads/urp/2D/wo_composite_shadow.png) | ![](../../uploads/urp/2D/w_composite_shadow.png)  
---|---  
Without **Composite Shadow Caster 2D** | With **Composite Shadow Caster 2D**  
  
[](../urp/HDREmulationScale.html)

HDR emulation scale

[](../urp/ShaderGraph.html)

Create a 2D sprite lit Shader Graph in URP

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

