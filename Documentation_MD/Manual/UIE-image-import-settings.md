[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-image-import-settings.html)
  * [中文](/cn/current/Manual/UIE-image-import-settings.html)
  * [日本語](/ja/current/Manual/UIE-image-import-settings.html)
  * [한국어](/kr/current/Manual/UIE-image-import-settings.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-image-import-settings.html)
  * [中文](/cn/current/Manual/UIE-image-import-settings.html)
  * [日本語](/ja/current/Manual/UIE-image-import-settings.html)
  * [한국어](/kr/current/Manual/UIE-image-import-settings.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Style UI](UIE-USS.html)
  * [USS properties](UIE-uss-properties.html)
  * Image import settings

[](UIB-styling-ui-backgrounds.html)

Set background images

[](UIE-Transform.html)

USS transform

# Image import settings

After you have imported an image to your project, for the most intuitive
results, it’s recommended that you apply certain import settings for Textures,
**Sprites** A 2D graphic objects. If you are used to working in 3D, Sprites
are essentially just standard textures but there are special techniques for
combining and managing sprite textures for efficiency and convenience during
development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite), and Vector images before you use them
as a background for a **visual element** A node of a visual tree that
instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) in the **UI**(User Interface)
Allows a user to interact with your application. Unity currently supports
three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Builder.

## Texture

The recommended import settings for a **Texture** image that you use as a
background for a visual element:

**Property:** | **Value:**  
---|---  
**Texture Type** | **Default**  
| **Non-Power of 2** | None  
| ****Compression** A method of storing data that reduces the amount of
storage space it requires. See [Texture Compression](class-
TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression)** | None  
| **Alpha Is Transparency** | true  
**Texture Type** | **Editor GUI and Legacy GUI**  
| **Non-Power of 2** | None  
| **Compression** | None  
| **Alpha Is Transparency** | true  
**Texture Type** | **Sprite (2D and UI)**  
| **Compression** | None  
| **Alpha Is Transparency** | true  
| **Sprite Mode** | Single  
| ****Mesh** The main graphics primitive of Unity. Meshes make up a large part
of your 3D worlds. Unity supports triangulated or Quadrangulated polygon
meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Type** | Tight  
  
## Sprites

The recommended import settings for a **Sprite** image that you use as a
background for a visual element:

**Property:** | **Value:**  
---|---  
**Texture Type** | **Sprite (2D and UI)**  
| **Compression** | None  
| **Alpha Is Transparency** | true  
| **Sprite Mode** | Multiple if file contains multiple sprites, Single otherwise  
| **Mesh Type** | Tight  
  
## Vector images

The recommended import settings for a SVG **Vector** image that you use as a
background for a visual element:

**Property:** | **Value:**  
---|---  
**Generated Asset Type** | UI Toolkit Vector Image  
**Tessellation Settings** | Basic  
**Target Resolution** | Lowest value that produces satisfactory results  
  
**Tip** :

  * You can [apply default presets to Assets by folder](DefaultPresetsByFolder.html) to automatically set your desired import settings.
  * All image types are subject to [dynamic atlasing](../ScriptReference/UIElements.DynamicAtlasSettings.html) if they’re not already in an atlas. (An image is in an atlas if imported as a Sprite with **Sprite Mode** set to **Multiple** , or if you have manually added it to a [Sprite Atlas](sprite/atlas/atlas-landing.html)A utility that packs several sprite textures tightly together within a single texture known as an atlas. [More info](sprite/atlas/v2/v2-landing.html)  
See in [Glossary](Glossary.html#SpriteAtlas) asset.) You can configure dynamic
atlasing in a [Panel Settings](UIE-Runtime-Panel-Settings.html) asset.

## Additional resources

  * [UIE-uxml-element-Image](UIE-uxml-element-Image.html)

[](UIB-styling-ui-backgrounds.html)

Set background images

[](UIE-Transform.html)

USS transform

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

