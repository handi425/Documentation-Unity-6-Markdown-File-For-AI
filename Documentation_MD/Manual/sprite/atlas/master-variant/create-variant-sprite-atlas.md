[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/atlas/master-variant/create-variant-sprite-atlas.html)
  * [中文](/cn/current/Manual/sprite/atlas/master-variant/create-variant-sprite-atlas.html)
  * [日本語](/ja/current/Manual/sprite/atlas/master-variant/create-variant-sprite-atlas.html)
  * [한국어](/kr/current/Manual/sprite/atlas/master-variant/create-variant-sprite-atlas.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/atlas/master-variant/create-variant-sprite-atlas.html)
  * [中文](/cn/current/Manual/sprite/atlas/master-variant/create-variant-sprite-atlas.html)
  * [日本語](/ja/current/Manual/sprite/atlas/master-variant/create-variant-sprite-atlas.html)
  * [한국어](/kr/current/Manual/sprite/atlas/master-variant/create-variant-sprite-atlas.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Sprites](../../../sprite/sprite-landing.html)
  * [Sprite atlas](../../../sprite/atlas/atlas-landing.html)
  * [Variant Sprite Atlases](../../../sprite/atlas/master-variant/master-variant-landing.html)
  * Create a variant Sprite Atlas

[](../../../sprite/atlas/master-variant/variant-sprite-atlas.html)

Variant Sprite Atlas

[](../../../sprite/atlas/master-variant/scale-textures-variant-sprite-
atlas.html)

Scale the textures of a variant Sprite Atlas

# Create a variant Sprite Atlas

To create a Variant **Sprite** A 2D graphic objects. If you are used to
working in 3D, Sprites are essentially just standard textures but there are
special techniques for combining and managing sprite textures for efficiency
and convenience during development. [More info](../../../sprite/sprite-
landing.html)  
See in [Glossary](../../../Glossary.html#Sprite) Atlas:

  1. Prepare the **Sprite Atlas** A utility that packs several sprite textures tightly together within a single texture known as an atlas. [More info](../../../sprite/atlas/v2/v2-landing.html)  
See in [Glossary](../../../Glossary.html#SpriteAtlas) that will be the Variant
Atlas’ Master Atlas. It contains the Texture Assets that the Variant Atlas
will derive its own content from.

  2. [Create a new Sprite Atlas](../workflow/create-sprite-atlas-asset.html), and set its **Type** to ‘Variant’.

  3. Assign the Sprite Atlas prepared in Step 1 to this property to set it as the Variant’s Master.

As a Variant Atlas without a Master Atlas contains no content on its own,
Unity will not pack it into a `.spriteatlas` Asset.

In a Project that includes both a Master and a Variant Sprite Atlas, if both
are **Included in the Build** , then the Textured used by mutual sprites can
come from either Sprite Atlas (refer to Scenario 3 of the [Resolving different
Sprite Atlas scenarios](../distribution/resolve-different-sprite-atlas-
scenarios.html) page).

To automatically load Sprite Textures from the Variant Atlas instead of the
Master Atlas, enable **Include in Build** for the Variant Atlas only and
disable it for the Master Atlas. The build then automatically loads the
Variant Sprite Atlas instead of the Master Atlas at runtime.

[](../../../sprite/atlas/master-variant/variant-sprite-atlas.html)

Variant Sprite Atlas

[](../../../sprite/atlas/master-variant/scale-textures-variant-sprite-
atlas.html)

Scale the textures of a variant Sprite Atlas

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

