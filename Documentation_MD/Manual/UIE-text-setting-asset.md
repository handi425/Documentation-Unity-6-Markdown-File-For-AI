[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-text-setting-asset.html)
  * [中文](/cn/current/Manual/UIE-text-setting-asset.html)
  * [日本語](/ja/current/Manual/UIE-text-setting-asset.html)
  * [한국어](/kr/current/Manual/UIE-text-setting-asset.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-text-setting-asset.html)
  * [中文](/cn/current/Manual/UIE-text-setting-asset.html)
  * [日本語](/ja/current/Manual/UIE-text-setting-asset.html)
  * [한국어](/kr/current/Manual/UIE-text-setting-asset.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Work with text](UIE-work-with-text.html)
  * UITK Text Settings assets

[](UIE-advanced-text-generator.html)

Advanced Text Generator

[](UIE-fallback-font.html)

Fallback font

# UITK Text Settings assets

UI Toolkit stores project-wide text settings in the UITK Text Settings asset.
**UI**(User Interface) Allows a user to interact with your application. Unity
currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit uses a default UITK Text Settings
asset for your text objects.

For runtime UI, you can create and assign a UITK Text Settings asset to the
[Panel Setting](UIE-Runtime-Panel-Settings.html) asset, and edit the text
setting properties:

  * To create a UITK Text Settings, select **Assets** > **Create** > **UI Toolkit** > **Text Settings**. This creates a UITK Text Settings asset with the default values.
  * To assign a UITK Text Settings to a Panel Setting, select the Panel Setting and drag the UITK Text Settings to the Text Settings field in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window.

**Note** : In the current release, you can’t change the default UITK Text
Settings for Editor UI.

This section describes all the properties for the UITK Text Settings asset.
The UITK Text Settings asset controls the default values for all text objects
used within that Panel.

You can edit the paths to store the font assets, **sprite** A 2D graphic
objects. If you are used to working in 3D, Sprites are essentially just
standard textures but there are special techniques for combining and managing
sprite textures for efficiency and convenience during development. [More
info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) assets, custom style sheets, and the
color gradient presets. The paths must be a sub-folder of a `Resources`
folder. Create a `Resources` folder if you don’t have one in your project.

## Default Font Asset

After you [create a font asset](UIE-font-asset.html) from a font file, you
must place it in the path set to store all the font assets.

**Property** | **Description**  
---|---  
**Default Font Asset** | Default font to use when you create a new text object.  
**Path** | Path to store all the font assets.  
  
## Fallback Emoji Text Assets

Manage the global [fallback font assets](UIE-fallback-font.html) list for this
font asset.

**Note** : The [local fallback set in the Font Asset Properties](UIE-font-
asset-properties.html#fallback-font-assets) has precedence over the global
fallback .

**Property** | **Description**  
---|---  
**Text Asset List** | Select **+** and **-** to add and remove font slots.   
Click the circle icon next to a font to open an Object Picker where you can
choose a font asset.  
Drag the handles on the left side of any font asset to reorder the list.  
  
## Dynamic Font System Settings

Project-wide settings to handle missing glyphs.

**Property** | **Description**  
---|---  
**Missing Character Unicode** | Unicode of the character to use when a missing glyph isn’t in any of the fallback fonts.  
  
The default value of `0` produces the outline of a square.  
**Clear Dynamic Data on Build** | Clear all dynamic data and restore the font asset back to its default creation and empty state.  
**Disable Warnings** | Enable this if you don’t want to log a warning for every missing glyph.  
  
## Default Sprite Asset

After you [create a sprit asset](UIE-sprite.html), you must place it in the
path set to store all the sprite assets. You can set a default sprite asset
and reference the sprites in the default sprite asset by index or sprite name.

**Property** | **Description**  
---|---  
**Default Sprite Asset** |  [Sprite asset](UIE-sprite.html) to use by default.  
**Missing Sprite Unicode** | Unicode of the sprite for a missing sprite.  
**Path** | Path to store all the sprite assets.  
  
## Sprite Asset Fallback

The fallback list set in the Panel Text Setting is called the global fallback.
The [local fallback set in the Sprite Asset](UIE-sprite.html) has precedence
over the global fallback list.

**Property** | **Description**  
---|---  
**Sprite Asset Fallback List** | Add or remove a sprite asset in the fallback list. You can also drag the handles on the left side of any sprit asset to reorder the list.  
  
## Default Style Sheet

After you create a custom style sheet, you must place it in the path set to
store all the custom style sheet assets.

**Property** | **Description**  
---|---  
**Default Style Sheet** | Default [style sheet](UIE-style-sheet.html) to use by all text objects in the project.  
**Path** | Path to store all the custom style sheet assets.  
  
## Color Gradient Presets

Set the path to store all color gradients presets.

**Property** | **Description**  
---|---  
**Path** | Path to store the Color Gradient presets.  
  
## Line Breaking for Asian Languages

To get correct line-breaking behavior for Asian languages, specify which
characters behave as leading and following characters.

**Property** | **Description**  
---|---  
**Leading Characters** | Specify the text file that contains the list of leading characters.  
**Following Characters** | Specify the text file that contains the list of following characters.  
**Korean Line Breaking Rules** | Enable this to use modern rules.  
  
## Additional resources

  * [Font assets](UIE-font-asset.html)
  * [Style sheets assets](UIE-style-sheet.html)
  * [Include sprites in text](UIE-sprite.html)
  * [Color gradients](UIE-color-gradient.html)

[](UIE-advanced-text-generator.html)

Advanced Text Generator

[](UIE-fallback-font.html)

Fallback font

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

