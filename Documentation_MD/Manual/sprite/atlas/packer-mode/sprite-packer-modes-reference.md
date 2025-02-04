[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/atlas/packer-mode/sprite-packer-modes-reference.html)
  * [中文](/cn/current/Manual/sprite/atlas/packer-mode/sprite-packer-modes-reference.html)
  * [日本語](/ja/current/Manual/sprite/atlas/packer-mode/sprite-packer-modes-reference.html)
  * [한국어](/kr/current/Manual/sprite/atlas/packer-mode/sprite-packer-modes-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/atlas/packer-mode/sprite-packer-modes-reference.html)
  * [中文](/cn/current/Manual/sprite/atlas/packer-mode/sprite-packer-modes-reference.html)
  * [日本語](/ja/current/Manual/sprite/atlas/packer-mode/sprite-packer-modes-reference.html)
  * [한국어](/kr/current/Manual/sprite/atlas/packer-mode/sprite-packer-modes-reference.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Sprites](../../../sprite/sprite-landing.html)
  * [Sprite atlas](../../../sprite/atlas/atlas-landing.html)
  * [Sprite packer modes](../../../sprite/atlas/packer-mode/packer-mode-landing.html)
  * Sprite packer modes reference

[](../../../sprite/atlas/packer-mode/enable-disable-sprite-atlas-default-
packing-behavior.html)

Enable or disable the Sprite Atlas default packing behavior

[](../../../sprite/atlas/v2/v2-landing.html)

Sprite Atlas V2

# Sprite packer modes reference

Mode | Function  
---|---  
**Disabled** | Select this mode to disable **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](../../../sprite/sprite-landing.html)  
See in [Glossary](../../../Glossary.html#Sprite) Atlas packing in the current
Project. Sprite Atlases are not built when the Project enters Play mode or
when publishing a build. **Pack Preview** is also disabled.  
****Sprite Atlas** A utility that packs several sprite textures tightly
together within a single texture known as an atlas. [More
info](../../../sprite/atlas/v2/v2-landing.html)  
See in [Glossary](../../../Glossary.html#SpriteAtlas) V1 - Enabled For Builds** | Select this mode to have Unity pack Sprites into the Sprite Atlas when publishing builds only. The Editor and Play mode reference the original source Texture instead of the Texture within the Sprite Atlas.  
**Sprite Atlas V1 - Always Enabled** | This option is enabled by default. Select this mode to have Unity pack selected Textures into the Sprite Atlas, and Sprites reference the packed Textures during runtime. However, Sprites will reference the original unpacked Textures during Edit mode.  
**Sprite Atlas V2 - Enabled** | Select this mode to have Unity pack Sprites into the Sprite Atlas immediately when there are any changes. The packed Sprite Atlas is available when the project enters Play mode or when publishing a build.  
**Sprite Atlas V2 - Enabled For Builds** | Select this mode to have Unity pack Sprites into the Sprite Atlas only when publishing a build. The Editor and Play mode will reference the original unpacked Textures.  
  
[](../../../sprite/atlas/packer-mode/enable-disable-sprite-atlas-default-
packing-behavior.html)

Enable or disable the Sprite Atlas default packing behavior

[](../../../sprite/atlas/v2/v2-landing.html)

Sprite Atlas V2

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

