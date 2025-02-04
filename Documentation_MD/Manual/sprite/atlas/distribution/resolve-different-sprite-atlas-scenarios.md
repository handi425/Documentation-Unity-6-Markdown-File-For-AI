[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/atlas/distribution/resolve-different-sprite-atlas-scenarios.html)
  * [中文](/cn/current/Manual/sprite/atlas/distribution/resolve-different-sprite-atlas-scenarios.html)
  * [日本語](/ja/current/Manual/sprite/atlas/distribution/resolve-different-sprite-atlas-scenarios.html)
  * [한국어](/kr/current/Manual/sprite/atlas/distribution/resolve-different-sprite-atlas-scenarios.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/atlas/distribution/resolve-different-sprite-atlas-scenarios.html)
  * [中文](/cn/current/Manual/sprite/atlas/distribution/resolve-different-sprite-atlas-scenarios.html)
  * [日本語](/ja/current/Manual/sprite/atlas/distribution/resolve-different-sprite-atlas-scenarios.html)
  * [한국어](/kr/current/Manual/sprite/atlas/distribution/resolve-different-sprite-atlas-scenarios.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Sprites](../../../sprite/sprite-landing.html)
  * [Sprite atlas](../../../sprite/atlas/atlas-landing.html)
  * [Distribution](../../../sprite/atlas/distribution/distribution-landing.html)
  * Resolve different Sprite Atlas scenarios

[](../../../sprite/atlas/distribution/retrieve-sprite-contents-runtime-
getsprites.html)

Retrieve sprite contents at runtime with GetSprites

[](../../../sprite/atlas/packer-mode/packer-mode-landing.html)

Sprite packer modes

# Resolve different Sprite Atlas scenarios

The way Unity resolves the interaction between Sprites and **Sprite** A 2D
graphic objects. If you are used to working in 3D, Sprites are essentially
just standard textures but there are special techniques for combining and
managing sprite textures for efficiency and convenience during development.
[More info](../../../sprite/sprite-landing.html)  
See in [Glossary](../../../Glossary.html#Sprite) Atlases depends on various
conditions. The examples below detail the most common scenarios:

## Scenario 1: Basic Sprite Atlas usage

  1. ****Sprite Atlas** A utility that packs several sprite textures tightly together within a single texture known as an atlas. [More info](../../../sprite/atlas/v2/v2-landing.html)  
See in [Glossary](../../../Glossary.html#SpriteAtlas) A** contains **Sprite
1**.

  2. **Sprite Atlas A** has **Include in Build** enabled.
  3. Result: The Project’s published build includes **Sprite Atlas A**. **Sprite 1** renders with the Texture from **Sprite Atlas A**.

## Scenario 2: ‘Include in Build’ is disabled

  1. **Sprite Atlas A** contains **Sprite 1**.
  2. **Sprite Atlas A** has **Include in Build** disabled.
  3. Result: The Project’s published build does not include **Sprite Atlas A** , and does not include **Sprite 1’s** Texture. **Sprite 1** appears invisible in the build at run time, because the Texture it refers to is not available and is not loaded.

## Scenario 3: One Sprite in two Sprite Atlases

  1. **Sprite Atlas A** and **Sprite Atlas B** both include **Sprite 1** in their [Objects for Packing](../workflow/select-items-objects-packing-list.html) lists.
  2. Both **Sprite Atlas A** and **Sprite Atlas B** have **Include in Build** enabled.
  3. Both **Sprite Atlases** have different Texture output settings in this example.
  4. Result: The Project’s published build includes both Sprite Atlases. Unity randomly chooses which Texture to render **Sprite 1** with, in an internal process that is out of your control.

In this scenario, to ensure that the Sprite renders with the Texture from the
Sprite Atlas you want, follow the steps below:

  1. Disable **‘Include in Build’** for both Sprite Atlases.
  2. When you initialize the Sprite at run time, request the Sprite directly from one of the Atlases with [SpriteAtlas.GetSprite](../../../../ScriptReference/U2D.SpriteAtlas.GetSprite.html). This ensures that Unity always draws the Sprite Texture from the correct Sprite Atlas.

[](../../../sprite/atlas/distribution/retrieve-sprite-contents-runtime-
getsprites.html)

Retrieve sprite contents at runtime with GetSprites

[](../../../sprite/atlas/packer-mode/packer-mode-landing.html)

Sprite packer modes

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

