[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/SecondaryTextures.html)
  * [中文](/cn/current/Manual/urp/SecondaryTextures.html)
  * [日本語](/ja/current/Manual/urp/SecondaryTextures.html)
  * [한국어](/kr/current/Manual/urp/SecondaryTextures.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/SecondaryTextures.html)
  * [中文](/cn/current/Manual/urp/SecondaryTextures.html)
  * [日本語](/ja/current/Manual/urp/SecondaryTextures.html)
  * [한국어](/kr/current/Manual/urp/SecondaryTextures.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [2D lighting in URP](../urp/2d-index.html)
  * [Blend Modes in 2D lighting](../urp/2d-light-blending.html)
  * Add normal map and mask textures to a sprite in URP

[](../urp/2d-light-masking.html)

Masking

[](../urp/HDREmulationScale.html)

HDR emulation scale

# Add normal map and mask textures to a sprite in URP

Assign **normal map** A type of Bump Map texture that allows you to add
surface detail such as bumps, grooves, and scratches to a model which catch
the light as if they are represented by real geometry.  
See in [Glossary](../Glossary.html#Normalmap) and mask textures to **sprites**
A 2D graphic objects. If you are used to working in 3D, Sprites are
essentially just standard textures but there are special techniques for
combining and managing sprite textures for efficiency and convenience during
development. [More info](../sprite/sprite-landing.html)  
See in [Glossary](../Glossary.html#Sprite) by using the [Sprite
Editor](https://docs.unity3d.com/Manual/SpriteEditor.html)’s [Secondary
Textures](https://docs.unity3d.com/Manual/SpriteEditor-SecondaryTextures.html)
module to create advanced lighting effects with 2D lights.

First select a Sprite, and open the [Sprite
Editor](https://docs.unity3d.com/Manual/SpriteEditor.html) from its
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](../UsingTheInspector.html)  
See in [Glossary](../Glossary.html#Inspector) window. Then select the
**Secondary Textures** module from the drop-down menu at the top left of the
editor window.

![](../../uploads/urp/2D/ST_ModuleSelect.png)

## Adding a Secondary Texture

In the Secondary Textures editor, select a Sprite to add Secondary Textures
to. With a Sprite selected, the **Secondary Textures** panel appears at the
bottom right of the editor window. The panel displays the list of Secondary
Textures currently assigned to the selected Sprite. To add a new Secondary
Texture to the Sprite, select + at the bottom right of the list.

![](../../uploads/urp/2D/ST_ListField.png)

This adds a new entry to the list with the ‘Name’ and ‘Texture’ boxes. Enter a
custom name into the Name box, or select the arrow to the right of the Name
box to open the drop-down list of suggested names. These suggested names can
include suggestions from installed Unity packages, as the Secondary Textures
may need to have specific names to interact correctly with the **Shaders** A
program that runs on the GPU. [More info](../Shaders.html)  
See in [Glossary](../Glossary.html#Shader) in these packages to produce their
effects.

The 2D Lights package suggests the names ‘MaskTex’ and ‘NormalMap’. Select the
name that matches the function of the selected Texture - select ‘MaskTex’ for
a masking Texture, or ‘NormalMap’ for a normal map Texture. Naming these
Textures correctly allow them to interact with the 2D Lights Shaders to
properly produce the various lighting effects.

![](../../uploads/urp/2D/ST_Names.png)

To select the Texture Asset for this Secondary Texture entry, drag the Texture
Asset directly onto the Texture field, or open the **Object Picker** window by
selecting the circle to the right of the Texture box.

![](../../uploads/urp/2D/ST_ObjectDrag.png)

Secondary Textures are sampled with the same UV coordinates as the Texture of
the selected Sprite. Align the Secondary Textures with the main Sprite Texture
to ensure that additional Texture effects are displayed correctly.

![](../../uploads/urp/2D/ST_Align.png)

To preview the Secondary Texture in the **Sprite Editor** window, select an
entry in the list. This automatically hides the Sprite’s main Texture. Click
outside of the Secondary Textures list to deselect the entry, and the main
Sprite Texture becomes visible again.

![](../../uploads/urp/2D/ST_Preview.png)

## Deleting a Secondary Texture

To delete a Secondary Texture, select it from the list and then select - at
the bottom right of the window. This automatically removes the entry.

![](../../uploads/urp/2D/ST_Delete.png)

## Applying

Select **Apply** at the top of the editor to save your entries. Invalid
entries without a Name or an assigned Texture are automatically removed when
changes are applied.

![](../../uploads/urp/2D/ST_Apply.png)

## Additional resources

  * [Work with sprites](../sprite/sprite-landing.html)
  * [Use the Sprite Editor](../sprite/sprite-editor/use-editor.html)

[](../urp/2d-light-masking.html)

Masking

[](../urp/HDREmulationScale.html)

HDR emulation scale

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

