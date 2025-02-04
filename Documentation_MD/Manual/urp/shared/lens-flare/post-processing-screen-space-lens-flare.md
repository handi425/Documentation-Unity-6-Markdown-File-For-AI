[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/shared/lens-flare/post-processing-screen-space-lens-flare.html)
  * [中文](/cn/current/Manual/urp/shared/lens-flare/post-processing-screen-space-lens-flare.html)
  * [日本語](/ja/current/Manual/urp/shared/lens-flare/post-processing-screen-space-lens-flare.html)
  * [한국어](/kr/current/Manual/urp/shared/lens-flare/post-processing-screen-space-lens-flare.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/shared/lens-flare/post-processing-screen-space-lens-flare.html)
  * [中文](/cn/current/Manual/urp/shared/lens-flare/post-processing-screen-space-lens-flare.html)
  * [日本語](/ja/current/Manual/urp/shared/lens-flare/post-processing-screen-space-lens-flare.html)
  * [한국어](/kr/current/Manual/urp/shared/lens-flare/post-processing-screen-space-lens-flare.html)

  * [Visual effects](../../../visual-effects.html)
  * [Lens flares](../../../visual-effects-lens-flares.html)
  * [Lens flares in URP](../../../urp/shared/lens-flare/lens-flare.html)
  * Add screen space lens flares in URP

[](../../../urp/shared/lens-flare/lens-flare-component.html)

Add lens flares in URP

[](../../../urp/shared/lens-flare/lens-flare-srp-reference.html)

Lens Flare (SRP) component reference for URP

# Add screen space lens flares in URP

![A scene with screen space lens flares turned
on.](../../../../uploads/urp/shared/lens-flare/screenspacelensflaresurp.png) A
scene with screen space lens flares turned on.

The **Screen Space**Lens Flare** A component that simulates the effect of
lights refracting inside a camera lens. Use a Lens Flare to represent very
bright lights or add atmosphere to your scene. [More info](../../../class-
LensFlare.html)  
See in [Glossary](../../../Glossary.html#LensFlare)** override adds lens
flares to your **scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](../../../CreatingScenes.html)  
See in [Glossary](../../../Glossary.html#Scene).

To calculate lens flares, the Universal **Render Pipeline** A series of
operations that take the contents of a Scene, and displays them on a screen.
Unity lets you choose from pre-built render pipelines, or write your own.
[More info](../../../render-pipelines.html)  
See in [Glossary](../../../Glossary.html#Renderpipeline) (URP) fetches bright
areas of the current image, such as emissive lights and bright specular
reflections. URP then draws the same areas back to the screen in different
locations and using different effects such as stretch, blur, and chromatic
aberration.

The **Screen Space Lens Flare** creates lens flares from the following:

  * Emissive surfaces.
  * Bright spots in your scene that appear depending on the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../../../CamerasOverview.html)  
See in [Glossary](../../../Glossary.html#Camera) view, for example a bright
specular reflection on a shiny metal object, or a bright outside area viewed
from a dark indoor area.

  * All onscreen lights.

You can use the [Lens Flare (SRP)](lens-flare-component.html) component
instead to create a flare for a light that has a specific position in the
scene. You can also use both the **Lens Flare (SRP)** component and the
**Screen Space Lens Flare** override in the same scene.

## How screen space lens flares work

The bright areas URP uses to calculate screen space lens flares are the same
areas the [Bloom override](../../post-processing-bloom.html) brightens.

URP uses the same buffer as the Bloom override to fetch the bright areas and
render the lens flares. The settings in the Bloom override affect the
appearance of screen space lens flares.

**Note** : If you have a [Bloom override](../../post-processing-bloom.html) in
the volume, set **Intensity** in the Bloom override to a value higher than 0
or lens flares won’t appear.

You can create the following types of lens flare:

  * Regular flares, which are a brightened distorted version of the bright areas of the screen.
  * Reversed flares, which are regular flares flipped upside-down and reversed.
  * Warped flares, which are regular flares transformed using polar coordinates, to mimic a circular camera lens.
  * Streaks, which are flares stretched in one direction, to mimic an anamorphic camera lens.

You can control which types of flares appear and how many there are. You can
also control the chromatic aberration effect URP adds to the flares.

![The left image shows an emissive cube with bloom but no lens flares. The
right image shows the same cube and a regular flare \(top-left\), a reversed
flare \(bottom-right\), a warped flare \(top-right\) and streaks \(to the left
and right of the cube\).](../../../../uploads/urp/shared/lens-
flare/screenspacelensflares-types.png) The left image shows an emissive cube
with bloom but no lens flares. The right image shows the same cube and a
regular flare (top-left), a reversed flare (bottom-right), a warped flare
(top-right) and streaks (to the left and right of the cube).

**Note** : Some lens flares only appear, or only appear at full intensity, if
you enable High Dynamic Range (HDR) rendering on your camera. To enable
**HDR** high dynamic range  
See in [Glossary](../../../Glossary.html#HDR), refer to [the **Output**
section of the Camera component reference](../../camera-component-
reference.html#Output)

[](../../../urp/shared/lens-flare/lens-flare-component.html)

Add lens flares in URP

[](../../../urp/shared/lens-flare/lens-flare-srp-reference.html)

Lens Flare (SRP) component reference for URP

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

