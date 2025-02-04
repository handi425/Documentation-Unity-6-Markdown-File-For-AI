[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/atlas/master-variant/master-variant-sprite-atlases.html)
  * [中文](/cn/current/Manual/sprite/atlas/master-variant/master-variant-sprite-atlases.html)
  * [日本語](/ja/current/Manual/sprite/atlas/master-variant/master-variant-sprite-atlases.html)
  * [한국어](/kr/current/Manual/sprite/atlas/master-variant/master-variant-sprite-atlases.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/atlas/master-variant/master-variant-sprite-atlases.html)
  * [中文](/cn/current/Manual/sprite/atlas/master-variant/master-variant-sprite-atlases.html)
  * [日本語](/ja/current/Manual/sprite/atlas/master-variant/master-variant-sprite-atlases.html)
  * [한국어](/kr/current/Manual/sprite/atlas/master-variant/master-variant-sprite-atlases.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Sprites](../../../sprite/sprite-landing.html)
  * [Sprite atlas](../../../sprite/atlas/atlas-landing.html)
  * [Variant Sprite Atlases](../../../sprite/atlas/master-variant/master-variant-landing.html)
  * Master and Variant Sprite Atlases

[](../../../sprite/atlas/master-variant/master-variant-landing.html)

Variant Sprite Atlases

[](../../../sprite/atlas/master-variant/variant-sprite-atlas.html)

Variant Sprite Atlas

# Master and Variant Sprite Atlases

The **Type** property defines whether a **Sprite** A 2D graphic objects. If
you are used to working in 3D, Sprites are essentially just standard textures
but there are special techniques for combining and managing sprite textures
for efficiency and convenience during development. [More
info](../../../sprite/sprite-landing.html)  
See in [Glossary](../../../Glossary.html#Sprite) Atlas is a ‘**Master** ’ or a
‘**Variant** ’. Sprite Atlases are created as Master types by default. Set
their Type to ‘Variant’ to create a **Variant Atlas**.

A Variant Atlas requires a Master type **Sprite Atlas** A utility that packs
several sprite textures tightly together within a single texture known as an
atlas. [More info](../../../sprite/atlas/v2/v2-landing.html)  
See in [Glossary](../../../Glossary.html#SpriteAtlas) to be set in its
**Master Atlas** property. The Variant Atlas receives a copy of the Master
Atlas’s contents to use as its own. Refer to documentation on [Variant Sprite
Atlas](variant-sprite-atlas.html) for more details about how to create and use
Variant Sprite Atlases.

When the Sprite Atlas Type is set to ‘Variant’, the following properties
appear:

![](../../../../uploads/Main/2DSpriteAtlas_VariantProperties.png) Property | Description  
---|---  
**Type** | Set the Atlas’s Type to **Variant** to reveal the following properties.  
**Master Atlas** | A Variant Atlas receives a copy of its Master Atlas’ contents to use as its own. Assign a Sprite Atlas to this property to make it the **Master** Atlas of the currently selected **Variant** Atlas. The Master Atlas cannot be a Variant Atlas itself.  
**Include in Build** | Check this box to include the Sprite Atlas in the current build. This option is enabled by default.  
**Scale** | Set the scale factor of the Variant Sprite Atlas that can range from 0.1 to 1. The size of the Variant Atlas Texture is the result of the Master Atlas’ Texture multiplied by the **Scale** value. The default and maximum Scale value is 1, where the Variant Atlas Texture remains identical to its Master Atlas’ Texture.  
  
[](../../../sprite/atlas/master-variant/master-variant-landing.html)

Variant Sprite Atlases

[](../../../sprite/atlas/master-variant/variant-sprite-atlas.html)

Variant Sprite Atlas

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

