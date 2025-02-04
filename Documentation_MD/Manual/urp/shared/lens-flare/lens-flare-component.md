[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/shared/lens-flare/lens-flare-component.html)
  * [中文](/cn/current/Manual/urp/shared/lens-flare/lens-flare-component.html)
  * [日本語](/ja/current/Manual/urp/shared/lens-flare/lens-flare-component.html)
  * [한국어](/kr/current/Manual/urp/shared/lens-flare/lens-flare-component.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/shared/lens-flare/lens-flare-component.html)
  * [中文](/cn/current/Manual/urp/shared/lens-flare/lens-flare-component.html)
  * [日本語](/ja/current/Manual/urp/shared/lens-flare/lens-flare-component.html)
  * [한국어](/kr/current/Manual/urp/shared/lens-flare/lens-flare-component.html)

  * [Visual effects](../../../visual-effects.html)
  * [Lens flares](../../../visual-effects-lens-flares.html)
  * [Lens flares in URP](../../../urp/shared/lens-flare/lens-flare.html)
  * Add lens flares in URP

[](../../../urp/shared/lens-flare/choose-a-lens-flare-type.html)

Choose a lens flare type in URP

[](../../../urp/shared/lens-flare/post-processing-screen-space-lens-
flare.html)

Add screen space lens flares in URP

# Add lens flares in URP

![Lens flares in a scene.](../../../../uploads/urp/shared/lens-flare/lens-
flare-header.png) Lens flares in a scene.

Unity’s Scriptable **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](../../../render-
pipelines.html)  
See in [Glossary](../../../Glossary.html#Renderpipeline) (SRP) includes the
Lens Flare (SRP) component which renders a lens flare in your **scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](../../../CreatingScenes.html)  
See in [Glossary](../../../Glossary.html#Scene). This is the SRP equivalent of
the Built-in Render Pipeline’s [Lens
Flare](https://docs.unity3d.com/Manual/class-LensFlare.html)A component that
simulates the effect of lights refracting inside a camera lens. Use a Lens
Flare to represent very bright lights or add atmosphere to your scene. [More
info](../../../class-LensFlare.html)  
See in [Glossary](../../../Glossary.html#LensFlare) component, which is
incompatible with SRPs. You can attach a Lens Flare (SRP) component to any
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More
info](../../../class-GameObject.html)  
See in [Glossary](../../../Glossary.html#GameObject), but some properties only
appear when you attach a Lens Flare (SRP) component to a light.

## Creating lens flares in SRP

The Lens Flare (SRP) component controls where the lens flare is as well as
properties such as attenuation and whether the lens flare considers occlusion.
For properties that define how the lens flare looks, SRP uses the [Lens Flare
(SRP) Data](lens-flare-asset.html) asset. Each Lens Flare (SRP) component must
reference a Lens Flare (SRP) data asset to display a lens flare on-screen.

To create a lens flare in a scene:

  1. Create or select a GameObject to attach the lens flare too.
  2. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../../../UsingTheInspector.html)  
See in [Glossary](../../../Glossary.html#Inspector), click **Add Component**.

  3. Select **Rendering** > **Lens Flare (SRP)**. Currently, the lens flare doesn’t render in the scene because the component doesn’t reference a Lens Flare (SRP) Data asset in its **Lens Flare Data** property.
  4. Create a new Lens Flare (SRP) Data asset (menu: **Assets** > **Create** > **Lens Flare (SRP)**).
  5. In the Lens Flare (SRP) component Inspector, assign the new Lens Flare (SRP) Data asset to the **Lens Flare Data** property.
  6. Select the Lens Flare (SRP) Data asset and, in the Inspector, add a new element to the **Elements** list. A default white lens flare now renders at the position of the Lens Flare (SRP) component. For information on how to customize how the lens flare looks, refer to [Lens Flare (SRP) Data](lens-flare-asset.html).

Refer to the following for more information:

  * [Lens Flare (SRP) reference](lens-flare-srp-reference.html)
  * [Lens Flare (SRP) Data Asset reference](lens-flare-asset.html)

[](../../../urp/shared/lens-flare/choose-a-lens-flare-type.html)

Choose a lens flare type in URP

[](../../../urp/shared/lens-flare/post-processing-screen-space-lens-
flare.html)

Add screen space lens flares in URP

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

