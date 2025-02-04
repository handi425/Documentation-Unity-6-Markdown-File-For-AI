[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/atlas/distribution/prepare-sprite-atlases-distribution.html)
  * [中文](/cn/current/Manual/sprite/atlas/distribution/prepare-sprite-atlases-distribution.html)
  * [日本語](/ja/current/Manual/sprite/atlas/distribution/prepare-sprite-atlases-distribution.html)
  * [한국어](/kr/current/Manual/sprite/atlas/distribution/prepare-sprite-atlases-distribution.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/atlas/distribution/prepare-sprite-atlases-distribution.html)
  * [中文](/cn/current/Manual/sprite/atlas/distribution/prepare-sprite-atlases-distribution.html)
  * [日本語](/ja/current/Manual/sprite/atlas/distribution/prepare-sprite-atlases-distribution.html)
  * [한국어](/kr/current/Manual/sprite/atlas/distribution/prepare-sprite-atlases-distribution.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Sprites](../../../sprite/sprite-landing.html)
  * [Sprite atlas](../../../sprite/atlas/atlas-landing.html)
  * [Distribution](../../../sprite/atlas/distribution/distribution-landing.html)
  * Prepare Sprite Atlases for distribution

[](../../../sprite/atlas/distribution/distribution-landing.html)

Distribution

[](../../../sprite/atlas/distribution/methods-distribution.html)

Methods of distribution

# Prepare Sprite Atlases for distribution

Ensure that the source Texture of the **Sprite** A 2D graphic objects. If you
are used to working in 3D, Sprites are essentially just standard textures but
there are special techniques for combining and managing sprite textures for
efficiency and convenience during development. [More
info](../../../sprite/sprite-landing.html)  
See in [Glossary](../../../Glossary.html#Sprite) is always uncompressed. While
packing **Sprite Atlas** A utility that packs several sprite textures tightly
together within a single texture known as an atlas. [More
info](../../../sprite/atlas/v2/v2-landing.html)  
See in [Glossary](../../../Glossary.html#SpriteAtlas), **pixel** The smallest
unit in a computer image. Pixel size depends on your screen resolution. Pixel
lighting is calculated at every screen pixel. [More
info](../../../ShadowPerformance.html)  
See in [Glossary](../../../Glossary.html#pixel) data is read from the source
texture and if it uses any compressed format, it may result in loss of
precision as it must be uncompressed first before packing. If a Sprite is
packed to a Sprite Atlas, only the Sprite Atlas Texture needs to be
compressed.

A Project can have multiple Sprite Atlases for different purposes (for
example, [Variant Atlases](../master-variant/variant-sprite-atlas.html) with
[lower-resolution](../master-variant/scale-textures-variant-sprite-atlas.html)
Textures for hardware with different limitations). If you enable all available
Sprite Atlases, you might encounter conflicts (refer to [Resolving different
Sprite Atlas scenarios](../distribution/resolve-different-sprite-atlas-
scenarios.html) for more information).

To prevent these issues, properly prepare Sprite Atlases for distribution with
the following steps:

  1. Disable ‘Include in Build’ in the Sprite Atlas properties.
  2. Choose a [method](methods-distribution.html) to distribute the Atlas.
  3. Load the Atlas via [Late Binding](late-binding.html) with a script.

## Disable ‘Include in Build’

Unity includes Sprite Atlases in a Project’s build by default, and
automatically loads them at run time. Clear the **Include in Build** setting
of the selected Sprite Atlas to disable this behavior.

If ‘Include in Build’ is disabled, Unity still packs the Sprite Atlas into a
*.spriteatlas file in the Project’s Assets folder. However, sprites which
reference Textures in a disabled Sprite Atlas appear invisible as the
reference Texture is not available or loaded. Unity does not include the
disabled Sprite Atlas in the Project’s published build, and does not
automatically load it at run time. To do so, a
[script](../../../../ScriptReference/U2D.SpriteAtlas.html) is required to load
the Sprite Atlas via [Late Binding](late-binding.html).

[](../../../sprite/atlas/distribution/distribution-landing.html)

Distribution

[](../../../sprite/atlas/distribution/methods-distribution.html)

Methods of distribution

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

